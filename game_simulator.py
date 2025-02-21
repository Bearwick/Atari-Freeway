import gymnasium as gym
import configparser
import ale_py

class Game_Simulator():
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('Config.ini')
        
        r_mode = self.config.get('Config', 'render_mode')
        gym.register_envs(ale_py)
        self.env = gym.make('ALE/Freeway-v5', render_mode=r_mode)
        self.env.reset()

        self.score = 0
        self.game_active = True
    
    def push_action(self, action):
        obs, reward, terminated, truncated, info = self.env.step(action) 
        self.score += reward

        return obs, reward, self.score
    
    def terminate_game(self):
        self.env.close()


game = Game_Simulator()

score = 0

while score != 2:
    obs, reward, score = game.push_action(1)

game.terminate_game()
