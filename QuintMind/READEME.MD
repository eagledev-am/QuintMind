# QuintMind - Setup Guide

## 1. Create Virtual Environment

Create and activate a virtual environment for the project:

```bash
# Create virtual environment
python3 -m venv env

# Activate virtual environment
source env/bin/activate
```

## 2. Install Requirements

With the virtual environment activated, install all dependencies:

```bash
pip install -r requirements.txt
```

## 3. Setup Environment Variables

Create a `.env` file in the `QuintMind` directory with the following content:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
```

## 4. Access Swagger UI

After running the server, access the interactive API documentation:

- **Swagger UI**: `http://127.0.0.1:8000/api/schema/swagger-ui/`
- **ReDoc**: `http://127.0.0.1:8000/api/schema/redoc/`
- **OpenAPI Schema**: `http://127.0.0.1:8000/api/schema/`

## 5. Run Migrations and Start Server

```bash
# Navigate to project directory
cd QuintMind

# Apply database migrations
python manage.py makemigrations
python manage.py migrate

# Run development server
python manage.py runserver
```

The server will start at `http://127.0.0.1:8000/`