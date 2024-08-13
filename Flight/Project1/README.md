"""Project 1"""
This project is walks covers basic control of a drone including connecting, arming, takeoff, landing, and simple waypoint movement.
It focuses on basic commands with MAVSDK one of the Libraries that we use.

""Useful Commands""
For takeoff the command below can be used the number signifies the takeoff altitude.
'''
await drone.param.set_param_float("MIS_TAKEOFF_ALT", 25)
'''

MavSDK's go_to_location and return_to_launch will also be useful when navigating the waypoints and landing.
Reference the MavSDK documents below to find how to call the commands.

""Testing""
QGroundControl and JMAVSIM
Both should have been setup in the installation guide. If they aren't navigate [here](https://missourimrr.github.io/docs/flight/installation_guide/)

To open QGroundControl, right click the app image and select run.
To open JMAVSIM, type ./opensitl.sh in your terminal and press enter to run.
Wait for both to open and connect before running your code.

""Extra Information""
MAVSDK is a python library that uses Mavlink and the PX4 firmware to autonomously control a drone.
To start flight the drone needs to be connected to, armed (firmware becomeing prepped to fly), and then controlled through code.

[Flight Docs](https://missourimrr.github.io/docs/flight/) have more indepth information about firmware and libraries that we use.

[MavSDK](http://mavsdk-python-docs.s3-website.eu-central-1.amazonaws.com) while hard to navigate has all the commands and information to use it to control the drone.

When picking coordinates Google Earth is the best to use while it is not needed in this project it is useful to note for the future.
