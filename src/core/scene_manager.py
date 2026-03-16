class GameSceneManager:
    def __init__(self, scene):
        self.current_scene = scene
        self.previous_scene = None
        self._exit_game = False

    def get_scene(self):
        return self.current_scene
    
    def get_previous_scene(self):
        return self.previous_scene
    
    def set_state(self, scene):
        self.previous_scene = self.current_scene
        self.current_scene = scene

    @property
    def exit_game(self):
        return self._exit_game

    @exit_game.setter
    def exit_game(self, value: bool):
        self._exit_game = value