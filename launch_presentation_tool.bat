@echo off
title Bank of Namibia Sandbox - Credit Risk Scoring Tool
color 0b
echo ===============================================================================
echo     BANK OF NAMIBIA (BoN) FINTECH REGULATORY SANDBOX PROTOTYPE
echo     Digital Micro-Lending Credit Risk Scoring & Explainability Tool
echo ===============================================================================
echo     Candidate : Percyviarance Minsozi Simasiku (Student ID: 201061589)
echo     Supervisor: Mrs. Johanna Nelulu
echo     University: Department of Computer Science, University of Namibia
echo ===============================================================================
echo.
echo Starting interactive presentation prototype...
echo The web dashboard will open automatically in your browser.
echo.

cd /d "%~dp0"
call .venv\Scripts\streamlit.exe run app.py --server.port 8501 --server.headless false

pause
