
import profiles as profiles

def test_power_law_wind_speed():
    Vz=profiles.power_law_wind_speed(80,10,25,0.2)
    assert Vz==37.89