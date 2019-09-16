#!/usr/bin/env python
# Four spaces as indentation [no tabs]
import math, copy, random, logging, qvalue
from common import *
from util import *
from state import *
import numpy

class Agent:

    def __init__(self):
        self.env = None
        self.metric_history = list()

    
    ################-------------------###################

    def reset(self, env):
        self.state = env.init

    def train(self, env):
        pass

    def reset(self, game):
        self.env = None

    def get_action(self, state):
        raise "Not implemented"

    def argmax_action(self, state):
        pass

    def make_state(self, env):
        return (env.state[0], env.state[1])

    def run(self, env):
        """
        Execute actions with actual policy.
        """
        self.action = self.getAction(self.make_state(env))
        self.state, self.reward = env.execute(self.action)
        return self.action, self.state
