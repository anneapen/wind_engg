import turbulence as turbulence

def test_turbulence_intensity():
    TI=turbulence.turbulence_intensity(20,3)
    assert TI==0.15

def test_turbulence_std_dev():
    sd=turbulence.turbulence_std_dev(0.15,20)
    assert sd==3