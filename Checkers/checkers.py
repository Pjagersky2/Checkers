"""Module for displaying a GUI checkerboard."""
from tkinter import Canvas, Tk


class Checkers(Canvas):
    """Representation of a checkers game."""

    size = 800
    grid_size = 8
    colors = {
        "dark": "#a77d5c",
        "light": "#e8cfaa"
    }

    def __init__(self, master: Tk) -> None:
        """Create a new instance."""

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

        print((top_left_x, top_left_y), (bot_right_x, bot_right_y), piece_offset, reduce_length)
        if top_left_x == 0.0:
            color = "blue"

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

        print("left click", event.x, event.y)


def main() -> None:
    """Run the main function."""

    window = Tk()
    window.title("Checkers")
    checkers = Checkers(window)
    checkers.pack()
    window.mainloop()


if __name__ == "__main__":
    main()
