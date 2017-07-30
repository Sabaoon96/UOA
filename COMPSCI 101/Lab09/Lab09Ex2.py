from tkinter import * 
 
def draw_pattern_in_canvas(a_canvas): 
	grid_size = 50
	# You complete this function
	circle_colour = "red"
	square_colour = "green"
	outline_thickness = 2
	outline_colour = "black"
	
	y = 0
	for row in range(0,7):
		x = 0
		fill_in = row % 2 == 0
		for column in range(0,10):
			if fill_in:
				a_canvas.create_oval(x, y, x+grid_size, y+grid_size, fill = circle_colour, outline = outline_colour, width = outline_thickness)
			else:
				a_canvas.create_rectangle(x, y, x+grid_size, y+grid_size, fill = square_colour, outline = outline_colour, width = outline_thickness)
				a_canvas.create_line(x+(grid_size/2), y, x+(grid_size/2), y+grid_size, fill = outline_colour)
				a_canvas.create_line(x, y+(grid_size/2), x+grid_size, y+(grid_size/2), fill = outline_colour)
			x = x + grid_size
			fill_in = not fill_in
		y = y + grid_size
	
def draw_grid(a_canvas):
	for row in range(50, 350, 50):
		a_canvas.create_line(-1, row, 501, row, fill = "lightblue")
	for column in range(50, 500, 50):
		a_canvas.create_line(column, -1, column, 351, fill = "lightblue")
		
def main(): 
	window = Tk()  
	window.title("Red and Green Pattern")  
	window.config(background = 'white')   
	window.geometry("500x350+10+20") 

	a_canvas = Canvas(window) 
	a_canvas.config(background = "white")   
	a_canvas.pack(fill = BOTH, expand = True) #Canvas fills the whole top level window 
	draw_grid(a_canvas)
	draw_pattern_in_canvas(a_canvas) 
	window.mainloop()   
 
main()