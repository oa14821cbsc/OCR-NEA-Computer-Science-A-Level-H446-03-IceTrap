class GameSceneManager:
    def __init__(self, scene):
        self.current_scene = scene
        self.previous_scene = None
        self.quit = False

    def get_scene(self):
        return self.current_scene
    
    def get_previous_scene(self):
        return self.previous_scene
    
    def set_state(self, scene):
        self.previous_scene = self.current_scene
        self.current_scene = scene
        
    def exit_game(self):
        self.quit = True