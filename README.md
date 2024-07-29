# Pattern Drawer

This Python program is designed to draw patterns on a canvas using a dictionary of colors. The program includes functions to process input lines, create a color dictionary, and draw patterns on a canvas.

## Functions

### `create_colour_dictionary(colours_list)`

This function takes a list of colors and creates a dictionary where the key is the first letter of the color and the value is the color name.

**Parameters:**
- `colours_list` (list): A list of color strings.

**Returns:**
- `dict`: A dictionary with the first letter of the color as the key and the color name as the value.

### `draw_pattern(a_canvas, colour_dictionary, pattern_list, size, start_x, start_y)`

This function draws a pattern on a given canvas using the provided color dictionary and pattern list.

**Parameters:**
- `a_canvas` (Canvas): The canvas on which to draw the pattern.
- `colour_dictionary` (dict): A dictionary mapping color codes to color names.
- `pattern_list` (list): A list of lists representing the pattern to draw.
- `size` (int): The size of each rectangle in the pattern.
- `start_x` (int): The starting x-coordinate for the pattern.
- `start_y` (int): The starting y-coordinate for the pattern.

## Usage

1. **Create a Color Dictionary:**
   ```python
   colours_list = ["RRed", "GGreen", "BBlue"]
   colour_dictionary = create_colour_dictionary(colours_list)


2. **Draw a Pattern:**
pattern_list = [
    ["R", "G", "B"],
    ["G", "B", "R"],
    ["B", "R", "G"]
]
draw_pattern(a_canvas, colour_dictionary, pattern_list, 20, 0, 0)


** Example:

from tkinter import Canvas, Tk

# Initialize the Tkinter window and canvas
root = Tk()
a_canvas = Canvas(root, width=200, height=200)
a_canvas.pack()

# Define the color list and pattern
colours_list = ["RRed", "GGreen", "BBlue"]
pattern_list = [
    ["R", "G", "B"],
    ["G", "B", "R"],
    ["B", "R", "G"]
]

# Create the color dictionary
colour_dictionary = create_colour_dictionary(colours_list)

# Draw the pattern on the canvas
draw_pattern(a_canvas, colour_dictionary, pattern_list, 20, 0, 0)

# Run the Tkinter main loop
root.mainloop()

## Requirements
Python 3.x
Tkinter library