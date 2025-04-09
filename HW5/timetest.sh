startComp=$EPOCHREALTIME
gfortran rk4.f90 -o rk4.exe
stopComp=$EPOCHREALTIME

startRuntime=$EPOCHREALTIME
./rk4.exe
stopRuntime=$EPOCHREALTIME

compTime=$(echo "$stopComp - $startComp" | bc)
runtime=$(echo "$stopRuntime - $startRuntime" | bc)
totalTime=$(echo "$compTime + $runtime" | bc)

echo "Compilation time: $compTime"
echo "Runtime time: $runtime"
echo "Total time: $totalTime"