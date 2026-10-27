@echo off
title Push to GitHub and Deploy Prototype to the Web
color 0b

echo ===============================================================================
echo     CONNECT PROTOTYPE TO YOUR GITHUB ACCOUNT AND DEPLOY TO THE WEB
echo ===============================================================================
echo     Candidate : Percyviarance Minsozi Simasiku (Student ID: 201061589)
echo     Project   : Credit Risk Prediction for Financial Inclusion in Namibia
echo ===============================================================================
echo.

set "PATH=%PATH%;C:\Users\201061589\AppData\Local\Programs\Git\cmd;C:\Program Files\GitHub CLI"

cd /d "%~dp0"

echo [STEP 1/3] Checking GitHub Login Status...
gh auth status >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo You need to log in to your GitHub account.
    echo A one-time code will be displayed below, and your browser will open.
    echo Press any key to open the GitHub login page...
    pause >nul
    gh auth login --web -p https -w
) else (
    echo [OK] Already logged in to GitHub!
)

echo.
echo [STEP 2/3] Creating GitHub Repository and Pushing Project...
gh repo create thesis_credit_risk --public --source=. --remote=origin --push
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo [NOTICE] Attempting to push to existing remote...
    git push -u origin main
)

echo.
echo [OK] Project is now live on your GitHub account!
echo.
echo [STEP 3/3] Deploying Prototype to the Web (Streamlit Community Cloud)...
echo.
echo To make your prototype accessible to ANYONE on the internet:
echo 1. Your browser will open to https://share.streamlit.io
echo 2. Click "Sign in with GitHub"
echo 3. Click "Create app" or "New app"
echo 4. Select:
echo      Repository: thesis_credit_risk
echo      Branch:     main
echo      Main file:  app.py
echo 5. Click "Deploy!"
echo.
echo In 1-2 minutes, you will get a public link (e.g., https://credit-risk-namibia.streamlit.app)
echo that you can share with your supervisor, put on your CV, or add to your thesis!
echo.
echo Press any key to open Streamlit Cloud and your GitHub repository in your browser...
pause >nul

start https://share.streamlit.io
gh browse

echo.
echo All done! You can close this window.
pause
