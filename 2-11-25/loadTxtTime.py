import custom_parse_version
import numpy_load
import pandas_version
import time

filename = "NGC6341.dat"

#print("Numpy load...")
start = time.time()
numpy_load.func(filename)
stop = time.time()
timeTaken = round(stop-start,5)
print(f"Numpy took: {timeTaken} seconds")

#print("Custom load...")
start = time.time()
custom_parse_version.func(filename)
stop = time.time()
timeTaken = round(stop-start,5)
print(f"Custom took: {timeTaken} seconds")

#print("Pandas load...")
start = time.time()
pandas_version.func(filename)
stop = time.time()
timeTaken = round(stop-start,5)
print(f"Pandas took: {timeTaken} seconds")