@echo off
start cmd /k "cd Back && uvicorn main:app --reload"
start cmd /k "cd Front && npm run dev"