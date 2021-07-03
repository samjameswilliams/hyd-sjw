def area_pipe(ID):
    '''
    Function to calculate the internal area of the pipe

    Arguments: ID - float - internal diameter in mm

    Returns: A - float - internal pipe area in m3

    Dependencies - math
    '''
    import math
    A = (math.pi*((ID/1000)**2))/4 # m**2 Pipe area
    return A