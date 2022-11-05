"""Module for displaying a GUI checkerboard."""
import tkinter as tk


class Checkers:
    """Representation of a checkers game."""

    size = 800
    grid_size = 8
    colors = {
        "dark": "#a77d5c",
        "light": "#e8cfaa"
    }

    def __init__(self, window: tk.Tk) -> None:
        """Create a new instance."""

        self.window = window
        self.canvas = None

    @property
    def square_length(self) -> int:
        """Evaluate the length of a square."""

        return self.size // self.grid_size

    def start(self) -> None:
        """Start the checkers game."""

        self.canvas = tk.Canvas(self.window,
                                width=self.size,
                                height=self.size)

        self.draw_board()

        self.canvas.pack()

    def draw_square(self, col: int, row: int, color: str) -> None:
        """Draw a square on the canvas."""

        # Top-left corner
        top_left_x = col * self.square_length
        top_left_y = row * self.square_length

        #  Bottom-right corner
        bot_right_x = top_left_x + self.square_length
        bot_right_y = top_left_y + self.square_length

        self.canvas.create_rectangle(top_left_x,
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


def main() -> None:
    """Run the main function."""

    window = tk.Tk()

    checkers = Checkers(window)
    checkers.start()

    window.mainloop()


if __name__ == "__main__":
    main()
