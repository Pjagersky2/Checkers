"""Module for displaying a GUI checkerboard."""
from tkinter import Canvas, Tk


class Checkers(Canvas):
    """Representation of a checkers game."""

    grid_size = 8
    colors = {
        "dark": "#a77d5c",
        "light": "#e8cfaa"
    }

    def __init__(self, master: Tk, size: int = 800) -> None:
        """Create a new instance."""

        self.size = size

        super().__init__(master, width=self.size, height=self.size)

        self.bind("<Button-1>", self.left_click)
        self.draw_board()

    @property
    def square_length(self) -> int:
        """Evaluate the length of a square."""

        return self.size // self.grid_size

    def draw_square(self, col: int, row: int, color: str) -> None:
        """Draw a square on the canvas."""

        # Top-left corner
        top_left_x = col * self.square_length
        top_left_y = row * self.square_length

        #  Bottom-right corner
        bot_right_x = top_left_x + self.square_length
        bot_right_y = top_left_y + self.square_length

        self.create_rectangle(top_left_x,
                              top_left_y,
                              bot_right_x,
                              bot_right_y,
                              fill=color)

    def draw_piece(self, col: int, row: int, color: str) -> None:
        """Draw a piece on the canvas."""

        reduction_scalar = 0.9  # 90 percent
        offset_percent = (1 - reduction_scalar) / 2
        piece_offset = round(self.square_length * offset_percent)
        reduce_length = self.square_length * reduction_scalar

        # Top-left corner
        top_left_x = (col * self.square_length) + piece_offset
        top_left_y = (row * self.square_length) + piece_offset

        # Bottom-right corner
        bot_right_x = top_left_x + reduce_length
        bot_right_y = top_left_y + reduce_length

        self.create_oval(top_left_x,
                         top_left_y,
                         bot_right_x,
                         bot_right_y,
                         fill=color)

    def draw_board(self) -> None:
        """Draw the entire checkerboard."""

        for col in range(self.grid_size):
            for row in range(self.grid_size):
                color_index = (row + col) % 2

                color_key = "dark" if color_index else "light"
                color = self.colors[color_key]

                self.draw_square(col, row, color)

                # Temporary code
                if color_key == "dark":
                    piece_color = None

                    if row < 3:
                        piece_color = "black"
                    elif row >= 5:
                        piece_color = "red"

                    if piece_color:
                        self.draw_piece(col, row, piece_color)

                # self.draw_piece(col, row, "black")

    def left_click(self, event) -> None:
        """Left-click event handler"""

        col = event.x // self.square_length
        row = event.y // self.square_length

        # (x, y) = event.x , event.y coordinates anywhere on canvas
        # (a, b) = square grid from 0 - 7
        # x and y have to be between 0 - 800
        # assuming x and y are a random point in cell (0, 0)

        # legal random point in cell (0, 0) -> (x, y) = (021, 25)
        # legal random point in cell (1, 0) -> (x, y) = (125, 25)
        # legal random point in cell (2, 0) -> (x, y) = (223, 25)

        # cell -> min    - max
        # 0    -> 0      - 100
        # 1    -> 100    - 200
        # 2    -> 200    - 300
        # given a minimum, to get a cell divide by square_size

        # print("left click", event.x, event.y)
        print((col, row), (event.x, event.y))


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
