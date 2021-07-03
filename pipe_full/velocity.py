def velocity(Q,A):
    '''
    Function to calculate the velocity of flow

    Arguments: 
    Q - float - flow in l/s
    A - float - internal pipe area in m3

    Returns: 
    V - float - flow velocity in m/s
    '''
    V = (Q/1000)/A # m/s Flow velocity
    return V