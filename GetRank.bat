:start
echo Start: %date% %time%
python BaHaSpider.py
echo End: %date% %time%
choice /t 7200 /d y /n >nul

goto start