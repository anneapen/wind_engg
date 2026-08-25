
import profiles as profiles
import pytest as pytest

def test_power_law_wind_speed():
    Vz=profiles.power_law_wind_speed(80,10,25,'open')
    assert Vz==33.45

