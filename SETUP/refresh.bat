@echo off
taskkill /fi "imagename eq explorer.exe" /f
cd /d %userprofile%\AppData\Local
del IconCache.db /a
start explorer.exe
