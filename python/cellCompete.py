def cellCompete(states, days):
    n = len(states)
    for day in range(days):
        houses = [0] + states + [0]
        states = [houses[i-1] ^ houses[i+1] for i in range(1, n+1)]
    return states
