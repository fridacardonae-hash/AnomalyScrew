# AnomalyScrew: interfaz de inspección

Esta carpeta contiene el repositorio Git de la interfaz. Ejecutar python main.py desde aquí. La documentación de abajo describe también carpetas de la raíz superior que no forman parte de este repositorio.

# AnomalyScrews

Inspección de anomalías en tres posiciones de tornillos; incluye interfaz de escritorio, preparación de imágenes y experimentos de entrenamiento PaDiM.

## Alcance de esta documentación

Basada en la revisión estática de los archivos locales del 22 de octubre de 2026. Los comandos son instrucciones de arranque deducidas del código; no se ejecutaron aplicaciones, instalaciones, entrenamientos ni conexiones a equipos.

## Estructura

| Ruta | Contenido |
| --- | --- |
| `backend/` | Lógica de inspección, procesamiento o servicios. |
| `frontend/` | Interfaz de usuario y recursos de presentación. |
| `m2_j0013/` | Datos o recursos locales; conservar su organización. |
| `pack_inv/` | Datos o recursos locales; conservar su organización. |
| `RTV/` | Datos o recursos locales; conservar su organización. |
| `testing/` | Datos de prueba. |

## Preparación

Se necesita Python y un entorno compatible con las versiones declaradas. La versión exacta de Python no se ha validado. En PowerShell, desde esta carpeta:

```powershell
python -m venv .venv-doc
.\.venv-doc\Scripts\Activate.ps1
python -m pip install -r "frontend/requirements.txt"
```

## Configuración

Revisar `frontend/config.json` antes del arranque. Sus claves de primer nivel son:

`Components`, `Image_correlation1`, `Image_correlation2`, `Image_correlation3`, `Image_correlation4`, `Modelbinpath`, `Folder_path`, `enviados_log`, `scorelimit1`, `scorelimit2`, `scorelimit3`, `log_path`, `model v3`, `PLC_IP`, `PLC_PORT`.

Ajustar rutas de imágenes y modelos, regiones de interés y límites de clasificación según la estación. Si aparecen PLC_IP y PLC_PORT, configurarlos para el equipo correspondiente. Mantener los archivos de modelo y metadatos requeridos por el código. Las rutas locales o compartidas deben existir y ser accesibles.

## Ejecución

Desde la raíz de esta carpeta, con el entorno activado:

```powershell
Set-Location frontend
python main.py
```

## Flujo de trabajo

1. Revisar configuración, modelos y carpetas de entrada/salida.
2. Abrir la interfaz y cargar las imágenes o activar el modo de seguimiento disponible.
3. Consultar los resultados de inspección y los registros generados por la variante utilizada.
4. Validar con muestras conocidas antes de habilitar comunicación con el PLC. Los módulos PLC incluyen escritura de bits.

## Observaciones específicas

La interfaz usa rutas relativas a frontend; ejecutar desde esa carpeta. backend/df reúne preparación de datos y backend/training experimentos PaDiM. Existen main.py, main2.py y multi_thread.py; no se determinó cuál es la versión de producción.

## Verificación y mantenimiento

La documentación se comprobó contra la estructura y el código local, sin prueba funcional. Si falla un import, revisar el entorno y el manifiesto de la variante; si falla una lectura, comprobar el directorio de trabajo y las rutas configuradas. Actualizar este README cuando cambien entradas, dependencias o configuración.
