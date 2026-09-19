import numpy as np
from scipy.signal import welch


def kaimal_spectrum(frequency,
    mean_wind_speed,
    std_dev,
    length_scale
):
    """
    Calculates longitudinal turbulence spectrum
    using a Kaimal-type formulation.
    """

    n = frequency * length_scale / mean_wind_speed

    Su = (
        4 * std_dev**2 * length_scale / mean_wind_speed
        /
        (1 + 6 * n) ** (5 / 3)
    )

    return round(Su,2)


def welch_spectrum(wind_speed, sampling_freq):
    """
    """

    wind_speed = np.asarray(
        wind_speed,
        dtype=float
    )

    frequency, psd = welch(
        wind_speed,
        fs=sampling_freq,nperseg=8
    )

    return frequency, psd

