"""Module for displaying a GUI checkerboard."""
import tkinter as tk

window = tk.Tk()

size = 800
grid_size = 8

canvas = tk.Canvas(window, width=size, height=size, bg="blue")


def draw_square(x, y, color):

    rect_size = size // grid_size

    x1 = x * rect_size
    y1 = y * rect_size
    x2 = x1 + rect_size
    y2 = y1 + rect_size

    canvas.create_rectangle(x1, y1, x2, y2, fill=color)


colors = ("red", "black")
for col in range(grid_size):
    for row in range(grid_size):
        color_index = (row + col) % 2
        print(color_index)
        color = colors[color_index]
        draw_square(col, row, color)

canvas.pack()

window.mainloop()
