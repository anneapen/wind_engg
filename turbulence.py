import numpy as np

def turbulence_intensity(mean_Vz:float,std_dev:float)->float:
    """
    Returns the turbulent intensity from the given mean wind speed and standard deviation of the fluctuations
    """
    TI=std_dev/mean_Vz
    return round(TI,2)

def turbulence_std_dev(ti:float,mean_Vz:float)->float:
    """
    Returns the standard deviation of the fluctuations from given mean wind speed and turbulent intensity
    """
    std_dev=ti*mean_Vz
    return round(std_dev)

