<p align="center"><img src="https://raw.githubusercontent.com/afmdiazh/Chess-Dot-Py/main/resources/logo.png"
height="130"></p>

<p align="center">ChessDotPy es una aplicación simple que se comunica con la API de <a href="https://www.chess.com/">Chess.com</a></p>

<p align="center"><a href="https://github.com/afmdiazh/Chess-Dot-Py/blob/main/README.md">README en inglés</a></p>

<p align="center"><img src="https://img.shields.io/github/languages/top/afmdiazh/Chess-Dot-Py" alt="Top Language Badge"/> <img src="https://img.shields.io/github/last-commit/afmdiazh/Chess-Dot-Py" alt="Last Commit Badge"/></p>

<p align="center"><a href="https://github.com/afmdiazh/Chess-Dot-Py/stargazers"><img src="https://img.shields.io/github/stars/afmdiazh/Chess-Dot-Py" alt="Stars Badge"/> <a href="https://github.com/afmdiazh/Chess-Dot-Py/network/members"><img src="https://img.shields.io/github/forks/afmdiazh/Chess-Dot-Py" alt="Forks Badge"/></a> <a href="https://github.com/afmdiazh/Chess-Dot-Py/pulls"><img  src="https://img.shields.io/github/issues-pr/afmdiazh/Chess-Dot-Py" alt="Pull Requests Badge"/></a> <a href="https://github.com/afmdiazh/Chess-Dot-Py/issues"> <img src="https://img.shields.io/github/issues/afmdiazh/Chess-Dot-Py" alt="Issues Badge"/></a> <a href="https://github.com/afmdiazh/Chess-Dot-Py/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/afmdiazh/Chess-Dot-Py?color=2b9348"></a> <a href="https://github.com/afmdiazh/Chess-Dot-Py/blob/master/LICENSE"><img src="https://img.shields.io/github/license/afmdiazh/Chess-Dot-Py?color=2b9348" alt="License Badge"/></a></p>

## Características

Con esta herramiente podemos acceder facilmente al perfil de cualquier jugador y ver la clasificación de cualquier modo de juego.
También nos facilita ver el rompecabezas diario y el historial de partidas de los jugadores.

La interfaz está dividida en secciones:

- Jugador:

  - Foto de perfil

  - Información del perfil

  - Estadísticas (también dividido en categorías)

- Historial:

  - Oponente

  - Color de las piezas

  - Puntuación

  - Porcentaje de precisión

  - Reglas y control de tiempo

- Clasificación:

  - Rango

  - Puntuación

  - Victorias, derrotas y empates

  - Nacionalidad y estilo

- Rompecabezas:

  - Rompecabezas diario

  - Rompecabezas aleatorio (se actualiza cada 15 segundos)

  - Soluciones

## Instalación

### Opción 1: Ejecutable ( Solo Windows )

Descarga un ejetuable generado automáticamente desde la [página de github actions](https://github.com/afmdiazh/Chess-Dot-Py/actions/workflows/pyinstaller.yml) o el último ejecutable publicado desde la [página de releases](https://github.com/afmdiazh/Chess-Dot-Py/releases) (preferiblemente este, ya que estas versiones están revisadas manualmente).

Ten en cuenta que los ejecutables generados automáticamente pueden no ser siempre tan estables como los de la página de releases.

### Opción 2: Instalación manual

1. Instala [Python](https://www.python.org/downloads/).

2. Descarga el repositorio o ejecuta el comando `git clone https://github.com/afmdiazh/Chess-Dot-Py` (requiere [git](https://git-scm.com/downloads)) para clonar el repositorio localmente.

3. Instala el gestor de paquetes [pip](https://pip.pypa.io/en/stable/) para instalar las librerías requeridas.

4. Instala las librerías requeridas con el comando `pip install dependencies.txt` (desde la carpeta src) o ejecutando `dependencies.bat`.

5. Ejecuta ChessDotPy con el commando `python main.py` (desde la carpeta src) o ejecutando `start.bat`.

## Uso

### Jugador

Para ver las estadísticas y el perfil de un jugador, dirígete a la pestaña Jugador y escribe su nombre. Después de eso, puede presionar enter o "Buscar" y, si el jugador existe, se cargarán sus estadísticas.

- Al hacer doble clic en el avatar del jugador, se abrirá su perfil de Chess.com en el navegador.

- Al presionar "Recargar" o F5 se recargará el perfil del jugador.

- Al pulsar borrar se borrará toda la sección.

### Historial

Para ver el historial de un jugador, dirígete a la pestaña Historial y escribe su nombre. Después de eso, puede presionar enter o "Buscar" y, si el jugador existe, se cargará su historial.

- Al hacer doble clic en cualquier partida, se abrirá un menú para acceder a los datos del oponente directamente.

- Al presionar "Recargar" o F5 se recargará el historial del jugador.

- Al pulsar borrar se borrará toda la sección.

### Clasificación

Para cargar los datos de la tabla de clasificación, dirígete a la pestaña Clasificación y presiona "Actualizar" o F5. Después de eso, tardará unos minutos en descargar toda la información de la tabla de clasificación y un poco más para descargar las imágenes de perfil en segundo plano.

- Al hacer doble clic en cualquier jugador, se abrirá un menú para acceder a los datos del jugador directamente.

- Hacer doble clic en cualquier nombre de columna cambiará el orden predeterminado por el de esa columna.

### Rompecabezas

Para cargar los datos del rompecabezas, dirígete a la pestaña Rompecabezas y presiona "Obtener rompecabezas diario" o "Obtener rompecabezas aleatorio" (los rompecabezas aleatorios se actualizan cada 15 segundos, más o menos). Después de que se cargue el rompecabezas, puedes presionar "Revelar solución" para ver los movimientos necesarios para resolver el rompecabezas.

- Al hacer doble clic en la imagen del rompecabezas diario, se abrirá el rompecabezas en el navegador.

## Capturas de pantalla

<p  align="center"><img  src="https://raw.githubusercontent.com/afmdiazh/Chess-Dot-Py/main/resources/s1.png"></p>

<p  align="center"><img  src="https://raw.githubusercontent.com/afmdiazh/Chess-Dot-Py/main/resources/s2.png"></p>

<p  align="center"><img  src="https://raw.githubusercontent.com/afmdiazh/Chess-Dot-Py/main/resources/s3.png"></p>

<p  align="center"><img  src="https://raw.githubusercontent.com/afmdiazh/Chess-Dot-Py/main/resources/s4.png"></p>

<p  align="center"><img  src="https://raw.githubusercontent.com/afmdiazh/Chess-Dot-Py/main/resources/s5.png"></p>

## Módulos usados

- [Chess.com](https://pypi.org/project/chess.com/ "Chess.com") - API Wrapper para Chess.com

- [PyQt5](https://pypi.org/project/PyQt5/ "PyQt5") - Interfaz gráfica

- [Qt Material](https://pypi.org/project/qt-material/ "Qt Material") - Temas de interfaz gráfica

- [Emoji](https://pypi.org/project/emoji/ "Emoji") - Convertir strings de texto a emojis

- [Pyinstaller](https://pypi.org/project/pyinstaller/ "Pyinstaller") - Crear ejecutables con código Python

## Versionado

El sistema de versionado utilizado para este proyecto está basado en [Semver](https://semver.org/lang/es/ "Semver"), y sigue el patrón de X.Y.Z:

- X: Versión grande o com cambios de compatibilidad

- Y: Funcionalidad nueva

- Z: Parches o cambios pequeños

## Contribuciones

Las pull requests son bienvenidas. Para cambios más grandes, abra un asunto primero para discutir lo que le gustaría cambiar

## Licencia

[MIT](https://choosealicense.com/licenses/mit/)
