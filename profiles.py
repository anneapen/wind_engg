
def power_law_wind_speed(z:float,zref:float,Vref:float,alpha:float)->float:
    """
    Returns the wind speed based on power law
    """
    Vz=Vref*((z/zref)**alpha)
    return round(Vz,2)