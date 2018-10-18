#!/usr/bin/env python3

import statistics

agesData = [10,13,14,12,11,10,11,10,15]

print(f"Media: {statistics.mean(agesData)}") # Media/ Average
print(f"Mediana: {statistics.median(agesData)}") # Mediana / Median point
print(f"Moda: {statistics.mode(agesData)}") # Item mais frequemente apresentado

# print(statistics.variance(agesData)) # Variance
# print(statistics.stdev(agesData))
#
# import math
# print(math.sqrt(statistics.variance(agesData)))  #sqrt variance == stdev

