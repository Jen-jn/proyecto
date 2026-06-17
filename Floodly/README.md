# 🌊 Floodly - Sistema de Monitoreo de Inundaciones

## Descripción

Floodly es una aplicación de escritorio desarrollada en Python con CustomTkinter que proporciona un sistema completo de monitoreo y reporte ciudadano de inundaciones. La aplicación permite a los usuarios reportar zonas inundadas, ver alertas en tiempo real, acceder a consejos de seguridad y monitorear zonas críticas.

## Características

✅ **Splash Screen**: Pantalla de inicio animada con barra de progreso  
✅ **Sistema de Login**: Autenticación con email/contraseña y redes sociales  
✅ **Dashboard Principal**: Interfaz moderna con navegación lateral  
✅ **Mapa de Inundaciones**: Visualización de zonas de riesgo  
✅ **Reportes Ciudadanos**: Sistema para crear y ver reportes  
✅ **Alertas en Tiempo Real**: Notificaciones de peligros detectados  
✅ **Consejos de Seguridad**: Guías antes, durante y después de inundaciones  
✅ **Zonas Críticas**: Tabla de monitoreo de áreas de riesgo  
✅ **Interfaz Moderna**: Diseño profesional y responsivo  

## Requisitos

- Python 3.12 o superior
- pip (gestor de paquetes de Python)

## Instalación

### 1. Clonar o descargar el proyecto

```bash
git clone <url-del-repositorio>
cd Floodly
```

### 2. Crear un entorno virtual (recomendado)

```bash
python -m venv venv

# En Windows:
venv\Scripts\activate

# En macOS/Linux:
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

## Uso

Para ejecutar la aplicación:

```bash
python main.py
```

## Estructura del Proyecto

```
Floodly/
│
├── main.py                 # Punto de entrada principal
├── theme.py               # Paleta de colores y temas
├── README.md              # Este archivo
├── requirements.txt       # Dependencias del proyecto
│
└── views/
    ├── __init__.py
    ├── splash.py          # Pantalla de inicio
    ├── login.py           # Pantalla de login
    ├── forgot_password.py # Recuperación de contraseña
    ├── dashboard.py       # Dashboard principal
    ├── home.py            # Pantalla de inicio del dashboard
    ├── safety_tips.py     # Consejos de seguridad
    ├── critical_zones.py  # Zonas críticas
    ├── reports.py         # Reportes ciudadanos
    ├── create_report.py   # Crear nuevo reporte
    ├── report_detail.py   # Detalle del reporte
    └── alerts.py          # Pantalla de alertas
```

## Paleta de Colores

- **Primary Blue**: #0D5BD7
- **Secondary Cyan**: #2ED4F7
- **Danger Red**: #FF3B30
- **Warning Orange**: #FFB020
- **Success Green**: #28C76F
- **Background**: #F8FAFC
- **Card**: #FFFFFF
- **Text Dark**: #1F2937
- **Text Light**: #6B7280

## Flujo de la Aplicación

1. **Splash Screen** → Pantalla de inicio con animación (3 segundos)
2. **Login** → Autenticación del usuario
3. **Dashboard** → Panel principal con navegación lateral
4. **Vistas Disponibles**:
   - Inicio: Mapa y estado general
   - Consejos: Guías de seguridad
   - Zonas Críticas: Monitoreo de áreas
   - Reportes: Ver y crear reportes
   - Alertas: Notificaciones activas
   - Configuración: Ajustes de la app

## Nota Importante

Esta versión incluye:
- ✅ Datos completamente simulados
- ✅ Sin base de datos
- ✅ Sin backend
- ✅ Interfaz gráfica completamente funcional
- ✅ Navegación completa entre todas las vistas

## Características de Seguridad

### Consejos Antes de la Inundación
- Preparar mochila de emergencia
- Identificar rutas de evacuación seguras
- Mantener documentos importantes protegidos
- Llevar registro de bienes de valor
- Establecer plan de reunión familiar
- Tener números de emergencia a mano

### Acciones Durante la Inundación
- No cruzar calles o puentes inundados
- Desconectar suministro de electricidad
- Buscar zonas seguras en pisos superiores
- Evitar contacto con agua de inundación
- Mantener contacto con autoridades
- No manejar en zonas inundadas

### Recuperación Después de la Inundación
- Evitar agua contaminada
- Revisar daños estructurales
- Seguir indicaciones sanitarias
- Desinfectar superficies
- Desechar alimentos contaminados
- Documentar daños para seguros

## Zonas Críticas Monitoreadas

1. **Mercado Oriental** - Nivel Alto - Crítico
2. **El Riguero** - Nivel Alto - Crítico
3. **Barrio Altagracia** - Nivel Alto - En riesgo
4. **Barrio Pedro Árauz Palacios** - Nivel Alto - En riesgo
5. **Barrio San Judas** - Nivel Medio - Monitoreado

## Futuras Mejoras

- Integración con base de datos real
- API backend
- Geolocalización en tiempo real
- Integración con Google Maps
- Notificaciones push
- Sincronización en la nube
- Reportes en PDF
- Estadísticas y análisis

## Requisitos del Sistema

- **SO**: Windows, macOS, Linux
- **RAM**: 512 MB mínimo
- **Espacio en disco**: 100 MB

## Licencia

Este proyecto es de código abierto y está disponible bajo licencia MIT.

## Autor

Desarrollado como proyecto de demostración de CustomTkinter.

## Soporte

Para reportar problemas o sugerencias, por favor crear un issue en el repositorio.

---

**¡Gracias por usar Floodly!** 🌊

### Instrucciones de Uso Rápido

1. **Primera ejecución**: Verás la pantalla de splash con animación
2. **Login**: Usa cualquier email y contraseña para iniciar sesión
3. **Dashboard**: Explora todas las secciones desde la barra lateral
4. **Crear Reporte**: Haz clic en "Nuevo Reporte" para simular crear un reporte
5. **Ver Alertas**: Consulta alertas activas en la sección de Alertas

### Atajos de Teclado

- `Alt+F4` - Cerrar aplicación (Windows)
- `Cmd+Q` - Cerrar aplicación (macOS)
