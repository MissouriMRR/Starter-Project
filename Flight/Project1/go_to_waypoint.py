###########################################   --Do not edit--  ########################################################

#Everything here will roughly be similar everytime when booting the drone in other code

import asyncio
from mavsdk import System

async def run():                                        ## definition of an asynchronous function called run
    drone: System = System()                                    ## Creates a new system object named drone that can be used later when  
                                                        ## calling any type of system methods
    await drone.connect(system_address="udp://:14540")  ## The connect function is used to connect the physical drone and the simulated drone. 
                                                        ## The system address parameter can be changed to connect to either the real drone, or the simulator drone.

    print("Waiting for drone to connect...")
    async for state in drone.core.connection_state():   ## Loops over the connection state function to check if drone is properly connected to the given system address
        if state.is_connected:                          ## Prints the following statement if properly connected
            print(f"-- Connected to drone!")
            break
    
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