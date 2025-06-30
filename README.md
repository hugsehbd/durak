# How to Run the Durak Game

## Prerequisites

- **Python 3.8 or higher**
- **Node.js 16 or higher**
- **npm** (comes with Node.js)

## 1. Backend (Python/FastAPI)

1. **Navigate to the project directory**:
    ```bash
    cd durak
    ```

2. **Install Python dependencies**:
    ```bash
    pip install -r backend/requirements.txt
    ```
    
    Or install manually:
    ```bash
    pip install fastapi uvicorn[standard] pydantic python-multipart typing-extensions
    ```

3. **Start the backend server**:
    ```bash
    uvicorn backend.main:app --reload
    ```
    - The API will be available at `http://127.0.0.1:8000/api`.

## 2. Frontend (React/Vite)

1. **Install Node.js dependencies** (in your project root):
    ```bash
    npm install
    ```

2. **Start the frontend dev server**:
    ```bash
    npm run dev
    ```
    - The app will be available at `http://localhost:5173` (or as shown in your terminal).

---

## Installation Troubleshooting

### Python Issues:
- If you get permission errors, try: `pip install --user -r backend/requirements.txt`
- For virtual environment: 
  ```bash
  python -m venv venv
  # On Windows:
  venv\Scripts\activate
  # On macOS/Linux:
  source venv/bin/activate
  pip install -r backend/requirements.txt
  ```

### Node.js Issues:
- If `npm install` fails, try: `npm install --legacy-peer-deps`
- Clear npm cache: `npm cache clean --force`

## Requirements Files

- **Backend**: `backend/requirements.txt` - Contains all Python dependencies
- **Frontend**: `package.json` - Contains all Node.js dependencies

## Quick Setup

1. **Backend setup**:
   ```bash
   cd backend
   pip install -r requirements.txt
   uvicorn main:app --reload
   ```

2. **Frontend setup** (in a new terminal):
   ```bash
   npm install
   npm run dev
   ```

## Notes

- You must run both the backend and frontend simultaneously for the game to work
- Bots must be Python files implementing the required interface (see `backend/example_bot.py` for an example)
- If you see security warnings after `npm install`, you can run `npm audit fix` or `npm audit fix --force` to attempt to resolve them. These warnings are common and do not usually affect development, but review them before using in production.
- For production deployment, consider using a production WSGI server like Gunicorn instead of uvicorn with --reload
