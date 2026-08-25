
def power_law_wind_speed(z:float,z_ref:float,V_ref:float,terrain:str)->float:
    """
    Returns the wind speed based on power law
    """
    if z <= 0:
        raise ValueError("Height z must be greater than zero.")

    if V_ref <= 0:
        raise ValueError("Reference wind speed V_ref must be greater than zero.")

    if z_ref <= 0:
        raise ValueError("Reference height z_ref must be greater than zero.")

    if terrain!=("open" or "suburban" or "urban"):
        raise ValueError("Terrain should be open/suburban/urban .")
        
    alpha={"open":0.14,"suburban":0.22,"urban":0.33}
    
    Vz=V_ref*((z/z_ref)**alpha[terrain])
    return round(Vz,2)