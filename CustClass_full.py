import pandas as pd
import numpy as np


class Customer:
    ''' A single customer that moves through the supermarket in a MCMC simulation'''
    
    def __init__(self, c_id, name, state, budget=100):
        transition_matrix = pd.read_csv("data/transition_matrix.csv", index_col=0)
        self.c_id = c_id
        self.name = name
        self.state = state
        self.budget = budget
        self.transition_matrix = transition_matrix
        self.hist = [self.state]
        self.money = [self.budget]
    
    def __repr__(self):
        if self.hist[-1] == 'entrance' or self.hist[-1] == 'checkout':
            return f'Customer {self.name} in {self.state} with ${self.budget}.'
        else:
            return f'Customer {self.name} in {self.state} with ${self.budget} left, was in {self.hist[-2]}.'
    
    def is_active(self):
        """
        Returns True if the customer has not reached the checkout
        for the second time yet, False otherwise.
        """
        if self.state == 'checkout':
            return print(f'Customer {self.name} has been churned and spent ${cust1.money[0] - cust1.money[-1]}!')
        else:
            return print(f'Customer {self.name} is still active.')
        
    
    def next_state(self):
        '''
        Propagates the customer to the next state.
        '''

        next_loc = np.random.choice(self.transition_matrix.columns.values, p=self.transition_matrix.loc[self.state])
        #p = Probs
        
        #hard coded the revenue
        if next_loc == 'fruit':
            self.budget -= 4
        elif next_loc == 'spices':
            self.budget -= 3
        elif next_loc == 'dairy':
            self.budget -= 5
        elif next_loc == 'drinks':
            self.budget -= 6
        
        #list for 'path-history'
        self.state = next_loc
        self.hist.append(self.state)
        
        #list for money spend
        self.budget = self.budget
        self.money.append(self.budget)


