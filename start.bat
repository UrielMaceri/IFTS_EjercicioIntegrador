@echo off
start cmd /k "cd Back && uvicorn main:app --reload"
start cmd /k "cd Front && npm run dev"

timeout /t 3 /nobreak >nul
start http://localhost:8888