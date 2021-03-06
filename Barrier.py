from typing import List
import pygame, Actor

class Barrier(Actor):
    """
       A single sprite immobile wall that prevents movement throught it.
       """

    def __init__(self, start_xpos: float, start_ypos: float, width: float, height: float, sprites):
        super().__init__(start_xpos, start_ypos, width, height, 0, sprites)

    # Overrides the Super class Actor's move methods below, since the Barriers cannot move.
    
    def move_left(self) -> None:
        return None

    def move_right(self) -> None:
        return None

    def move_up(self) -> None:
        return None

    def move_down(self) -> None:
        return None
