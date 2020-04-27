# MagicMirror
###### Magic Mirror Project
###### Joel Levi Brooks
###### WBIT 4030
###### Spring 2020


##### This README is divided into 3 parts: Hardware, Dependencies, Files.

## 1. Hardware
   - Needed Hardware
     - Rasberry Pi, Power Adapter, MicroSD Card
       - I built this on a Raspberry Pi 3B+.  However, any Pi should work as they all will run the X GUI.  
     - PIR motion sensor.
       - You can find this on Amazon or e-Bay by searching for PIR Motion Sensor.
     - Breadboard
       - You can find one of these on Amazon or e-Bay by searching for Solderless Breadboard.
     - Three (3) Male to Female jumper cables
       - Easy to find, but usually sold in packs of 25+.  I used the 6 inch versions.
     - Two (2) Male to Male jumper cables
       - Easy to find, but usually sold in packs of 25+.  I used the 6 inch versions.  
     - vi. One (1) 100-Ohm Resistor
       - Easy to find, but the smallest pack I could find was a pack of 10.  

   - Hardware Installation
     - Pi
       - There are a million How-to's on setting up a Raspberry Pi.  Save yourself a ton of trouble and buy a quality MicroSD card as well as the official Pi Power Adapter.  I swear by the CanaKits that you can easily find on Amazon.
     - Wiring
       - M to M Jumper from positive rail (red) to some column on the breadboard.  
       - Connect black wire from PIR to this positive column.
       - M to M jumper from ground rail (black) to some column on the breadboard.
       - Connect the red wire from the PIR to this positive column.
       - Connect the signal wire (yellow) from the PIR to the bottom of a column on the breadboard.
       - Put the Resistor between the signal wire and the transmission wire.
       - M to F Jumper on the same column as the signal wire.  this is the transmission wire.  The female end goes to GPIO pin 11.  **If you are using my code directly, you must connect transmission wire to GPIO pin 11.**
       - M to F Jumper from GPIO Pin 4 to positive rail of breadboard.  You can use any of the pins that provide 5v of power, 4 is just the one I arbitrarily used.
       - M to F Jumper from GPIO Pin 34 to ground rail of breadboard.  You can use any of the ground pins, I just arbitrarily used pin 34.
     - Adjustments
       - The PIR has adjustment dials.  Mine worked just fine out of the box, but if you need to tweak it, please read the documentation that came with your PIR.
     
     
