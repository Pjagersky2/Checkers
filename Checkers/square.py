"""Module for a GUI checkerboard square."""
from tkinter import Canvas
from typing import Tuple


class Square:
    """Representation of a square on a checkers game."""

    side_length = -1
    colors = {
        "dark": "#a77d5c",
        "light": "#e8cfaa"
    }

    @classmethod
    def set_side_length(cls, length: int) -> None:
        """Set the side length for all square instances."""

        cls.side_length = length

    def __init__(self, col: int, row: int) -> None:
        """Create a new instance."""

        self.col = col
        self.row = row
        self.color = self.get_color()

    def __str__(self) -> str:
        """String logic."""

        return f"Square(col: {self.col}, row: {self.row}, color: {self.color})"

    @property
    def coords(self) -> Tuple[int, int, int, int]:
        """Coordinates of the square."""

        top_left_x = self.col * self.side_length
        top_left_y = self.row * self.side_length

        bot_right_x = top_left_x + self.side_length
        bot_right_y = top_left_y + self.side_length

        return (top_left_x, top_left_y, bot_right_x, bot_right_y)

    def get_color(self) -> str:
        """Evaluate the color."""

        color_index = (self.row + self.col) % 2
        color_key = "dark" if color_index else "light"
        color = self.colors[color_key]

        return color

    def draw(self, canvas: Canvas) -> None:
        """Draw the square to the canvas."""

        canvas.create_rectangle(*self.coords, fill=self.color)

    def is_square(self, col: int, row: int) -> bool:
        """Check if position is the square."""

        result = False
        if self.col == col and self.row == row:
            result = True

        return result

    def reset(self) -> None:
        """Reset to original square properties."""

        self.color = self.get_color()
