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
     - Monitor and HDMI cable
       - I used a monitor that I had sitting around.  However, there are a couple considerations.  If you plan on using carpentry to build a frame, you may need to consider how easy/safe it is to remove the bezel of the monitor.  Additionally, the Pi pushes out to standard HDMI.  However, the Pi4 uses micro HDMI, so you will need a different cable.
     - USB Keyboard and Mouse for Setup and installation
       - The easiest way to set up your MagicMirror is directly connecting to the Pi.  However, SSH can be used for most of the installation if you want to use a remote computer to do it.  I also used VNC Server/viewer to remote into the desktop of the Pi for portions of this project.
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

## 2. Dependencies
   - Raspbian OS
     - Follow any guide that you want to etch your boot disk for the Pi.  Make sure you select Raspbian with GUI.  **The GUI is X and it is required for the MagicMirror package to run.** The image viewer, feh, and the scripts will work from the command line, but the MagicMirror requires X and will not run from the command line interface.  Additionally, some of the code required absolute references (where I put the complete file path) as opposed to relative references.  Because of this, all my file paths are expecting the username to be "pi", the default username created with a fresh Raspbian install.  If you are using a different username, the paths will need to be changed.
   - feh
     - feh is the image viewing software.  Install with the following code `sudo apt-get install feh`.
   - Pictures
     - Put some pictures (jpg and png preferred) into your /home/pi/Pictures/ folder.  No special characters in the filenames, but other than that limitation the file names can be anything.  
   - npm
     - npm is the framework that the Magic Mirror software works off of.  Install it with the following commands in order:
     ```
     curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
     sudo apt install -y nodejs
     git clone https://github.com/MichMich/MagicMirror
     cd MagicMirror/
     npm install
     npm start
     ```
     - Now you have cloned the repository that contains the pre-written MagicMirror code, installed npm and started it.
   - xdotool
     - xdotool is the keystroke emulator needed for ending both the MagicMirror and feh programs.  It was much cleaner to use a keystroke emulator than to kill the process from the command line.
     - install with the following `sudo apt-get install xdotool`
     
     
     
     
     
