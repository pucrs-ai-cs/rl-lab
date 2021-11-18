# Reinforcement-Learning Practical

### Installation
To install pygame on PUCRS computers, use this command:
```
pip install pygame --user
```

### Source:
These are the files required to build your reinforcement learning algorithm. 

- [common.py](common.py) with constants
- [util.py](util.py) with util functions
- [game.py](game.py) with drawing calls
- [environment.py](environment.py) contains the scenario behavior
- [agent.py](agent.py) contains training components, such as environment interaction and previous state

### Assignment
The goal of this assignment is to implement the core of the Q-Learning algorithm. You will be responsible for implementing three distinct methods:
- The exploration function(**f()** method)
- The Q-Learning update method (**get_action()** method)
- Implement a decreasing function for the learning rate (**alpha()** method)

In this scenario we help the agent, via reinforcement learning, to navigate and maximise rewards within a map, aiming to reach the move between an initial state and the goal state, represented by a treasure chest. In some scenarios there will be a rupee that the agent can gather. The rewards are +50 for reaching the chest, +40 for getting the rupee and -1 for any other tile.

This assignment is not graded. Thus no tests are provided.

### Execution
The execution of this assignment can be done entirely in this Jupyter Notebook, or in two distinct python files. If you want to program/test outside of Jupyter just follow these instructions. Please note that currently there is a problem with pygame (a package responsible for displaying the agent moving in the environment) and Jupyter, which causes the jupyter kernel to crash after closing the pygame window.

In order to test your code and get the convergence episode, you can use the environment.py file:
```
python environment.py [Map]
```

To check the converged solution of your algorithm, you can run the GUI to see the agent executing the learned policy in each map.
```
python game.py [Map]
