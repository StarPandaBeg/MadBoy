@echo off
cd %appdata%/xsploit
taskkill /f /im python.exe
taskkill /f /im ngrok.exe
run.bat