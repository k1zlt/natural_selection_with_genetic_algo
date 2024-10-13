from initialization import environment, agents
from agent import Agent

reproduce_time = 40
iteration = 1

def update(environment=environment, agents: list[Agent]=agents):
    global iteration
    remove_indexes = []
    for i in range(len(agents)):
        agents[i].move()
        if not environment.is_inside_circle(agents[i]):
            remove_indexes.append(i)
    for i in remove_indexes[::-1]:
        del agents[i]
    iteration += 1
    if iteration%reproduce_time ==0:
        new_agents = []
        for agent in agents:
            new_agents = [*new_agents,*agent.reproduce()]
            print()
        if len(new_agents) != 0:
            agents = [*agents,*new_agents] 
    return agents

# agents = update()
# print("Initial agent positions:")
# for agent in agents:
#     print(agent)

