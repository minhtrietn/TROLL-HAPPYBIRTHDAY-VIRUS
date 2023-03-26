reg delete "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer" /v "NoDesktop" /f
taskkill /f /im explorer.exe && start explorer.exe
