import numpy as np


def spectrum(frequency,
    mean_wind_speed,
    std_dev,
    length_scale
):
    """
    Calculate longitudinal turbulence spectrum
    using a Kaimal-type formulation.
    """

    frequency = np.asarray(frequency, dtype=float)

    n = frequency * length_scale / mean_wind_speed

    Su = (
        4 * std_dev**2 * length_scale / mean_wind_speed
        /
        (1 + 6 * n) ** (5 / 3)
    )

    return Su