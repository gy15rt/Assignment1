# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 09:03:12 2017

@author: gy15rt
"""
import csv
import random
import operator
import matplotlib.pyplot
import agentframework_home as agentframework
import sys
import matplotlib.animation 

# a new empty list to contain the environment data from the csv file
environment = [] 

# using the open function to bring the data in 
# leave quote_num to leave the data as floats
f = open('in.txt', newline='') 
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)

# a 'for' loop to put the data into rows and then the rows into environment list
for row in reader:
    rowlist = [] 				# A list of new empty rows

    for value in row:
        rowlist.append(value)   # A list of value

        #print(value) 				# Floats
    environment.append(rowlist)   
        
f.close() 	# Don't close until you are done with the reader;


# this shows the empty plot - 300 by 300
matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.show()


# empty agent list to put the agents in
agents = []

# this checks there's a link to the Agent class for both environment and agents
a = agentframework.Agent(environment, agents)
print(a.x, a.y)
 
a.move()
print(a.x, a.y)
#to show it's working the print outs should be random each time and show 1 unit movement from starting point.

    
# the number of agents in the model 
#num_of_agents = int(sys.argv[1])
num_of_agents=20
#the number of times each agent is going to move
#num_of_iterations = int(sys.argv[2])
num_of_iterations = 200
# the area they move in  
#neighbourhood = int(sys.argv[3])
neighbourhood = 30

 
# Make the agents and append to env
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents))
     

# random.shuffle(x[, random]) - added below to shuffle the agents
# Move the agents. iterations goes first so each agent moves one iter' then the next iter
for j in range(num_of_iterations):
    random.shuffle(agents)    
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)
        
#how much have they 'sheep' eaten? remove comment # to print
consumption = 0
for sheep in agents:       
    consumption = (consumption + sheep.store) 
#print (consumption)


# this will write out the data that has been consumed - unhash to create csv file
#f2 = open('consumption.csv', 'a', newline='') 
#f2.write(str(consumption) + '\n')
#writer = csv.writer(f2, delimiter=' ')
#for row in data:		
#	writer.writerow(row)		# List of values.
#f2.close()
   
#sets axis and shows undelying environment
matplotlib.pyplot.xlim(0, 300)
matplotlib.pyplot.ylim(0, 300)
matplotlib.pyplot.imshow(environment)

#shows agents in environment
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
matplotlib.pyplot.show()

# The following code should enable you to see the agents moving over the 300/300 environment as an animation
# Errors appearing from matplotlib animation
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])


ax.set_autoscale_on(False)

# Make the agents.
for i in range(num_of_agents):
    agents.append([random.randint(0,300),random.randint(0,300)])

def update(frame_number):
    
    fig.clear()   

    for i in range(num_of_agents):
            if random.random() < 0.5:
                agents[i][0]  = (agents[i][0] + 1) % 99 
            else:
                agents[i][0]  = (agents[i][0] - 1) % 99
            
            if random.random() < 0.5:
                agents[i][1]  = (agents[i][1] + 1) % 99 
            else:
                agents[i][1]  = (agents[i][1] - 1) % 99 
        
   
    
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i][0],agents[i][1])
        print(agents[i][0],agents[i][1])


animation = matplotlib.animation.FuncAnimation(fig, update, interval=1)

























     
        
        
