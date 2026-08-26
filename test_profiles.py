
import profiles as profiles


def test_power_law_wind_speed():
    Vz=profiles.power_law_wind_speed(80,10,25,'open')
    assert Vz==33.45

def test_friction_velocity():
    V_friction=profiles.friction_velocity(10,20,'suburban')
    assert V_friction==2.28