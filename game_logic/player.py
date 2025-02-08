from abc import ABC, abstractmethod

class Player(ABC):
    @abstractmethod
    def make_move(self):
        pass
    
    @abstractmethod
    def get_player_color(self):
        pass