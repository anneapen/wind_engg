import spectra as spectra

def test_kaimal_spectrum():
    Su=spectra.kaimal_spectrum(frequency=0.1,mean_wind_speed=10,std_dev=2,length_scale=20)
    assert Su==8.6