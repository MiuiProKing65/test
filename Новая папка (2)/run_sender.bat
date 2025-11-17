@echo off
color 0A
title 🚀 Telegram Auto Sender 😎

echo.
echo ╔══════════════════════════════════════╗
echo ║     🚀  TELEGRAM AUTO SENDER 😎      ║
echo ║  Сообщения каждые 5с в Избранное     ║
echo ╚══════════════════════════════════════╝
echo.

echo [START] Скрипт запущен в: %date% %time%
echo.

cd /d %~dp0
python sender.py

echo.
echo [END] Скрипт завершил работу.
pause