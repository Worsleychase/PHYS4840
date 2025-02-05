# HW1.py

# Problem 2
import numpy as np

max_money = float(input("Enter the amount of money you have for sandwiches: "))

prices = {
    "Ham": 3.65,
    "Apple Brie": 4.25,
    "PB&J": 3.00,
    "Turkey": 3.35
}
half_prices = {key: 0.6 * val for key, val in prices.items()}

combinations = []
spare_change_values = []

for h, h_price in half_prices.items():
    for ham_count in range(int(max_money // prices["Ham"]) + 1):
        for apple_count in range(int(max_money // prices["Apple Brie"]) + 1):
            for pbj_count in range(int(max_money // prices["PB&J"]) + 1):
                for turkey_count in range(int(max_money // prices["Turkey"]) + 1):
                    for half_sandwich in prices.keys():
                        total_cost = (
                            ham_count * prices["Ham"]
                            + apple_count * prices["Apple Brie"]
                            + pbj_count * prices["PB&J"]
                            + turkey_count * prices["Turkey"]
                            + half_prices[half_sandwich]
                        )
                        if total_cost <= max_money:
                            spare_change = max_money - total_cost
                            if round(spare_change * 100) % 25 == 0:
                                combinations.append((ham_count, apple_count, pbj_count, turkey_count, half_sandwich))
                                spare_change_values.append(spare_change)

if combinations:
    spare_change_values = np.array(spare_change_values)
    combinations = np.array(combinations, dtype=object)
    best_combo_idx = spare_change_values.argmin()
    best_combo = combinations[best_combo_idx]

    print(f"The least spare change is: ${spare_change_values.min():.2f}")
    print("Best sandwich combo:")
    print(f"Ham: {best_combo[0]}, Apple Brie: {best_combo[1]}, PB&J: {best_combo[2]}, Turkey: {best_combo[3]}")
    print(f"Half sandwich: {best_combo[4]}")
else:
    print("No valid combination found.")

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Problem 3

max = 10000
primes = [2]

import math

for n in range(3, 10001, 2):
    is_prime = True
    sqrt_n = math.isqrt(n)

    for p in primes:
        if (p > sqrt_n):
            break 
        if (n % p == 0):
            is_prime = False
            break 

    if is_prime:
        primes.append(n)

#print(f"Number of primes found: {len(primes)}")\
print(primes)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Problem 4

def recurA(n):
    if (n == 0):
        return 1
    return ((4*n-2)/(n+1))*recurA(n-1)

print(recurA(100))

def recurB(m,n):
    if (n == 0):
        return m
    return recurB(n,(m%n))

print(recurB(108,192))