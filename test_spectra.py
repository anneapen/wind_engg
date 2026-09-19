import spectra as spectra
import numpy as np

def test_kaimal_spectrum():
    Su=spectra.kaimal_spectrum(frequency=0.1,mean_wind_speed=10,std_dev=2,length_scale=20)
    assert Su==8.6

def test_welch_spectrum():
    wind_speed=[10,12,10,8,10,12,10,8]
    sampling_freq=1
    frequency, psd=spectra.welch_spectrum(wind_speed, sampling_freq)
    assert np.allclose(frequency,[0., 0.125, 0.25 , 0.375, 0.5])
    assert np.allclose(psd,[ 0.,  2.66666667, 10.66666667,  2.66666667,  0.])
