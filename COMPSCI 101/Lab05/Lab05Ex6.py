"""
Author:
Date-written: August 2015
Lab 5 Exercise 5.6
Produces a list of selling prices by applying a markup to a list of cost prices.
"""

def main():
	cost_price_list = [1.47, 2.35, 12.78, 3.56, 11.19, 9.26, 56.37]
	selling_price_list = apply_markup(cost_price_list, 20)
	print("Cost prices:    ", cost_price_list)
	print("Selling prices: ", selling_price_list)
	
	
def apply_markup(price_list, markup):
	# You complete this function then delete this comment
	new_selling_prices = []
	for prices in price_list:
		new_selling_prices += [prices * (1 + (markup / 100))]
		for index in range(0, len(new_selling_prices)):
			new_selling_prices[index] = round(new_selling_prices[index], 2)
	return new_selling_prices
main()