# Clínica Salud Integral - Sistema de Gestión

Sistema web para la gestión administrativa de una clínica: permite registrar, consultar y editar pacientes y médicos, además de visualizar un dashboard con estadísticas generales.

## Tecnologías utilizadas

- Python 3
- Flask
- MySQL
- HTML5 / CSS3
- Jinja2 (motor de plantillas de Flask)

## Funcionalidades

- Registro de pacientes con historia clínica completa
- Registro de médicos con especialidad y días de atención
- Edición de datos de pacientes y médicos
- Historial completo de pacientes registrados
- Listado completo del equipo médico
- Dashboard principal con estadísticas (total de pacientes, médicos y fecha actual)

## Estructura del proyecto

clinica-salud-integral/
├── Codigo.py              # Rutas y lógica principal de Flask
├── Inicio.py              # Conexión a la base de datos
├── Base_Datos.sql         # Script de creación de la base de datos
├── requirements.txt       # Dependencias del proyecto
├── .env.example           # Ejemplo de variables de entorno
├── .gitignore
├── templates/
│   ├── menu.html
│   ├── paciente.html
│   ├── medico.html
│   ├── historial.html
│   ├── lista_medicos.html
│   ├── datos_pacientes.html
│   └── datos_medicos.html
└── static/
    ├── dashboard.css
    ├── paciente.css
    ├── medico.css
    └── lista.css

## Requisitos previos

- Python 3.9 o superior
- MySQL Server instalado y corriendo
- pip

## Instalación

1. Cloná el repositorio
```bash
git clone https://github.com/tu-usuario/clinica-salud-integral.git
cd clinica-salud-integral

2. Creá un entorno virtual (opcional pero recomendado)
```bash
python -m venv venv
source venv/bin/activate - En Windows: venv\Scripts\activate

3. Instalá las dependencias
```bash
pip install -r requirements.txt
```

4. Configurá la base de datos
- Abrí MySQL (O base de datos que utilizes) y ejecutá el script `Base_Datos.sql`.
- Esto crea la base `salud_integral` con las tablas `pacientes` y `medicos`, junto con datos de prueba.
- En caso contrario, dejare la hoja de sql para exportar directamente donde todos los datos son ficticion y a modificar tanto en la ejecucion del programa como en la Base de datos

5. Configurá las variables de entorno
```bash
cp .env.example .env

```
- Completá el archivo `.env` con tus credenciales de MySQL (usuario, contraseña, host).

6. Ejecutá la aplicación
```bash
python Codigo.py 
```

## Uso

Con el servidor corriendo, accedé desde el navegador a:

http://localhost:5000

### Rutas principales

| Ruta | Método | Descripción |
|---|---|---|
| `/` | GET | Dashboard principal con estadísticas |
| `/paciente` | GET | Formulario de registro de paciente |
| `/guardar_paciente` | POST | Guarda un nuevo paciente en la base de datos |
| `/lista_pacientes` | GET | Historial completo de pacientes |
| `/editar_paciente/<id>` | GET | Formulario de edición de un paciente |
| `/actualizar_paciente` | POST | Actualiza los datos de un paciente |
| `/medico` | GET | Formulario de registro de médico |
| `/guardar_medico` | POST | Guarda un nuevo médico en la base de datos |
| `/lista_medicos` | GET | Listado completo de médicos |
| `/editar_medico/<id>` | GET | Formulario de edición de un médico |
| `/actualizar_medico` | POST | Actualiza los datos de un médico |

## Roadmap / Mejoras futuras

- [ ] Eliminar registros de pacientes y médicos
- [ ] Buscador y filtros en los listados
- [ ] Validación de DNI duplicado antes de insertar
- [ ] Paginación en listados extensos
- [ ] Sistema de login y roles de usuario (administración / recepción)
- [ ] Historial de turnos y citas médicas
- [ ] Exportar historia clínica a PDF

## Licencia

Este proyecto está bajo la licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.

## Autor

Desarrollado por **[Tu Nombre]** — [tu.email@ejemplo.com] — [github.com/tu-usuario](https://github.com/tu-usuario)
