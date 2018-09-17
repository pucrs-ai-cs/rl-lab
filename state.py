# State representation for Q-Learning.
class State:

    def __init__ (self, x, y, rupees):
        self.x = x
        self.y = y
        self.rupees = list(rupees)
        self.feat_vec = []

    def __hash__ (self):
        return hash(str(self))

    def __repr__(self):
    	return str(self.x) + str(self.y) + str(self.rupees)

    def __eq__(self, other):
        return str(self) == str(other)
