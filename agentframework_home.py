# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 09:03:56 2017

@author: gy15rt
"""

import random
          
class Agent:
    def __init__ (self, environment, agents):
        self.environment = environment
        self.store = 0
        # (0,len(environment[0])) means starting point to length of data across (width)
        self.x = random.randint(0,len(environment[0]))
        self.y = random.randint(0,len(environment))
        self.agents = agents
     
     # starting point - random
    def move (self):
            if random.random() < 0.5:
                self.x = (self.x + 1) % (len(self.environment[0]))
            else:
                self.x = (self.x - 1) % (len(self.environment[0]))
 
            if random.random() < 0.5:
                self.y = (self.y + 1) % (len(self.environment))
            else:
                self.y = (self.y - 1) % (len(self.environment))
                
    def eat (self): # can you make it eat what is left?
            if self.environment[self.y][self.x] > 10:
        
               self.environment[self.y][self.x] -= 10
        
               self.store += 10
              
    
 # Calculate the distance between self and the current other agent:        
    def distance_between(self, agent1):
        return (((self.x - agent1.x)**2) + ((self.y - agent1.y)**2))**0.5
    #this (distance_between) is now a fuction that is called below

    
    def share_with_neighbours (self, neighbourhood):
            self.neighbourhood = neighbourhood
            
            # Loop through the agents in self.agents . 
            for agent in self.agents:
                # Calculate the distance between self and the current other agent:
                distance = self.distance_between(agent)
                # If distance is less than or equal to the neighbourhood
                if distance <= self.neighbourhood:
                    # Sum self.store and agent.store
                    # Divide sum by two to calculate average. 
                    average = (self.store + agent.store)/2
                    self.store = average
                    agent.store = average
                #check it's working    
                #print("sharing" + str(distance) + " " + str(average))
    
