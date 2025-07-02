
# 🔥 Playwright Automation with Python + Pytest + GitHub Actions

Este es un proyecto de automatización de pruebas end-to-end utilizando **Playwright con Python y Pytest**, implementando buenas prácticas como **Page Object Model (POM)** y ejecutando pipelines en **GitHub Actions**.

---

## 🚀 Características

- ✔️ Automatización de UI con Playwright y Python.
- ✔️ Implementación de Page Object Model (POM).
- ✔️ Manejo de datos sensibles con variables de entorno (.env y GitHub Secrets).
- ✔️ Reportes en HTML generados con pytest-html.
- ✔️ Ejecución continua con GitHub Actions.
- ✔️ Proyecto escalable y organizado.

---

## 📦 Estructura del Proyecto

```
.
├── .github/workflows/       # Workflows de GitHub Actions
├── pages/                   # Page Objects
│   ├── loginpage.py
│   └── employee_page.py
├── tests/                   # Archivos de pruebas
│   ├── 01_login_test.py
│   └── 02_add_employee.py
├── .env                     # Variables de entorno locales
├── pytest.ini                # Configuración de pytest
├── requirements.txt          # Dependencias
├── README.md                 # Este archivo
```

---

## 🛠️ Instalación local

1. Clona el repositorio:

```bash
git clone https://github.com/tuusuario/tu-repo.git
cd tu-repo
```

2. Instala dependencias:

```bash
pip install -r requirements.txt
playwright install
```

3. Crea un archivo `.env`:

```env
ORANGE_USERNAME=Admin
ORANGE_PASSWORD=admin123
```

4. Ejecuta los tests:

```bash
pytest tests/ --html=report.html --self-contained-html
```

---

## ☁️ Ejecución en GitHub Actions

1. Agrega los secrets en tu repositorio:

- `ORANGE_USERNAME`
- `ORANGE_PASSWORD`

2. El workflow en `.github/workflows/python-playwright.yml` se ejecutará automáticamente en cada push o pull request a `main`.

3. Los reportes HTML estarán disponibles como artifacts descargables en cada run.

---

## 📄 Reportes

Los reportes se generan automáticamente en formato HTML con `pytest-html` y son descargables desde GitHub Actions o localmente.

---

## 🚩 Tests disponibles

| Test                     | Descripción                          |
|--------------------------|---------------------------------------|
| `01_login_test.py`       | Valida el login exitoso en OrangeHRM |
| `02_add_employee.py`     | Agrega un nuevo empleado             |

---

## 🏗️ Stack utilizado

- [Playwright](https://playwright.dev/python/) — Automation framework
- [Pytest](https://docs.pytest.org/) — Test runner
- [pytest-html](https://pypi.org/project/pytest-html/) — Reportes HTML
- [python-dotenv](https://pypi.org/project/python-dotenv/) — Manejo de .env
- [GitHub Actions](https://docs.github.com/en/actions) — CI/CD

---

## 🚀 Próximas mejoras

- 🔄 Data-driven testing con JSON o CSV.
- 📸 Captura de screenshots en fallos.
- 📑 Validación de empleados desde tablas.
- 🧠 Uso de fixtures avanzadas y storage_state.
- ☁️ Pipeline con matrix para navegadores.

---

## 🧑‍💻 Autor

- Julio Soto (XJoule) — [GitHub](https://github.com/xjoule42)

---
