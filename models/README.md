# Modelos

`lightgbm_reentrenado_usuario1_20261015.txt` está incluido **sólo en la copia local**. Se produjo en una corrida aislada para explicar con SHAP cinco candidatos de banda media del usuario 1. No es el checkpoint original de la evaluación de Test auditada; sus scores difieren de los scores previamente exportados (diferencia máxima observada: 0,009547). No utilizarlo como evidencia de que reproduce exactamente aquellas métricas.

Al ejecutar la notebook principal, la celda de selección de modelo guarda `lightgbm_model_auditado.txt` aquí. Ambos archivos están excluidos de Git por defecto. Para reproducir las métricas, ejecutar el pipeline completo y usar el modelo que genera la propia notebook; conservar también su Optuna DB, versiones y hashes.
