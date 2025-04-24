startComp=$EPOCHREALTIME
gfortran oddball.f90 -o mything.superduperextension
stopComp=$EPOCHREALTIME

startRuntime=$EPOCHREALTIME
./mything.superduperextension
stopRuntime=$EPOCHREALTIME

compTime=$(echo "$stopComp - $startComp" | bc)
runtime=$(echo "$stopRuntime - $startRuntime" | bc)
totalTime=$(echo "$compTime + $runtime" | bc)

echo "Compilation time: $compTime"
echo "Runtime time: $runtime"
echo "Total time: $totalTime"

echo "Python stuff"

startPython=$EPOCHREALTIME
python3 rutherford.py
stopPython=$EPOCHREALTIME

pythonTime=$(echo "$stopPython - $startPython" | bc)

echo "Python time: $pythonTime"