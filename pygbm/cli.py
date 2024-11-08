import argparse
import matplotlib.pyplot as plt
from .gbm_simulator import GBMSimulator

def main():
    parser = argparse.ArgumentParser(description='Simulate a Geometric Brownian Motion')
    parser.add_argument('--y0', type=float, default=100, help='Initial value')
    parser.add_argument('--mu', type=float, default=0.1, help='Drift')
    parser.add_argument('--sigma', type=float, default=0.2, help='Volatility')
    parser.add_argument('--T', type=float, default=1, help='Time horizon')
    parser.add_argument('--N', type=int, default=100, help='Number of time steps')
    parser.add_argument('--output', type=str, default='output.png', help='Output file name')


    args = parser.parse_args()

    simulator = GBMSimulator(args.y0, args.mu, args.sigma)
    t, y = simulator.simulate_path(args.T, args.N)
    plt.plot(t, y)
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.title('Geometric Brownian Motion')
    plt.savefig(args.output)

if __name__ == '__main__':
    main()