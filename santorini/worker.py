from santorini.player import Player

class Worker:
    """Worker class to represent a player's worker on the board."""

    def __init__(self, player: Player = None, worker_id: str = "", gender = "", initial_position: tuple[int, int] = (0, 0)):
        """
        Initializes a new worker with a player, an identifier, and an initial position on the board.
        Default values represent no worker.
        
        :param player: The player who owns this worker.
        :param worker_id: An identifier to distinguish between a player's workers (e.g., 'A' or 'B').
        :param initial_position: A tuple representing the worker's initial position on the board (row, col).
        """
        self.player = player
        self.worker_id = worker_id
        self._gender = gender
        self.position = initial_position

    def __bool__(self):
        return bool(self.player or self.worker_id)

    def __eq__(self, other):
        if not isinstance(other, Worker):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.player == other.player and self.worker_id == other.worker_id and self._gender == other._gender
