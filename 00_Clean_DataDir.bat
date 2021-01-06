@echo off

:begin

set fname=bkup_data
for /f "tokens=1-4 delims=/ " %%i in ("%date%") do ( set da=%%i )
SET ty=%TIME:~0,2%%TIME:~3,2%%TIME:~6,2%

echo Checking BackupFolder...
echo ------------------------------------------
if exist backup_folder (
		echo backup_folder Found!
) else (
		echo backup_folder NOT Found!
		echo Creating backup_folder ...
		mkdir backup_folder
		mkdir backup_folder\BKP_cleaned_data
		mkdir backup_folder\BKP_data
)
echo Done
echo.
echo.

echo Moving files and folders to backup_folder ...
echo ----------------------------------------------
if exist data ( 
    echo Found existing 'data' directory!
    echo.
    move data backup_folder\BKP_data\%fname%_%ty%_%da%
    ) else (
        echo No existing files and folder found
        echo Nothing to clean
        )
echo Done
echo.
echo.

echo Creating required directory structure ...
echo ----------------------------------------------
mkdir data
mkdir data\faults
mkdir data\test
echo Done
echo.
echo.

:end
