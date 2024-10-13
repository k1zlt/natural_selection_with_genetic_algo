from initialization import environment, agents
from agent import Agent
import random

reproduce_time = 40
iteration = 1

def update(environment=environment, agents: list[Agent]=agents):
    global iteration
    remove_indexes = []
    for i in range(len(agents)):
        agents[i].move()
        if not environment.is_inside_circle(agents[i]):
            remove_indexes.append(i)

        if not agents[i].is_alive():
            if not (i in remove_indexes):
                remove_indexes.append(i)
         
    for i in remove_indexes[::-1]:
        del agents[i]
    iteration += 1
    new_agents = []
    for agent in agents:
        if random.random() < 0.01:  # 80% chance to reproduce
            new_agents = [*new_agents, *agent.reproduce()]
    if len(new_agents) != 0:
        agents = [*agents,*new_agents] 
    return agents

# agents = update()
# print("Initial agent positions:")
# for agent in agents:
#     print(agent)

