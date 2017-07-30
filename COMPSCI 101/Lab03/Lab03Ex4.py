"""
Lab 3 Ex 4
Author: Sabaoon Raza Khan

"""

def main():
	formatted_date = format_date(12, 7, 15)
	print(formatted_date)
	formatted_date = format_date(1, 3, 0)
	print(formatted_date)
	
def format_date(day, month, year):

	day = str(day)
	day = "0" * (2 - len(day)) + day
	
	month = str(month)
	month = "0" * (2 - len(month)) + month
	
	year = str(year)
	year = "0" * (2 - len(year)) + year
	
	formatted_date = day + "/" + month + "/" + year
	return formatted_date
	
main()