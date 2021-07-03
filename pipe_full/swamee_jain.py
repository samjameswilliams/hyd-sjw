class swamee_jain():
    '''
    Class to calculate the friction factor 

    Attributes to instantiate: 
    V - float - flow velocity m/s
    ID - float - internal diameter of pipe mm
    v - float - viscosity m**2/s - default value for water

    Attributes created at instantiation: 
    Re - float - diensionless
    Re_ok - boolean - True if Re > 4000, required to satisfy STW requirements
    Re_ok_txt - message related to acceptability of Re number
    '''
    def __init__(self,V,ID,v=1*10**-6):
        self.V = V
        self.ID = ID
        self.Re = (V*(ID/1000))/v # dimensionless
        self.Re_ok = Re > 4000
        if self.Re_ok:
            self.Re_ok_txt = '> 4000, acceptable.'
        else:
            self.Re_ok_txt = '< 4000, unacceptable, increase flow velocity or decrease pipe diameter.'
    
    def __str__(self):
        return f'Reynolds no.{self.Re}{self.Re_ok_txt}'