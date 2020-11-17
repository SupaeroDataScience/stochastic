def mutate(ind):    
    rng = np.random.default_rng()
    x = rng.choice(len(ind))
    child = np.copy(ind)
    child[x] = ind[x+1]
    child[x+1] = ind[x]
    return child
