"""
Name: Sabaoon Raza Khan
UPI: skha787
ID: 983957824
Description: Program which produces a tessellation using five different tile shapes.
"""

from tkinter import *

# ------Draws one of the five different tiles.------
def draw_tile(a_canvas, tile_type, left, top, size):
	colours = ["yellow", "green", "blue", "deep sky blue", "purple", "red", "orange", "cyan"]
	colour_fill = colours[tile_type]
	outline_colour = "grey"
	line_width = 2
	if tile_type == 1:
		a_canvas.create_rectangle(left, top, left+size, top+(2*size), fill = colours[tile_type], outline = outline_colour, width = line_width)
		a_canvas.create_rectangle(left+size, top+size, left+(2*size), top+(3*size), fill = colours[tile_type], outline = outline_colour, width = line_width)
		a_canvas.create_rectangle(left+(2*size), top+(2*size), left+(3*size), top+(3*size), fill = colours[tile_type], outline = outline_colour, width = line_width)
		a_canvas.create_line(left+size, (top+size)+1, left+size, (top+(2*size))-1, fill = colours[tile_type], width = line_width)
		a_canvas.create_line(left+(2*size), (top+(2*size))+1, left+(2*size), (top+(3*size))-1, fill = colours[tile_type], width = line_width)
	if tile_type == 2:
		a_canvas.create_rectangle(left, top, left+(2*size), top+size, fill = colours[tile_type], outline = outline_colour, width = line_width)
		a_canvas.create_rectangle(left+size, top+size, left+(3*size), top+(2*size), fill = colours[tile_type], outline = outline_colour, width = line_width)
		a_canvas.create_rectangle(left+(2*size), top+(2*size), left+(3*size), top+(3*size), fill = colours[tile_type], outline = outline_colour, width = line_width)
		a_canvas.create_line((left+size)+1, top+size, (left+(2*size))-1, top+size, fill = colours[tile_type], width = line_width)
		a_canvas.create_line((left+(2*size))+1, top+(2*size), (left+(3*size))-1, top+(2*size), fill = colours[tile_type], width = line_width)
	if tile_type == 3:
		a_canvas.create_rectangle(left, top, left+size, top+(2*size), fill = colours[tile_type], outline = outline_colour, width = line_width)
		a_canvas.create_rectangle(left, top+size, left-size, top+(3*size), fill = colours[tile_type], outline = outline_colour, width = line_width)
		a_canvas.create_rectangle(left-(2*size), top+(2*size), left-size, top+(3*size), fill = colours[tile_type], outline = outline_colour, width = line_width)
		a_canvas.create_line(left, (top+size)+1, left, (top+(2*size))-1, fill = colours[tile_type], width = line_width)
		a_canvas.create_line(left-size, (top+(2*size))+1, left-size, (top+(3*size))-1, fill = colours[tile_type], width = line_width)
	if tile_type == 4:
		a_canvas.create_rectangle(left, top, left+(2*size), top+size, fill = colours[tile_type], outline = outline_colour, width = line_width)
		a_canvas.create_rectangle(left-size, top+size, left+size, top+(2*size), fill = colours[tile_type], outline = outline_colour, width = line_width)
		a_canvas.create_rectangle(left-size, top+(2*size), left, top+(3*size), fill = colours[tile_type], outline = outline_colour, width = line_width)
		a_canvas.create_line(left+1, top+size, (left+size)-1, top+size, fill = colours[tile_type], width = line_width)
		a_canvas.create_line((left-size)+1, (top+(2*size)), left-1, (top+(2*size)), fill = colours[tile_type], width = line_width)
	if tile_type == 5:
		a_canvas.create_rectangle(left, top, left+size, top+size, fill = colours[tile_type], outline = outline_colour, width = line_width)

# ------Process each symbol from a single line (string). ------
def process_single_line(a_canvas, line_of_pattern, left, top, size):
	for character in line_of_pattern:
		if character == "1":
			draw_tile(a_canvas, 1, left, top, size)
		elif character == "2":
			draw_tile(a_canvas, 2, left, top, size)
		elif character == "3":
			draw_tile(a_canvas, 3, left, top, size)
		elif character == "4":
			draw_tile(a_canvas, 4, left, top, size)
		elif character == "5":
			draw_tile(a_canvas, 5, left, top, size)
		left += size

# ------Organise the processing of the pattern. ------
def process_pattern(a_canvas, size):
	left = size
	top = size
	list_of_lines = get_list_of_pattern_lines("TileMap.txt")
	for line_string in list_of_lines:
		process_single_line(a_canvas, line_string, left, top, size)
		top += size

# ------Get the list of lines (strings) from the file. ------
def get_list_of_pattern_lines(filename):
	file_to_read = open(filename, "r")
	file_info = file_to_read.read()
	lines_list = file_info.split("\n")
	file_to_read.close()
	return lines_list

# ------Draws the five tiles on the right side of the canvas. ------
def draw_five_tiles(a_canvas, left, top, size):
	size = size * 3 // 4
	large_rect = (left, top, left + size * 11, top + size * 12)
	a_canvas.create_rectangle(large_rect, fill="Blue4", outline="SlateBlue1", width = 2)
	left_size_multiply = [0, 1, 6, 3, 7, 1]
	down_size_multiply = [0, 1, 1, 6, 6, 10]

	for tile_type in range(1, 6):
		left_value = left + size * left_size_multiply[tile_type]
		top_value = top + size * down_size_multiply[tile_type]
		draw_tile(a_canvas, tile_type, left_value, top_value, size)

# ------Draws the blue background grid lines of the given size. ------
def draw_grid(a_canvas, size, right_hand_side, bottom):
	for row in range(size, bottom, size):
		a_canvas.create_line(-1, row, right_hand_side + 1, row, fill="SlateBlue1")
	for col in range(size, right_hand_side, size):
		a_canvas.create_line(col, -1, col, bottom + 1, fill="SlateBlue1")

# ------main function. ------
def main():
	size = 20
	canvas_width = 700
	canvas_height = 340
	root = Tk()
	root.title("A5 - skha787")
	geometry_string = str(canvas_width)+"x"+str(canvas_height)+"+10+20"
	root.geometry(geometry_string)
	a_canvas = Canvas(root)

	a_canvas.config(background="SlateBlue1") #Uncomment when you have finished
	a_canvas.pack(fill=BOTH, expand = True) #Canvas fills the whole window
	#Draw the light blue background grid lines
	draw_grid(a_canvas, size, canvas_width, canvas_height)

	process_pattern(a_canvas, size)
	draw_five_tiles(a_canvas, canvas_width - size * 3 // 4 * 12, size, size)
	
	root.mainloop()
	
main()