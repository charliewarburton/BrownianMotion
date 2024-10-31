# gbm_simulator.py
import numpy as np

# Base class
class gbm_simulator:
    # Initialises class so we can use these self. attributes later
    def __init__(self, y0, mu, sigma):
        self.y0 = y0
        self.mu = mu
        self.sigma = sigma

# Daughter Class
class GBMSimulator(gbm_simulator):
    def __init__(self, y0, mu, sigma):
        super().__init__(y0, mu, sigma)


    def simulate_path(self, T, N):
        # Initialises class so we can use these self. attributes later
        self.T = T
        self.N = N

        # Setting seed for reproducibility
        np.random.seed(0)

        # Time step
        dt = T/N

        # Time grid
        t = np.linspace(0, T, N+1)

        # Brownian increments
        dW = np.sqrt(dt)*np.random.randn(N)

        # Initialise path
        y = np.zeros(N+1)
        y[0] = self.y0

        # Generate path
        for i in range(1, N+1):
            y[i] = y[i-1] + self.mu*y[i-1]*dt + self.sigma*y[i-1]*dW[i-1]

        return t, y


