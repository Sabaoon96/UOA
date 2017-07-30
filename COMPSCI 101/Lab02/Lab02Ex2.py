"""
COMPSCI101 Lab-02
Author: Sabaoon Raza Khan
"""

# Exercise 2.2:
import random

random_integer1 = random.randrange(75, 201)
random_integer2 = random.randrange(75, 201)

smallest = min(random_integer1, random_integer2)
largest = max(random_integer1, random_integer2)

print("Smallest random number generated was ", smallest, ".", sep = "")
print("Largest random number generated was ", largest, ".", sep = "")