@echo off

echo %date% > data.txt

rem Przypisanie zmiennych do plików
for /f "usebackq delims=" %%i in (`type data.txt`) do set "datas=%%i"
for /f "usebackq delims=" %%i in (`type plik.txt`) do set "time=%%i"

rem Zmiana aktualnego czasu na ilość minut
for /f "tokens=2 delims==" %%a in ('wmic OS Get localdatetime /value') do set "dt=%%a"
set "HH=%dt:~8,2%"
set "Min=%dt:~10,2%"
set /a "lmin = %HH%*60 + %Min%"

rem jeżeli po uruchomieniu daty nie będą zbierzne dane pozostałego czasu się odświerzą
if %datas% neq %date% (
    echo 200 > plik.txt
)

rem ustalenie pozostałego czasu dodająć do aktulnego pozostały regresujący (def 200)
set /a "exit = lmin+%time%" 

rem jeżeli pojawi się godzina 00:00 (następny dzień) program się zrestartuje odnawiając pozostały czas bez wyłączanie komputera
if %HH% equ 00 (
    if %Min% equ 00 (
        timeout /t 60
        start timer.bat
        taskkill /im cmd.exe /f
    )
    
)

rem pętla odpowiadająca za aktualizowanie pozostałęgo czasu
:loop
for /f "tokens=2 delims==" %%a in ('wmic OS Get localdatetime /value') do set "dt=%%a"


set "HH=%dt:~8,2%"
set "Min=%dt:~10,2%"
set /a "lmin = %HH%*60 + %Min%"

rem obliczanie pozostałęgo czasu i wpisanie go do pliku
set /a "able=%exit%-%lmin%"
echo pozostalo ci %able% minut
echo %able% > plik.txt

rem gdy wartość dostępnych minut spadnie do zera skrypt wyłączy system
if %able == 0 (
    echo wyłączam komputer
    rem shutdown
)

timeout /t 60
goto loop

pause