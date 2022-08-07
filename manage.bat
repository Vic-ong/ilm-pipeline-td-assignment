@echo off

setlocal
SET COMMAND=%1
SET PROJECT_NAME=priority-queue-app

echo [93m*** starting %PROJECT_NAME% ***[0m
echo [97mExecuting command -- [36m%COMMAND%[0m

@REM Install dependencies
if %COMMAND% == install (
  echo [97mInstalling dependencies...[0m
  pip install -r requirements.txt
)

@REM Set environment variables and start application
if %COMMAND% == start (
  echo [97mStarting application...[0m
  FOR /F "tokens=*" %%i in ('type .env') do SET %%i
  python src/index.py
)

:usage
echo [97mApplication exited[0m
echo [93m*** closing %PROJECT_NAME% ***[0m
endlocal
exit /B 1