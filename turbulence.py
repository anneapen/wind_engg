

def turbulence_intensity(mean_Vz:float,std_dev:float)->float:
    """
    """
    TI=std_dev/mean_Vz
    return round(TI,2)

def turbulence_std_dev(ti:float,mean_Vz:float)->float:
    """
    """
    std_dev=ti*mean_Vz
    return round(std_dev)