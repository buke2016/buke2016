import numpy as np

# Define the transition matrix
P = np.array([[0.7, 0.3],
              [0.4, 0.6]])

# Define the initial state distribution
pi_0 = np.array([0.5, 0.5])

# Simulate the Markov chain
n_steps = 10
state = np.zeros(n_steps, dtype=int)
state[0] = np.random.choice([0, 1], p=pi_0)
for t in range(1, n_steps):
    state[t] = np.random.choice([0, 1], p=P[state[t-1]])

print(state)