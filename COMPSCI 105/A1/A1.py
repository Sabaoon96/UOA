"""
Name: Sabaoon Raza Khan
UPI: skha787
ID: 983957824
Description: The program contains a canvas which allows users to add/remove shapes, such as rectangles, circles, & arcs.
"""

from tkinter import *
from RandRegion import RandRegion
from Stack import Stack
from Queue import Queue
import random

class A1: 
	def __init__(self, master):
		self.canvas_width = 700
		self.canvas_height = 400
		# Canvas Window Title
		master.title("A1 – skha787") 
		geometry_string = str(self.canvas_width)+"x"+str(self.canvas_height)+"+10+20"
		master.geometry(geometry_string)
		self.a_canvas = Canvas(root)
		self.a_canvas.config(background="SlateBlue1")	
		self.a_canvas.pack(fill=BOTH, expand = True) 
		
		# Button1 - Add rectangle
		button1 = Button(master, text = "Add Rect", command = self.add_rect)
		button1.pack(side = LEFT)
		# Button2 - Remove rectangle
		button2 = Button(master, text = "Remove Rect", command = self.remove_rect)
		button2.pack(side = LEFT)
		# Button3 - Add circle
		button1 = Button(master, text = "Add Circle", command = self.add_circle)
		button1.pack(side = LEFT)
		# Button4 - Remove circle
		button2 = Button(master, text = "Remove Circle", command = self.remove_circle)
		button2.pack(side = LEFT)
		# Button5 - Add arc
		button1 = Button(master, text = "Add Arc", command = self.add_arc)
		button1.pack(side = LEFT)
		# Button6 - Remove arc
		button1 = Button(master, text = "Remove Arc", command = self.remove_arc)
		button1.pack(side = LEFT)
		# Button7 - Remove red shapes
		button2 = Button(master, text = "Remove Red Shapes", command = self.remove_red)
		button2.pack(side = LEFT)
		
		# Colours Queue 1 (For rectangles)
		colours = ["red", "orange", "yellow", "green", "blue", "purple"]
		self.color_q1 = Queue()
		for item in colours:
			self.color_q1.enqueue(item)
			
		# Colours Queue 2 (For circles)
		colours = ["red", "orange", "yellow", "green", "blue", "purple"]
		self.color_q2 = Queue()
		for item in colours:
			self.color_q2.enqueue(item)
			
		# Colours Queue 3 (For arcs)
		colours = ["red", "orange", "yellow", "green", "blue", "purple"]
		self.color_q3 = Queue()
		for item in colours:
			self.color_q3.enqueue(item)
			
		# Tags Queue 1 (For rectangles)
		tags = ["red_to_remove", "other", "other", "other", "other", "other"]
		self.tag_q1 = Queue()
		for some_tag in tags:
			self.tag_q1.enqueue(some_tag)
			
		# Tags Queue 2 (For circles)
		tags = ["red_to_remove", "other", "other", "other", "other", "other"]
		self.tag_q2 = Queue()
		for some_tag in tags:
			self.tag_q2.enqueue(some_tag)
			
		# Tags Queue 3 (For arcs)
		tags = ["red_to_remove", "other", "other", "other", "other", "other"]
		self.tag_q3 = Queue()
		for some_tag in tags:
			self.tag_q3.enqueue(some_tag)
			
		# Rectangles List
		self.list = []
		
		# Circles Stack
		self.s = Stack()
		
		# Arcs Queue
		self.arcs_q = Queue()
		
	def add_rect(self):
		r = RandRegion(self.canvas_width, self.canvas_height)
		x, y, width, height = r.get_coord()
		
		# Gets color to fill
		item = self.color_q1.dequeue()
		# Gets tag to assign
		some_tag = self.tag_q1.dequeue()
		# Creates rectangle
		rec = self.a_canvas.create_rectangle(x, y, x+width, y+height, fill=item, tags=some_tag)
		self.color_q1.enqueue(item)
		self.tag_q1.enqueue(some_tag)
		# Adds rectangle to list of rectangles
		self.list.append(rec)
					
	def remove_rect(self):
		try:
			rec = random.choice(self.list)
			self.a_canvas.delete(rec)
			self.list.remove(rec)
		except IndexError:
			pass
		
	def add_circle(self):
		r = RandRegion(self.canvas_width, self.canvas_height)
		x, y, width, height = r.get_coord()
		
		# Gets color to fill
		item = self.color_q2.dequeue()
		# Gets tag to assign
		some_tag = self.tag_q2.dequeue()
		# Creates circle 
		circle = self.a_canvas.create_oval(x, y, x+width, y+height, fill=item, tags=some_tag)
		self.color_q2.enqueue(item)
		self.tag_q2.enqueue(some_tag)
		# Adds circle to stack of circles
		self.s.push(circle)
		
	def remove_circle(self):
		try:
			self.a_canvas.delete(self.s.pop())
		except IndexError:
			pass
		
	def add_arc(self):
		r = RandRegion(self.canvas_width, self.canvas_height)
		x, y, width, height = r.get_coord()
		
		# Gets color to fill
		item = self.color_q3.dequeue()
		# Gets tag to assign
		some_tag = self.tag_q3.dequeue()
		# Creates arc
		arc = self.a_canvas.create_arc(x, y, x+width, y+height, start=45, extent=90, fill=item, tags=some_tag)
		self.color_q3.enqueue(item)
		self.tag_q3.enqueue(some_tag)
		# Adds arc to queue of arcs
		self.arcs_q.enqueue(arc)
		
	def remove_arc(self):
		try:
			self.a_canvas.delete(self.arcs_q.dequeue())
		except IndexError:
			pass
		
	def remove_red(self):
		# Removes all red shapes using 'tag' assigned
		self.a_canvas.delete("red_to_remove")
	
	
root = Tk()
app = A1(root)
root.mainloop()

