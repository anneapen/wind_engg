import turbulence as turbulence
import numpy as np
import pytest as pytest

def test_turbulence_intensity():
    TI=turbulence.turbulence_intensity(20,3)
    assert TI==0.15

def test_turbulence_std_dev():
    sd=turbulence.turbulence_std_dev(0.15,20)
    assert sd==3

def test_wind_fluctuation():
    mean_wind_speed,fluctuations,std_dev,TI=turbulence.wind_fluctuation([10.2, 11.1, 9.8, 10.7, 10.4])
    assert mean_wind_speed==10.44
    assert np.allclose(fluctuations,[-0.24, 0.66, -0.64, 0.26, -0.04])
    assert std_dev==0.44
    # assert TI==0.04
    assert TI == pytest.approx(0.04)