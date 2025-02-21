import gymnasium as gym
import configparser
import ale_py

config = configparser.ConfigParser()
config.read('Config.ini')

gym.register_envs(ale_py)
env = gym.make('ALE/Freeway-v5', render_mode="human")
env.reset()

score = 0
game_active = True

while game_active:
    action = env.action_space.sample()
    
    obs, reward, terminated, truncated, info = env.step(1)
    
    score += reward
    
    if score == 2:
        game_active = False

    if terminated or truncated:
        obs, info = env.reset()

env.close()