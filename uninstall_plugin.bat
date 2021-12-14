:: YaPyCon YASARA plugin un-installer (Windows version)
::
:: Athanasios Anastasiou, Dec 2021

@echo off

echo Removing YaPyCon from YASARA.
echo.
echo.

:: Check if YASARA_HOME has been defined
if  not defined YASARA_HOME (
    :: Variable has not been defined
    :: Inform and exit
    echo The installer requires that the variable YASARA_HOME is set, prior to installing the plugin.
    echo You can set that variable by:
    echo     ^> set YASARA_HOME=/some/path/to/yasara
    echo.
    exit 1 )

:: YASARA_HOME is defined, check that it points to a YASARA folder (a very basic check is performed here).
if not exist "%YASARA_HOME%\bab\" (
    if not exist "%YASARA_HOME%\cif\" (
        if not exist "%YASARA_HOME%\plg\" (
            if not exist "%YASARA_HOME%\yasara.exe" (
                :: The variable is set but the yasara directory does not look like a valid installation directory
                :: Inform and exit
                echo The YASARA_HOME environment variable points to %YASARA_HOME%, which does not appear to
                echo be a valid YASARA installation. Please check the variable ^(or your installation^) and try
                echo again.
                echo.
                exit 1 ))))

:: Check that the file exists
if not exist  "%YASARA_HOME%\plg\yapycon.py" (
    :: If the file does not exist, inform and exit
    echo %YASARA_HOME%\plg\yapycon.py does not exist.
    echo No further action was taken.
    echo.
    exit 1 )

:: If the file exists then proceed to delete it
del "%YASARA_HOME%\plg\yapycon.py"
del "%YASARA_HOME%\plg\yasara_kernel.py"
:: Inform and exit
echo The YaPyCon plugin and its dependencies were succesfully removed from YASARA"
echo.
