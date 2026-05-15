<img width="1024" height="369" alt="image" src="https://github.com/user-attachments/assets/64ae23c3-2e99-497b-9049-8a6b2222cc2c" />


FastAPI Mastery: From Fundamentals to Advanced Patterns 🚀
==========================================================

Welcome to my **FastAPI** learning repository! This project is a curated collection of implementations covering everything from basic routing to advanced security and templating patterns. It serves as a practical reference for building robust, high-performance Python web APIs.

🛠️ Core Implementations
------------------------

This repository is organized by specific features and concepts:

| Category | File Examples | Key Concepts |
| :--- | :--- | :--- |
| **Routing & Params** | `hello.py`, `pathparameters.py`, `queryparameter.py` | Basic GET/POST, dynamic URLs, and filtering. |
| **Data Integrity** | `pydantic_class.py`, `validation.py`, `request_body.py` | Schema definition, type hinting, and strict validation. |
| **Security & Web** | `practical_cors.py`, `cookie.py`, `headers.py` | Cross-Origin resource sharing, session cookies, and custom headers. |
| **Logic & UI** | `dependecyuse.py`, `practicaljinja.py`, `templates.py` | Dependency Injection, Jinja2 rendering, and static files. |
| **API Design** | `responsemode.py` | Controlling output data with Response Models. |

🚀 Getting Started
------------------

### 1\. Clone the repository
```bash
git clone [https://github.com/HP04Harsh/FastAPI.git](https://github.com/HP04Harsh/FastAPI.git)
cd FastAPI
```

### 2\. Install Dependencies

Ensure you have Python 3.7+ installed, then run:
```
pip install fastapi uvicorn[standard] jinja2
```

### 3\. Run a Module

To start the development server for any specific file (e.g., the Jinja2 example):
```
uvicorn practicaljinja:app --reload
```

#### 🔍 Interactive Documentation

Once the server is running, FastAPI automatically generates beautiful, interactive documentation for you:

*   Swagger UI: [http://127.0.0.1:8000/docs](https://www.google.com/search?q=http://127.0.0.1:8000/docs) — Test your endpoints directly from the browser.
    

*   Redoc: [http://127.0.0.1:8000/redoc](https://www.google.com/search?q=http://127.0.0.1:8000/redoc) — Clean, professional API documentation.
    

#### 📂 Directory Highlights

*   /templates: Contains HTML files used for Jinja2 rendering.   

*   staticfiles.py: Demonstrates how to serve CSS, JS, and Images.

*   .gitignore: Optimized for Python development to keep the repo clean.
    

Author: [Harsh Pardhi](https://github.com/HP04Harsh)
