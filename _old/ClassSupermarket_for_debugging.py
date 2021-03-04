#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import time
from faker import Faker

from CustClass_full import Customer



#import transition_matrix
transition_matrix = pd.read_csv("data/transition_matrix.csv", index_col=0)



# In[54]:


# class Customer:
#     ''' a single customer that moves through the supermarket in a MCMC simulation'''
    
#     def __init__(self, name, state, c_id = 1, budget=np.random.randint(100,500, dtype=int)):
#         self.c_id = c_id
#         self.name = name
#         self.state = state
#         self.budget = budget
#         self.transition_matrix = transition_matrix
#         self.hist = [self.state]
#         self.money = [self.budget]
    
#     def __repr__(self):
#         if self.hist[-1] == 'entrance' or self.hist[-1] == 'checkout':
#             return  f'Customer {self.name} in {self.state} with {self.budget} $'
#         else:
#             return f'Customer {self.name} in {self.state} with {self.budget} $ left, was in {self.hist[-2]}'
    
#     def is_active(self):
#         """
#         Returns True if the customer has not reached the checkout
#         for the second time yet, False otherwise.
#         """
#         if self.state == 'checkout':
#             return f'Customer {self.name} has been churned and spent {cust1.money[0] - cust1.money[-1]}$!'
#         else:
#             return f'Customer {self.name} is still active.'
        
    
#     def next_state(self):
#         '''
#         Propagates the customer to the next state.
#         '''

#         next_loc = np.random.choice(self.transition_matrix.columns.values, p=self.transition_matrix.loc[self.state])
#         #p = Probs
        
#         #hard coded the revenue
#         if next_loc == 'fruit':
#             self.budget -= 4
#         elif next_loc == 'spices':
#             self.budget -= 3
#         elif next_loc == 'dairy':
#             self.budget -= 5
#         elif next_loc == 'drinks':
#             self.budget -= 6
        
#         #list for 'path-history'
#         self.state = next_loc
#         self.hist.append(self.state)
        
#         #list for money spend
#         self.budget = self.budget
#         self.money.append(self.budget)


# In[76]:


class Supermarket:
    """manages multiple Customer instances that are currently in the market.
    """

    def __init__(self, hour=7):        
        # a list of Customer objects
        self.customers = []
        self.minutes = 0
        self.current_time = 0
        self.data = pd.DataFrame()
        self.timestamp = []
        #self.time = time #open
        self.hour = hour

    def __repr__(self):
        return f'Supermarket("{self.customers}", "{self.current_time}")'

    def get_time(self):
        """current time in HH:MM format,
        """
        #self.time = time.strftime("%H:%M:%S") #current time
        
        #the supermarket opens at 7
        hour = self.hour
        minutes = self.minutes
        timestamp = f'{str(hour)}:{str(minutes)}'
        self.timestamp.append(timestamp)
        
        
    def print_customers(self):
        """print all customers with the current time and id in CSV format.
        """
        self.current_time = self.get_time()
        return f'Supermarket("{self.customers}", "{self.current_time}")'
        
    def next_minute(self):
        """propagates all customers to the next state.
        """

        self.minutes += 1

        self.move_customers()
        self.add_new_customers()
        self.remove_existing_customers()
        return self.customers
    
    
    def move_customers(self):
        for cust in self.customers:
            cust.next_state()
            
    def add_new_customers(self):
        """randomly creates new customers.
        """
        fake = Faker()
        self.customers.append(Customer(fake.name(), 'entrance', np.random.randint(1,500))) #self.c_id, 
        

    def remove_existing_customers(self):
        """removes every customer that is not active any more.
        """
        for cust in self.customers:
            if cust.state == 'checkout':
                self.customers.remove(cust) #removes the first matching element (which is passed as an argument) from the list
                print(f'Customer {cust.name} has been churned!')
                
    def write_all_cust(self):
        for cust in self.customers:
            self.data = pd.DataFrame.append(cust.name, cust.state, cust.budget, self.current_time)


# In[77]:


# Supermarket1=Supermarket()


# Supermarket1.next_minute()


# In[75]:




# In[23]:





# In[12]:





# In[ ]:


# for i in customers: #move all customers
#     i.next_state()
#     if i.state == 'checkout':
#         print(f'Customer {i.name} has been churned!') #adding time?
#         customers.remove(i)
#     else:
#         print(i)
#     if len(customers) < 20: #new_customers
#             x = 20 - len(customers)
#             #new_cust = []
#             new_cust = ([Customer(fake.name(), 'entrance', np.random.randint(1,500)) for i in range(x)])
#             for c in new_cust:
#                 customers.append(c)


# In[20]:


#print(Supermarket)


# In[24]:


#rint_customers()


# In[ ]:


# def add_new_customers(self, stop, id_suffix, terrain_map, image, x, y):
#     """randomly creates new customers.
#     """
#     for i in range(stop):
#         cust = Customer(str(i) + "_" + str(id_suffix), "entrance", transition_matrix,
#                         terrain_map=terrain_map, image=image, x=x, y=y)
#         self.customers.append(cust)

#     self.id_suffix += 1


# In[5]:




# In[ ]:





# In[29]:


# import datetime


# # In[33]:


# datetitime(7, 26)


# # In[16]:


# datetime.datetime.now().time()


# # In[35]:


# import time


# # In[37]:


# time.time(7, 26)


# # In[18]:


# time.strftime("%a, %d %b %Y %H:%M:%S")


# # In[19]:


# time.strftime("%H:%M:%S")

