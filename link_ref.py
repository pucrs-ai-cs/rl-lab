#!/usr/bin/env python
# Four spaces as indentation [no tabs]
# Standard Q-Learning implementation.
import math, copy, random, logging
from qvalue import *
from common import *
from util import *
from agent import *

class Link(Agent):

    def __init__(self):

        Agent.__init__(self)
        self.q_values = dict()
        self.frequency = dict()
        self.state = None
        self.reward = None
        self.action = NO_OP
        self.p_state = None 
        self.p_reward = None
        self.p_action = None
        self.gamma = 0.9
        self.r_plus = 50
        self.exploration = 1
        self.env = None
        self.prev_qtable = dict()

    def reset(self, env):
        """
        Reset the state to the initial environment state
        """
        self.state = env.init

    def train(self, env):
        """
        Execute MAX_TRAINING_EPISODES rounds or until converge.
        """
        print('It will converge at', CONVERGENCE_THRESHOLD)

        self.reset(env)
        self.env = env

        executions = 0
        last_plan = []
        while executions < MAX_TRAINING_EPISODES:
            self.state = self.make_state(env)
            action = self.get_action(self.state)
            last_plan.append(action)
            self.env.execute(action)
            if env.terminal((self.state.x, self.state.y)):
                executions += 1
                
                self.p_state = self.p_action = self.p_reward = self.state = self.action = self.reward = None
                self.reset(env)

                if self.converged():
                    break
                else:
                    last_plan = []
                    self.prev_qtable = copy.deepcopy(self.q_values)

                #print('Episode', executions, ': convergence %', self.convergence)

        print('Episode' , executions, ' : converged at', self.convergence)
        print('Last plan executed: ', [ACTIONS_NAMES[x] for x in last_plan])
        #self.return_policy()

    def alpha(self, qv):
        #YOUR IMPLEMENTATION HERE
        return alpha(self,qv)

    def f(self, qv):
        #YOUR IMPLEMENTATION HERE
        return f(self,qv)

    def get_action(self, state):
        #YOUR IMPLEMENTATION HERE
        return get_action(self,state)   

    def max_a(self, state):
        """
        Standard max action implementation java style.
        Return the max value you can obtain in a certain state.
        """
        max_value = float('-inf')
        if self.env.terminal((state.x, state.y)):
            max_value = self.q_values[qvalue.QValue(state, NO_OP)]
        else:
            for action in self.env.available_actions((state.x, state.y)):
                qv = qvalue.QValue(state, action)
                if qv in self.q_values:
                    q_sa = self.q_values[qv]
                    if q_sa > max_value:
                        max_value = q_sa
        if max_value == float('-inf'): 
            max_value = 0.0
        return max_value

    def argmax_a(self, state):
        """
        Standard argmax action implementation java style.
        Return the best action you can perform in a certain state.
        """
        a = NO_OP
        max_value = float('-inf')
        if state == None:
            return a
        for action in self.env.available_actions((state.x, state.y)):
            qv = qvalue.QValue(state, action)
            fvalue = self.f(qv)
            if fvalue > max_value:
                max_value = fvalue
                a = action
        return a

    def make_state(self, env):
        """
        Build state using position and rupees.
        """
        return State(env.state[0], env.state[1], env.rupees)

    def return_qvalue(self, qvalue):
        if qvalue in self.q_values:
            return self.q_values[qvalue]
        return 0

    def converged(self):
        """
        Return True if the change between previous util table and current util table
        are smaller than the convergence_threshold.
        """
        self.convergence = self.convergence_metric()
        return self.convergence < CONVERGENCE_THRESHOLD

    def run(self, env):
        """
        Execute actions.
        """
        self.action = self.argmax_a(self.make_state(env))
        #print "Running action: ", ACTIONS_NAMES[self.action]
        self.state, self.reward = env.execute(self.action)
        return self.action, self.state


    def convergence_metric(self):
        """
        Return the convergence metric.
        """
        prev = sum(self.prev_qtable.values())
        curr = sum(self.q_values.values())
        return math.sqrt(abs(curr - prev))



