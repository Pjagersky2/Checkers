"""Module for displaying a GUI checkerboard."""
import logging
from tkinter import Canvas, Tk
from typing import List

from checkers.square import Square
from checkers.piece import Piece

logger = logging.getLogger(__name__)


class Checkers(Canvas):
    """Representation of a checkers game."""

    grid_size = 8

    def __init__(self, master: Tk, size: int = 800) -> None:
        """Create a new instance."""

        self.size = size

        super().__init__(master, width=self.size, height=self.size)

        self.bind("<Button-1>", self.left_click)

        self.squares = self.init_squares()
        self.pieces = self.init_pieces()

        Square.set_side_length(self.square_length)
        Piece.set_side_length(self.square_length)

        self.draw_board()

    @property
    def square_length(self) -> int:
        """Evaluate the length of a square."""

        return self.size // self.grid_size

    def draw_squares(self) -> None:
        """Draw the squares."""

        for square in self.squares:
            square.draw(self)

    def draw_pieces(self) -> None:
        """Draw the pieces."""

        for piece in self.pieces:
            piece.draw(self)

    def draw_board(self) -> None:
        """Draw the entire checkerboard."""

        self.draw_squares()
        self.draw_pieces()

    def find_square(self, col: int, row: int) -> Square:
        """Find the square based on position."""

        found = None
        for square in self.squares:
            if square.is_square(col, row):
                found = square
                break
        else:
            raise Exception(f"Square not found for position: {col}, {row}")

        return found

    def find_piece(self, col: int, row: int) -> Square:
        """Find the piece based on position."""

        found = None
        for piece in self.pieces:
            if piece.is_piece(col, row):
                found = piece
                break

        return found

    def reset_squares(self) -> None:
        """Reset all the squares to original properties."""

        for square in self.squares:
            square.reset()

    def left_click(self, event) -> None:
        """Left-click event handler."""

        col = event.x // self.square_length
        row = event.y // self.square_length

        square = self.find_square(col, row)
        logger.info(square)

        piece = self.find_piece(col, row)
        if piece:
            logger.info(piece)
            square.color = "yellow"

        self.draw_board()
        self.reset_squares()

    @staticmethod
    def init_squares() -> List[Square]:
        """Initialize the board squares."""

        squares = []
        for col in range(Checkers.grid_size):
            for row in range(Checkers.grid_size):
                square = Square(col, row)
                squares.append(square)

        return squares

    @staticmethod
    def init_pieces() -> List[Piece]:
        """Initialize the board pieces."""

        pieces = []
        for col in range(Checkers.grid_size):
            for row in range(Checkers.grid_size):
                if (row + col) % 2:
                    color = None

                    if row < 3:
                        color = "#000000"
                    elif row >= 5:
                        color = "#ff0000"

                    if color:
                        piece = Piece(col, row, color)
                        pieces.append(piece)

        return pieces
