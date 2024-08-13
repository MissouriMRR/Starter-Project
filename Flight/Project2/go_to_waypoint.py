###########################################   --Do not edit--  ########################################################

#Everything here will roughly be similar everytime when booting the drone in other code

import asyncio
from mavsdk import System
import dronekit_sitl
import time
from dronekit import connect, VehicleMode, LocationGlobalRelative

async def run():                                        ## definition of an asynchronous function called run
    
    sitl = dronekit_sitl.start_default()
    connection_string = sitl.connection_string()

    # Connect to the Vehicle
    print('Connecting to vehicle on: %s' % connection_string)
    drone = connect(connection_string, wait_ready=True)
    
    print("Basic pre-arm checks")
    # Don't try to arm until autopilot is ready
    while not drone.is_armable:
        print(" Waiting for vehicle to initialise...")
        time.sleep(1)

    print("Arming motors")
    # Copter should arm in GUIDED mode
    drone.mode = VehicleMode("GUIDED")
    drone.armed = True

    # Confirm vehicle armed before attempting to take off
    while not drone.armed:
        print(" Waiting for arming...")
        time.sleep(1)

    print("Set default/target airspeed to 3")
    drone.airspeed = 3

    return drone


#######################################################################################################################



###########################################  -- Code Here -- ##########################################################

# Create an async function below for the take off of the drone, and moving to the different waypoints.
# The async function above can be used as an example.
# Example Coordinates 
#    (37.94852048112047, -91.78427643078165)
#    (37.94852048108085, -91.78427643078165)
#    (37.94852048104123, -91.78427643078165)
# make sure to pass drone as a parameter into move to function




if __name__ == "__main__":
    try:
        #call the run and move to waypoint function
        print("Starting Project")

    finally:
        print("Done!")