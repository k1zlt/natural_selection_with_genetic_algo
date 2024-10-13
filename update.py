from initialization import environment, agents
from agent import Agent
import random


def update(
    environment=environment,
    agents: list[Agent] = agents,
    reproduction_chance=0.01,
    live_constant=500,
    mutation_rate=1,
    birth_amount=1,
    mutation_chance=1,
    limit=1000,
):
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
    new_agents = []
    for agent in agents:
        if random.random() < reproduction_chance and len(agents) <= limit:
            new_agents = [
                *new_agents,
                *agent.reproduce(
                    amount=birth_amount,
                    mutation_rate=mutation_rate,
                    live_constant=live_constant,
                    mutation_chance=mutation_chance,
                ),
            ]
    if len(new_agents) != 0:
        agents = [*agents, *new_agents]
    return agents


# agents = update()
# print("Initial agent positions:")
# for agent in agents:
#     print(agent)
