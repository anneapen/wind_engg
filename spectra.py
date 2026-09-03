import numpy as np


def kaimal_spectrum(frequency,
    mean_wind_speed,
    std_dev,
    length_scale
):
    """
    Calculate longitudinal turbulence spectrum
    using a Kaimal-type formulation.
    """

    n = frequency * length_scale / mean_wind_speed

    Su = (
        4 * std_dev**2 * length_scale / mean_wind_speed
        /
        (1 + 6 * n) ** (5 / 3)
    )

    return round(Su,2)