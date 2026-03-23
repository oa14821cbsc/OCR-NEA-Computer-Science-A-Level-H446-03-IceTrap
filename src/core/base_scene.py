from abc import ABC, abstractmethod

class BaseScene(ABC):
    def __init__(self, display, game_scene_manager):
        self.display = display
        self.game_scene_manager = game_scene_manager
    
    @abstractmethod
    def run(self, events):
        raise NotImplementedError
    
    @abstractmethod
    def _draw(self):
        raise NotImplementedError
    
    @abstractmethod
    def _handle_events(self, events):
        raise NotImplementedError