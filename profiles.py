
def power_law_wind_speed(z:float,z_ref:float,V_ref:float,alpha:float)->float:
    """
    Returns the wind speed based on power law
    """
    if z <= 0:
        raise ValueError("Height z must be greater than zero.")

    if V_ref <= 0:
        raise ValueError("Reference wind speed V_ref must be greater than zero.")

    if z_ref <= 0:
        raise ValueError("Reference height z_ref must be greater than zero.")

    if alpha < 0:
        raise ValueError("Power-law exponent alpha cannot be negative.")
        
    Vz=V_ref*((z/z_ref)**alpha)
    return round(Vz,2)