"""
Name: Sabaoon Raza Khan
UPI: skha787
ID: 983957824
Description: Class which defines a random rectangular region for all the rectangles, circles and arc shapes that is used in the program.
"""

import random

class RandRegion:
	def __init__(self, canvas_width, canvas_height):
		self.canvas_width = canvas_width
		self.canvas_height = canvas_height
		self.max_width = 100
		self.max_height = 80
		
		# x,y coordinates of the top left corner
		self.x_topleft = random.randrange(canvas_width)
		self.y_topleft = random.randrange(canvas_height)
		
		# width of the rectangular region
		self.rec_width = 0
		if self.x_topleft > canvas_width - self.max_width:
			range = canvas_width - self.x_topleft
			self.rec_width = random.randrange(range)
		else:
			self.rec_width = random.randrange(self.max_width)
		
		# height of the rectangular region
		self.rec_height = 0 
		if self.y_topleft > canvas_height - self.max_height:
			range = canvas_height - self.y_topleft
			self.rec_height = random.randrange(range)
		else:
			self.rec_height = random.randrange(self.max_height)
		
	def get_coord(self):
		return (self.x_topleft, self.y_topleft, self.rec_width, self.rec_height)
		
	def __repr__(self):
		return 'RandRegion({0}, {1})'.format(self.canvas_width, self.canvas_height)
	
	def __str__(self):
		return "Rectangle | (x,y) coordinates: ({0},{1}), Width: {2}, Height: {3}".format(self.x_topleft, self.y_topleft, self.rec_width, self.rec_height)