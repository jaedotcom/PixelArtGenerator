"""
Aim: This program prompts the user to enter the name of a txt file that contains the list of keys for the color dictionary.
The program uses Tkinter and canvas in Python to draw and display pixel art.

Author: Jae Kim
"""
from tkinter import *

def get_lines_from_file(filename):
    new_list = []
    input_file = open(filename, 'r')
    contents = input_file.read()
    list_contents = contents.split("\n")
    for element in list_contents:
        new_list.append(element)
    input_file.close()
    
    return new_list
    
def create_pattern_list(lines):
    new_list = []
    for i in lines:
        str1=""
        new_list_2=[]
        new_list_2=list(i)
        new_list.append(new_list_2)
    return new_list

def create_colour_dictionary(colours_list):
    new_dict = {}
    for i in colours_list:
        front_letter = i[0]
        colour = i[2:]
        new_dict[front_letter] = colour
        
    return new_dict

def draw_pattern(a_canvas, colour_dictionary, pattern_list, size, start_x, start_y):
    y = start_y
    for row in pattern_list:
        x = start_x
        for column in range(len(row)):
            rectangle = (x, y, x + size, y + size)
            for i in row[column]:
                shade=colour_dictionary[i]
                a_canvas.create_rectangle(rectangle, fill=shade, outline="grey")
            x += size
        y += size
      

def main():
    size = 50
    start_x = size * 2
    start_y = size * 2
    name = input("Enter a name: ")
    palette_content = get_lines_from_file(name+"_palette.txt")
    colour_dictionary = create_colour_dictionary(palette_content)   
    pattern_content = get_lines_from_file(name+".txt")
    pattern_list = create_pattern_list(pattern_content)
    
    number_of_rows = len(pattern_list)	
    number_of_columns = len(pattern_list[0])
    canvas_width = size * number_of_columns +size * 4
    canvas_height = number_of_rows * size + size * 4
    window = Tk() 
    window.title("Tadah!") 
    geometry_string = str(canvas_width)+"x"+str(canvas_height)+"+10+20"
    window.geometry(geometry_string)
    a_canvas = Canvas(window)
    a_canvas.config(background="white")
    a_canvas.pack(fill=BOTH, expand = True)  
    draw_pattern(a_canvas, colour_dictionary, pattern_list, size, start_x, start_y)
    window.mainloop()


main()
