

def turbulence_intensity(mean_Vz:float,std_dev:float)->float:
    """
    """
    TI=std_dev/mean_Vz
    return round(TI,2)