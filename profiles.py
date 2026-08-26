import matplotlib.pyplot as plt
import numpy as np



def power_law_wind_speed(z:float,z_ref:float,V_ref:float,terrain:str)->float:
    """
    Returns the wind speed (Vz,m/s) for the given height (z,m),reference height(z_ref,m), 
    refernce speed (V_ref,m/s) & terrain conditions based on power law
    """
    if z <= 0:
        raise ValueError("Height z must be greater than zero.")

    if V_ref <= 0:
        raise ValueError("Reference wind speed V_ref must be greater than zero.")

    if z_ref <= 0:
        raise ValueError("Reference height z_ref must be greater than zero.")

    if terrain!=("open" or "suburban" or "urban"):
        raise ValueError("Terrain should be open/suburban/urban .")
        
    alpha={"open":0.14,"suburban":0.22,"urban":0.33}
    
    Vz=V_ref*((z/z_ref)**alpha[terrain])
    return round(Vz,2)

def power_law_wind_speed_profile(z_ref:float,V_ref:float,terrain:str):
    """
    Plots the wind speed for the given reference height(z_ref), refernce speed (V_ref) & terrain conditions
    based on power law
    """

    if V_ref <= 0:
        raise ValueError("Reference wind speed V_ref must be greater than zero.")

    if z_ref <= 0:
        raise ValueError("Reference height z_ref must be greater than zero.")

    if terrain!=("open" or "suburban" or "urban"):
        raise ValueError("Terrain should be open/suburban/urban .")
        
    alpha={"open":0.14,"suburban":0.22,"urban":0.33}

    #Heights
    z = np.linspace(1, 200, 200)
    #Calculating wind speeds    
    Vz=V_ref*((z/z_ref)**alpha[terrain])

    #Plot
    plt.figure(figsize=(6, 8))

    plt.plot(Vz, z)
    
    plt.xlabel("Wind Speed (m/s)")
    plt.ylabel("Height (m)")
    plt.title("Power Law Wind Profile")
    
    plt.xlim(0, 50)
    plt.ylim(0, 200)
    
    plt.grid()
    plt.show()

def friction_velocity(z_ref:float,V_ref:float,terrain:str)->float:
    """
    Returns the friction velocity for the given reference height, velocity and terrain conditions
    """
    k=0.4
    if V_ref <= 0:
        raise ValueError("Reference wind speed V_ref must be greater than zero.")

    if z_ref <= 0:
        raise ValueError("Reference height z_ref must be greater than zero.")
    
    z0={"open":0.03,"suburban":0.3,"urban":1}
    k=0.4
    V_friction=k*V_ref/np.log(z_ref/z0[terrain])
    return round(V_friction,2)


def logarithmic_law_wind_speed(z:float,z_ref:float,V_ref:float,terrain:str)->float:
    """
    Returns the wind speed using logarithmic law for the given height,reference height, velocity and terrain conditions
    """

    if z <= 0:
        raise ValueError("Height z must be greater than zero.")
    if terrain not in ("open", "suburban", "urban"):
        raise ValueError("Terrain should be open/suburban/urban .")
    
    z0={"open":0.03,"suburban":0.3,"urban":1}
    V_friction=friction_velocity(z_ref,V_ref,terrain)
    k=0.4
    
    Vz=(V_friction/k)*np.log(z/z0[terrain])
    return round(Vz,2)

def logarithmic_law_wind_speed_profile(z_ref:float,V_ref:float,terrain:str):
    """
    Plots the wind speed for the given reference height(z_ref), refernce speed (V_ref) & terrain conditions
    based on logarithmic law
    """

    if V_ref <= 0:
        raise ValueError("Reference wind speed V_ref must be greater than zero.")

    if z_ref <= 0:
        raise ValueError("Reference height z_ref must be greater than zero.")

    if terrain not in ("open", "suburban", "urban"):
        raise ValueError("Terrain should be open/suburban/urban .")
        
    z0={"open":0.03,"suburban":0.3,"urban":1}
    #Heights
    z = np.linspace(1, 200, 200)
    V_friction=friction_velocity(z_ref,V_ref,terrain)
    k=0.4
    #Calculating wind speeds 
    Vz=(V_friction/k)*np.log(z/z0[terrain])

    #Plot
    plt.figure(figsize=(6, 8))

    plt.plot(Vz, z)
    
    plt.xlabel("Wind Speed (m/s)")
    plt.ylabel("Height (m)")
    plt.title("Power Law Wind Profile")
    
    plt.xlim(0, 50)
    plt.ylim(0, 200)
    
    plt.grid()
    plt.show()