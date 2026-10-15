#!/usr/bin/env python3
"""Comprueba archivos, hashes y exclusiones de Git; no modifica datos."""
from pathlib import Path
import hashlib
import argparse
import subprocess
import sys

parser = argparse.ArgumentParser()
parser.add_argument('--strict', action='store_true', help='Exigir también caché, modelo y ejecución local')
args = parser.parse_args()
root = Path(__file__).resolve().parents[1]
manifest = root / 'manifest.sha256'
failed = []
for line in manifest.read_text().splitlines():
    if not line or line.startswith('#'):
        continue
    digest, relative = line.split('  ', 1)
    path = root / relative
    if not path.is_file():
        if args.strict or relative.startswith('data/raw/') or relative.startswith('optuna/'):
            failed.append(f'Falta: {relative}')
        else:
            print(f'OPCIONAL AUSENTE {relative}')
        continue
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            h.update(block)
    if h.hexdigest() != digest:
        failed.append(f'Hash diferente: {relative}')
    else:
        print(f'OK {relative}')
for relative in ['data/raw/orders.csv', 'data/processed/instacart.duckdb',
                 'models/lightgbm_reentrenado_usuario1_20261015.txt']:
    result = subprocess.run(['git', 'check-ignore', '-q', relative], cwd=root)
    if result.returncode != 0:
        failed.append(f'Git no ignora: {relative}')
if failed:
    print('\n'.join(failed), file=sys.stderr)
    sys.exit(1)
print('Hashes y exclusiones de Git correctos.')
