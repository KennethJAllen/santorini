"""Defines the Worker and Player classes."""
from __future__ import annotations
import pygame

from .config import SQUARE_SIZE, PADDING, BORDER

class Worker:
    """Worker class to represent a player's worker on the board."""

    def __init__(self, worker_id: int = None, player: Player = None):
        """
        Initializes a new worker with a player, an identifier, and an initial position on the board.
        Default values represent no worker.
        
        player: The player who owns this worker.
        worker_id: An identifier to distinguish between a player's workers (e.g., 1 or 2).
        position: The position that the worker is on.
        gender: Relevant for god cards. Not currently used.
        """
        self._worker_id = worker_id
        self._player = player
        self._position = None
        self._valid_moves = None

    def __bool__(self):
        return bool(self._player or self._worker_id)

    def __eq__(self, other):
        if not isinstance(other, Worker):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self._player is other._player and self._worker_id == other._worker_id

    def display(self) -> None:
        """Displayers the worker info."""
        if self:
            return f"{self._player.player_id}_{self._worker_id}"
        return ""

    def get_worker_id(self) -> int:
        """Returns the worker id."""
        return self._worker_id

    def get_player(self) -> Player:
        """Returns the player that the worker belongs to."""
        return self._player

    def set_positon(self, position: tuple[int,int]) -> None:
        """Set the worker position."""
        self._position = position

    def get_position(self) -> tuple[int,int]:
        """Get the worker position."""
        return self._position

    def set_valid_moves(self, valid_moves: set[tuple[int,int]]) -> None:
        """Set the worker position."""
        self._position = valid_moves

    def get_valid_moves(self) -> set[tuple[int,int]]:
        """Get the valid moves for this worker."""
        return self._valid_moves

    # display

    def get_display_position(self) -> tuple[int,int]:
        """Returns the center of the square corresponding to the worker on the display board."""
        x, y = self._position
        x_display = SQUARE_SIZE * x + SQUARE_SIZE // 2
        y_display = SQUARE_SIZE * y + SQUARE_SIZE // 2
        return x_display, y_display

    def draw(self, screen):
        """Display the piece on the screen."""
        player_color = self._player.get_color()
        radius = SQUARE_SIZE // 2 - PADDING
        # draw outline
        pygame.draw.circle(screen, player_color, self.get_display_position(), radius + BORDER)
        # draw piece
        pygame.draw.circle(screen, player_color, self.get_display_position(), radius)

class Player:
    """Player class to manage player actions and workers."""

    def __init__(self, player_id: int = None, workers: dict[int, Worker] = None):
        self.player_id = player_id
        self._color = (128, 128, 128)
        if workers is None:
            self._workers = {}
        else:
            self._workers = workers

    def __bool__(self):
        return bool(self.player_id)

    def add_worker(self, worker: Worker):
        """Adds a worker to the workers dictionary.
        Key (int): worker id, value: worker."""
        worker_id = worker.get_worker_id()
        self._workers[worker_id] = worker

    def get_worker(self, worker_id):
        """Returns the player's worker with the assosiated worker id."""
        return self._workers[worker_id]

    def get_workers(self) -> dict[int, Worker]:
        """Get the dictionary of workers.
        Key (int): worker id, value: worker."""
        return self._workers

    def get_color(self) -> tuple[int,int,int]:
        """Returns the RGB color corresponding to the player."""
        return self._color
