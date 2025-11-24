@echo off
REM Fact-Checking Reasoning Engine - Windows Launcher
REM Usage: run.bat "Your semantic probe claim here"

if "%~1"=="" (
    echo CRITICAL USAGE: run.bat "^<SemanticProbe Claim^>"
    exit /b 1
)

py cli.py %*
