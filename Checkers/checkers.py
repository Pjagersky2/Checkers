"""Module for displaying a GUI checkerboard."""
from tkinter import Canvas, Tk
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


class Checkers(Canvas):
    """Representation of a checkers game."""

    grid_size = 8

    def __init__(self, master: Tk, size: int = 800) -> None:
        """Create a new instance."""

        self.size = size

        super().__init__(master, width=self.size, height=self.size)

        self.bind("<Button-1>", self.left_click)

        self.squares = []
        for col in range(self.grid_size):
            for row in range(self.grid_size):
                square = Square(col, row)
                self.squares.append(square)

        Square.set_side_length(self.square_length)

        self.draw_board()

    @property
    def square_length(self) -> int:
        """Evaluate the length of a square."""

        return self.size // self.grid_size

    # def draw_piece(self, col: int, row: int, color: str) -> None:
    #     """Draw a piece on the canvas."""

    #     reduction_scalar = 0.9  # 90 percent
    #     offset_percent = (1 - reduction_scalar) / 2
    #     piece_offset = round(self.square_length * offset_percent)
    #     reduce_length = self.square_length * reduction_scalar

    #     # Top-left corner
    #     top_left_x = (col * self.square_length) + piece_offset
    #     top_left_y = (row * self.square_length) + piece_offset

    #     # Bottom-right corner
    #     bot_right_x = top_left_x + reduce_length
    #     bot_right_y = top_left_y + reduce_length

    #     self.create_oval(top_left_x,
    #                      top_left_y,
    #                      bot_right_x,
    #                      bot_right_y,
    #                      fill=color)

    def draw_squares(self) -> None:
        """Draw the squares."""

        for square in self.squares:
            square.draw(self)

    def draw_board(self) -> None:
        """Draw the entire checkerboard."""

        self.draw_squares()

        # # Temporary code
        # for col in range(self.grid_size):
        #     for row in range(self.grid_size):
        #         color_index = (row + col) % 2
        #         color_key = "dark" if color_index else "light"

        #         if color_key == "dark":
        #             piece_color = None

        #             if row < 3:
        #                 piece_color = "black"
        #             elif row >= 5:
        #                 piece_color = "red"

        #             if piece_color:
        #                 self.draw_piece(col, row, piece_color)

    def find_square(self, col: int, row: int) -> Square:
        """Find a square based on position."""

        found = None
        for square in self.squares:
            if square.is_square(col, row):
                found = square
                break
        else:
            raise Exception(f"Square not found for position: {col}, {row}")

        return found

    def reset_squares(self) -> None:
        """Reset all the squares to original properties."""

        for square in self.squares:
            square.reset()

    def left_click(self, event) -> None:
        """Left-click event handler."""

        col = event.x // self.square_length
        row = event.y // self.square_length

        # Change color.
        square = self.find_square(col, row)
        print(square)

        square.color = "blue"
        self.draw_board()
        self.reset_squares()


def main() -> None:
    """Run the main function."""

    size = 800

    window = Tk()
    window.title("Checkers")
    window.geometry(f"{size}x{size}")

    checkers = Checkers(window, size=size)
    checkers.pack()

    window.mainloop()


if __name__ == "__main__":
    main()
