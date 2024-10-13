from initialization import environment, agents

def update(environment=environment, agents=agents):
    remove_indexes = []
    for i in range(len(agents)):
        agents[i].move()
        if not environment.is_inside_circle(agents[i]):
            remove_indexes.append(i)
    for i in remove_indexes:
        del agents[i]
    return agents
