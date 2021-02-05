@echo off
cls
python --version
pip --version
echo ====================
echo Installing required packages
echo ====================
pip install requests
pip install clint
pip install click
pip install pyinstaller
echo Installed packages
echo ====================
pyinstaller --noconfirm --onefile --console --name "hlm"  "hlm.py"
