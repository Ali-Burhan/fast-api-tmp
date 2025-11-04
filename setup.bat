@echo off
echo Setting up FastAPI Application...

echo.
echo Creating virtual environment...
python -m venv venv

echo.
echo Activating virtual environment...
call venv\Scripts\activate.bat

echo.
echo Installing dependencies...
pip install -r requirements.txt

echo.
echo Creating .env file...
if not exist .env (
    copy .env.example .env
    echo .env file created. Please update it with your configuration.
) else (
    echo .env file already exists.
)

echo.
echo Setup complete! Run 'venv\Scripts\activate.bat' to activate the virtual environment.
echo Then run 'run.bat' to start the application.
pause
