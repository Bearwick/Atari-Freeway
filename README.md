# Atari-Freeway

This project is a test environment for implementing the Atari game Freeway using the Gymnasium interface. The gained knowledge is to be used in the course IT3105 AI Programming when creating a MuZero knockoff.

## Notes

- The game grid is not scalable.
- Default rewards is 1 when crossing road, else 0.
- env.step() is used for doing an action, and returns five actions:
  - **obs (observation):** is the current state of the environment after taking an action as a NumPy array. Used for decision-making in reinforcement learning.
  - **reward:** the reward after taking an action. +1 when crossing the road successfully. 0 if no progess made.
  - **terminated:** boolean that indicated if the game is over. For freeway, the game never ends unless stopped.
  - **truncated:** boolean that indicated if the episode ended due to a time limit. False Unless a wrapper enforces a time limit. True if a maximum step limit is applied.
  - **info:** a dictionary containing extra data about the environment. In freeway it can include frame number, score, or debugging info.

## Virtual Environment

### Create Virtual Environment

`python3 -m venv venv`

### Activate

`source venv/bin/activate`

### Deactivate

`deactivate`

### Export Dependencies

`pip freeze > requirements.txt`

### Install Dependecies

`pip install -r requirements.txt`
