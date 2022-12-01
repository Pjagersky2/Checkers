"""Module for a GUI piece in checkers."""
from tkinter import Canvas
from typing import Tuple


class Piece:
    """Representation of a piece on a checkers game."""

    side_length = -1

    @classmethod
    def set_side_length(cls, length: int) -> None:
        """Set the side length for all piece instances."""

        cls.side_length = length

    def __init__(self, col: int, row: int, color: str) -> None:
        """Create a new instance."""

        self.col = col
        self.row = row
        self.color = color

    def __str__(self) -> str:
        """String logic."""

        return f"Piece(col: {self.col}, row: {self.row}, color: {self.color})"

    @property
    def coords(self) -> Tuple[int, int, int, int]:
        """Coordinates of the piece."""

        reduction_scalar = 0.9  # 90 percent
        offset_percent = (1 - reduction_scalar) / 2
        piece_offset = round(self.side_length * offset_percent)
        reduce_length = self.side_length * reduction_scalar

        # Top-left corner
        top_left_x = (self.col * self.side_length) + piece_offset
        top_left_y = (self.row * self.side_length) + piece_offset

        # Bottom-right corner
        bot_right_x = top_left_x + reduce_length
        bot_right_y = top_left_y + reduce_length

        return (top_left_x, top_left_y, bot_right_x, bot_right_y)

    def draw(self, canvas: Canvas) -> None:
        """Draw the piece to the canvas."""

        canvas.create_oval(*self.coords, fill=self.color)

    def is_piece(self, col: int, row: int) -> bool:
        """Check if the position of the piece."""

        result = False
        if self.col == col and self.row == row:
            result = True

        return result

    def move_pieve(self) -> None:
        """Move the piece."""

        # Move coordinates
        self.draw()
