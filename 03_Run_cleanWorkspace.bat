@echo off
echo CLEANING WORKSPACE
echo.

set fname=bkup_cleaned_data
for /f "tokens=1-4 delims=/ " %%i in ("%date%") do ( set da=%%i )
SET ty=%TIME:~0,2%%TIME:~3,2%%TIME:~6,2%

echo Checking for backup_folder ...
echo ----------------------------------------------
if exist backup_folder (
    echo Backup Folder Found
    ) else (
        echo Backup Folder not found creating 'backup_folder' 
        mkdir backup_folder
	mkdir backup_folder\BKP_cleaned_data
	mkdir backup_folder\BKP_data
        )
echo.
echo Done
echo.
echo.

echo Moving files and folders to backup_folder ...
echo ----------------------------------------------
if exist cleaned_data ( 
    echo Found existing cleaned_data directory!
    echo.
    move cleaned_data backup_folder\BKP_cleaned_data\%fname%_%ty%_%da%
    ) else ( 
        echo No existing files and folder found
        echo Nothing to clean 
        )
echo.
echo Done
echo.

echo Creating required directory structure ...
echo ----------------------------------------------
mkdir cleaned_data
mkdir cleaned_data\faults
mkdir cleaned_data\faults_current_only
mkdir cleaned_data\time
echo Done
echo.

PAUSE