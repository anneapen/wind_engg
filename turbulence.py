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

def auto_correlation(fluctuations):
    """
    """
    #Correlating the fluctuations with both negative and positive shifts
    correlation=np.correlate(fluctuations,fluctuations,"full")

    #Considering only positive shifts because we're interested in how does correlation decay as we move forward in time
    correlation=correlation[correlation.size//2:]

    #Normalilizing the correlation 
    #At zero lag, the wind signal is being compared with itself without any shift, so it should represent perfect correlation.
    correlation=correlation/correlation[0]

    return np.round(correlation,2)

def integral_time_scale(fluctuations, sampling_freq: float):
    """
    Calculate integral turbulence time scale.
    """

    if sampling_freq <= 0:
        raise ValueError("Sampling frequency must be greater than zero.")

    dt = 1 / sampling_freq

    R = auto_correlation(fluctuations)

    zero_crossing = np.where(R <= 0)[0]

    if len(zero_crossing) == 0:
        raise ValueError("Autocorrelation does not cross zero.")

    first_zero = zero_crossing[0]

    # Exact zero crossing
    if R[first_zero] == 0:

        Tu = np.trapezoid(
            R[:first_zero + 1],
            dx=dt
        )

    else:

        R1 = R[first_zero - 1]
        R2 = R[first_zero]

        t1 = (first_zero - 1) * dt
        t2 = first_zero * dt

        # Interpolated zero-crossing time
        t_zero = t1 - R1 * (t2 - t1) / (R2 - R1)

        # Area up to last positive autocorrelation value
        Tu = np.trapz(
            R[:first_zero],
            dx=dt
        )

        # Add final triangular area
        Tu += 0.5 * R1 * (t_zero - t1)

    return round(Tu,2)

def integral_length_scale(mean_wind_speed,time_scale):
    """
    Returns the integral length scale
    """
    if mean_wind_speed <= 0:
        raise ValueError(
            "Mean wind speed must be greater than zero."
        )

    if time_scale <= 0:
        raise ValueError(
            "Time scale must be greater than zero."
        )

    L_u = mean_wind_speed * time_scale

    return L_u