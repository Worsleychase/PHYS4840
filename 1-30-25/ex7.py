import ex6
import numpy as np
import time

print("Sqrt test...")
start = time.time()
foo = ex6.sqrt(320918239832.239423)
stop = time.time()
print(f"My sqrt took {stop-start} seconds")
start = 0
stop = 0
start = time.time()
foo1 = np.sqrt(320918239832.239423)
stop = time.time()
print(f"Numpy sqrt took {stop-start} seconds")
print(f"Output difference = {foo - foo1}\n")

print("Floor test...")
start = time.time()
foo = ex6.floor(320918239832.239423)
stop = time.time()
print(f"My floor took {stop-start} seconds")
start = 0
stop = 0
start = time.time()
foo1 = np.floor(320918239832.239423)
stop = time.time()
print(f"Numpy floor took {stop-start} seconds")
print(f"Output difference = {foo - foo1}\n")

print("Round test...")
start = time.time()
foo = ex6.round(320918239832.239423,4)
stop = time.time()
print(f"My round took {stop-start} seconds")
start = 0
stop = 0
start = time.time()
foo1 = np.round(320918239832.239423,4)
stop = time.time()
print(f"Numpy round took {stop-start} seconds")
print(f"Output difference = {foo - foo1}\n")

print("Min test...")
start = time.time()
foo = ex6.min([213,2,230,53,0,23,58,45])
stop = time.time()
print(f"My min took {stop-start} seconds")
start = 0
stop = 0
start = time.time()
foo1 = np.min([213,2,230,53,0,23,58,45])
stop = time.time()
print(f"Numpy min took {stop-start} seconds")
print(f"Output difference = {foo - foo1}\n")

print("Argmin test...")
start = time.time()
foo = ex6.argmin([213,2,230,53,0,23,58,45])
stop = time.time()
print(f"My argmin took {stop-start} seconds")
start = 0
stop = 0
start = time.time()
foo1 = np.argmin([213,2,230,53,0,23,58,45])
stop = time.time()
print(f"Numpy argmin took {stop-start} seconds")
print(f"Output difference = {foo - foo1}")