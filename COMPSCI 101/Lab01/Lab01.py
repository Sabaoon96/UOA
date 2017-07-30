"""
Lab 01 Ex 1.3
Author: Sabaoon Raza Khan
Date Written: 27th July 2015

"""

import math

# Part (a)
number_of_pounds = 92
number_of_whole_stones = number_of_pounds // 14
number_of_whole_pounds = number_of_pounds % 14
print("There are", number_of_whole_stones, "stones and", number_of_whole_pounds, "pounds in", number_of_pounds, "pounds.")
print()

#Part (b)
radius = 10
height = 30
surface_area = (2 * math.pi * radius ** 2) + (2 * math.pi * radius * height)
print("Surface area of cylinder is", round(surface_area), "square cms.")
print()

#Part (c)
height_of_peter = 1.63
weight_of_peter = 64.75
bmi = weight_of_peter / height_of_peter ** 2
print("Peter's bmi is ", round(bmi, 1), ".", sep = "")
print()

#Part (d)
number_of_years = 20 
amount_invested = 3000
rate = 0.04
total_value = amount_invested * (1 + rate)** number_of_years
print("Total value after ", number_of_years, " years would be $", round(total_value, 2), ".", sep = "")
