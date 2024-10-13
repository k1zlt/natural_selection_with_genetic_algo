from initialization import environment, agents
from agent import Agent

reproduce_time = 10
iteration = 1

def update(environment=environment, agents: list[Agent]=agents):
    global iteration
    remove_indexes = []
    for i in range(len(agents)):
        agents[i].move()
        if not environment.is_inside_circle(agents[i]):
            remove_indexes.append(i)
    for i in remove_indexes:
        del agents[i]
    iteration += 1
    if iteration%reproduce_time ==0:
        new_agents = []
        for agent in agents:
            new_agents.append(*agent.reproduce())
        agents.append(*new_agents) 
    return agents

agents = update()
print("Initial agent positions:")
for agent in agents:
    print(agent)

