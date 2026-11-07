@echo off
chcp 65001 >nul
echo ===================================================
echo   成大 1107 課堂 專屬語音討論AI助教
echo ===================================================
echo 正在啟動後端服務與載入課堂知識庫...
start "" "http://localhost:8080"
python "E:\Gemin bak\ncku_course_assistant\app\server.py"
pause
