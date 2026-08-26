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

def wind_fluctuation(wind_speed):
    """
    Calculates mean wind speed, turbulent fluctuations and turbulent intensity
    from measured wind-speed data(taken as array).
    """

    wind_speed = np.asarray(wind_speed, dtype=float)

    mean_wind_speed = np.mean(wind_speed)

    fluctuations = wind_speed - mean_wind_speed

    std_dev=np.std(fluctuations)

    TI=turbulence_intensity(mean_wind_speed,std_dev)

    return mean_wind_speed,fluctuations,round(std_dev,2),TI

    