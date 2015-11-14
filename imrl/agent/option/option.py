"""Manages data structures and methods necessary to learn and execute options in MDPs.
An option consists of a policy, a universal option model (UOM), and a termination function."""

# Third party
import numpy as np

# First party
from imrl.agent.option.uom import UOM


class Option:

    def __init__(self, fa, policy, alpha, gamma):
        self.fa = fa
        self.policy = policy
        self.uom = UOM(fa, alpha, gamma)

    def get_next_fv(self, fv):
        """Get expected next feature vector given feature vector fv."""
        return np.dot(self.uom.m, fv)

    def get_return(self, r, fv):
        """Calculate the expected return for executing the option in the state corresponding to the feature vector fv
        given the reward function r."""
        return np.dot(r.T, np.dot(self.uom.u, fv))

    def is_terminal(self, fv):
        """Returns true if the option terminates in the given feature vector fv."""
        return True
