# stage-info-beamer
These are some nodes for the info-beamer software I created
to control a RaspberryPi, connected to a beamer on a stage.


buzzer
------
The aim of this node is, to use two Buzzers on a stage. If a buzzer is pressed, the other one should be "locked". The buzzer pressed first is shown with a big red square. 

The info-beamer node is listening for UDP-Input on Port 4444. Working commands are:

Command | Reaction
--- | ---
bl_on | Left Buzzer is pressed
bl_off | Left Buzzer is off
br_on | Right Buzzer is pressed
br_off | Right Buzzer is off

The corresponding Python-Script is listening on GPIO-Ports 2 and 3 for input.
IMPORTANT: The button you use has to interrupt the connection. (Pull-Up Resistor at the GPIO-Port)

You have to adjust the NODE_NAME variable in sendBuzzer.py , to send working info-beamer UDP commands.
