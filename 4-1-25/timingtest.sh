startFortran=$EPOCHREALTIME

gfortran RK2.f90 -o rk2.exe
./rk2.exe

stopFortran=$EPOCHREALTIME
startPython=$EPOCHREALTIME

/bin/python3 /home/chaserix/Documents/PHYS4840/4-1-25/exercise3.py

stopPython=$EPOCHREALTIME

FortranTime=$(echo "$stopFortran - $startFortran" | bc)
PythonTime=$(echo "$stopPython - $startPython" | bc)

echo "Fortran time: $FortranTime"
echo "Python time: $PythonTime"
