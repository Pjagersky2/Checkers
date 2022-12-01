"""Module containing the game logic for checkers."""
import logging.config
from tkinter import Tk

from checkers.board import Checkers
from checkers.config import logger_config

logging.config.dictConfig(logger_config)


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
