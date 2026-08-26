import turbulence as turbulence

def test_turbulence_intensity():
    TI=turbulence.turbulence_intensity(20,3)
    assert TI==0.15