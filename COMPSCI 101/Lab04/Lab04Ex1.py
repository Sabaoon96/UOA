"""
Lab 04 Exercise 4.1
Determines the price of a movie ticket, given the day and start time.
"""

def main():
	
	movie_price = get_movie_price("Monday", 14)
	display_price_of_movie("Monday", 14, movie_price)
	
	movie_price = get_movie_price("Tuesday", 16)
	display_price_of_movie("Tuesday", 16, movie_price)
	
	movie_price = get_movie_price("Wednesday", 16)
	display_price_of_movie("Wednesday", 16, movie_price)
	
	movie_price = get_movie_price("Thursday", 20)
	display_price_of_movie("Thursday", 20, movie_price)
	
	movie_price = get_movie_price("Friday", 12)
	display_price_of_movie("Friday", 12, movie_price)
	
	movie_price = get_movie_price("Friday", 17)
	display_price_of_movie("Friday", 17, movie_price)
	
	movie_price = get_movie_price("Saturday", 11)
	display_price_of_movie("Saturday", 11, movie_price)
	
	movie_price = get_movie_price("Saturday", 24)
	display_price_of_movie("Saturday", 24, movie_price)
	
	movie_price = get_movie_price("Sunday", 11)
	display_price_of_movie("Sunday", 11, movie_price)
	
def get_movie_price(day, hour):
#	Complete this function then delete this comment.
	price = 0
	
	if day == "Saturday" or day == "Sunday":
		price = 16.25
		return price
	
	elif day == "Tuesday":
		price = 10.75
		return price
	
	elif day == "Wednesday":
		price = 5.75
		return price
	
	if day == "Monday" or day == "Thursday" or day == "Friday":
		if hour < 17:
			price = 12.75
			
		elif hour >= 17:
			price = 15.75
	return price
			
def display_price_of_movie(day, hour, price):
	price = round(price, 2)
	if hour == 24:
		hour = 12
		am_or_pm = " midnight"
	elif hour == 12:
		am_or_pm = " noon"
	elif hour < 12:
		am_or_pm = "am"
	else:
		am_or_pm = "pm"
		hour = hour % 12

	print("Price of movie ticket at ", hour, am_or_pm, " on ", day, " is $", price, ".", sep = "")
		
main()
	