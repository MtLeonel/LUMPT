@echo off
setlocal
where py >nul 2>nul
if not errorlevel 1 (
  py -3 "%~dp0install_lumpt.py"
) else (
  python "%~dp0install_lumpt.py"
)
endlocal