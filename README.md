# stage-info-beamer
These are some nodes for the info-beamer software I created
to control a RaspberryPi, connected to a beamer on a stage.


buzzer
------
The aim of this node is, to use two Buzzers on a stage. If a buzzer is pressed, the other one should be "locked". The buzzer pressed first is shown with a big red square. 

The info-beamer node is listening for UDP-Input on Port 4444. Working commands are:

Command | Reaction
--- | ---
[nodeName]/buzzer:bl_on | Left Buzzer is pressed
[nodeName]/buzzer:bl_off | Left Buzzer is off
[nodeName]/buzzer:br_on | Right Buzzer is pressed
[nodeName]/buzzer:br_off | Right Buzzer is off

You have to adjust the NODE_NAME variable in sendBuzzer.py , to send working info-beamer UDP commands.
The corresponding Python-Script is listening on GPIO-Ports 2 and 3 for input.
IMPORTANT: The button you use has to interrupt the connection. (Pull-Up Resistor at the GPIO-Port)
Also: Replace Horn.wav with a real sound file. Due to License Reasons, I just uploaded an empty file.

twitter
-------
This is just a simple twitter wall, which shows the tweets in chronological order on the screen. 
Edit twitter.py for your needs, especially your tokens/secrets and the hashtag you want to search for. 
Also: Replace arial.ttf with a proper font file. Again: License reasons.
