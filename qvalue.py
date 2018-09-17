from common import *
class QValue:
	
    def __init__ (self, state, action):
        self.state = state
        self.action = action
        self.feat_vec = list(self.state.feat_vec)
        for a in ACTIONS: 
            if a == action: self.feat_vec.append(0)
            else: self.feat_vec.append(0)

    def __hash__ (self):
        return hash(str(self.state) + str(self.action))
    
    def __repr__(self):
    	return str(self.state) + str(self.action)

    def __eq__(self, other):
        return str(self) == str(other)
