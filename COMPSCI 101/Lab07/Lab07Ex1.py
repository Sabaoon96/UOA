"""
Lab 7 Ex 1
Author: Sabaoon Raza Khan
This program calculates and prints the area and perimeter
of a rectangle.  The length and width are entered by the user.
Date: September, 2015
"""

def main(): 
	length, width = get_length_and_width()
	area, perimeter = calculate_area_and_perimeter(length, width) 
	print_area_and_perimeter(area, perimeter) 
	
def get_length_and_width():
	length = input("Enter length: ")
	width = input("Enter width: ")
	return length, width
	
def calculate_area_and_perimeter(length, width) :
	length = float(length)
	width = float(width)
	area = length * width
	perimeter = (length + width) * 2
	return area, perimeter

def print_area_and_perimeter(area, perimeter):
	print("Area of rectangle is:", round(area,1), "square cms.")
	print("Perimeter of rectangle is:", round(perimeter,1), "cms.")
	
main()    



