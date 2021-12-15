:: YaPyCon YASARA plugin installer (Windows Version)
::
:: Athanasios Anastasiou, Dec 2021

@echo off

echo YaPyCon Installer
echo.
echo.

:: Check if YASARA_HOME has been defined
if not defined YASARA_HOME (
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

:: Check that you are not about to overwrite an existing file
if exist "%YASARA_HOME%\plg\yapycon.py" (
    echo %YASARA_HOME%\plg\yapycon.py already exists.
    echo Installation aborted.
    echo.
    echo If you are absolutely sure that you would like to proceed, please
    echo run uninstal_plugin.sh, first, followed by install_plugin.sh.
    echo.
    exit 1 )

:: Everything looks good, go ahead with the installation in /plg
copy "yapycon\yapycon.py" "%YASARA_HOME%\plg\"
copy "yapycon\yasara_kernel.py" "%YASARA_HOME%\plg\"
:: Inform and exit
echo YaPyCon and the associated yasara_kernel.py module were succesfully installed.
echo.
