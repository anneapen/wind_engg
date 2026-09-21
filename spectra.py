import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import welch


def kaimal_spectrum(frequency,mean_wind_speed,std_dev,length_scale):
    """
    Calculates longitudinal turbulence spectrum
    using a Kaimal-type formulation.
    """

    n = frequency * length_scale / mean_wind_speed

    Su = (4 * std_dev**2 * length_scale / mean_wind_speed/(1 + 6 * n) ** (5/3))
    return round(Su,2)

def von_karman_spectrum(frequency,mean_wind_speed,std_dev,length_scale):
    """
    Calculates longitudinal turbulence spectrum
    using Von Karman model
    """
    frequency = np.asarray(frequency, dtype=float)
    n = (frequency* length_scale/ mean_wind_speed)

    Su = (4* std_dev**2* length_scale/ mean_wind_speed/ (1 + 70.8 * n**2)**(5/6))
    return round(Su,2)


def welch_psd(wind_speed, sampling_freq):
    """
    Estimate PSD from measured wind data 
    """

    wind_speed = np.asarray(wind_speed,dtype=float)

    frequency, psd = welch(wind_speed,fs=sampling_freq,nperseg=8)

    return frequency, psd


def welch_spectrum(wind_speed, sampling_freq):
    """
    Plots the Welch Spectrum for the measured wind data
    """
    frequency, psd=welch_psd(wind_speed, sampling_freq)
    plt.figure(figsize=(6, 8))

    plt.plot(frequency,psd)
    
    plt.xlabel("Frequency")
    plt.ylabel("PSD")
    plt.title("Welch Spectrum")
    
    plt.xlim(0, 1)
    plt.ylim(0, 10)
    
    plt.grid()
    plt.show()


