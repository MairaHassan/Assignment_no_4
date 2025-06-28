# utils.py

import random

# Likelihood between 0 and 1 (e.g., 0.3 means 30% chance to stop)
DONE_LIKELIHOOD = 0.3

def done():
    return random.random() < DONE_LIKELIHOOD
