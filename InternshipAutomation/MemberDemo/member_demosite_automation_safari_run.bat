tasklist /fi "imagename eq javaw.exe" | find ":" > nul
if errorlevel 0 start C:\Python34\Scripts\selenium-server-standalone-2.45.0.jar

member_demosite_automation_safari_v4.py