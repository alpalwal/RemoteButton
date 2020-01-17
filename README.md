
## Parts Needed

Arduino ESP8266:  
https://www.amazon.com/gp/product/B010N1SPRK

Servo:  
https://www.amazon.com/gp/product/B073F4TRSK

Arduino > Servo Jumper Cables:
https://www.amazon.com/Antrader-Ribbon-Cables-Arduino-Raspberry/dp/B07RYM1L3Z

Amazon  IOT 1-click button:  
https://www.amazon.com/dp/B075FPHHGG?ref=ppx_pop_mob_ap_share

## Print
Download and print this file:  
https://www.thingiverse.com/thing:4107176  

This will house the arduino and servo.  

### Connect the Arduino and the Servo
Attach the servo to the Arduino. 
- Black to ground
- White to 5v+
- Grey to D4 (Pin digital 4)  

If you have a soldering iron, you can cut/shorten the cables so that there's less spare wire in the final assembly. 


### Load the Arduino code
- Hook up the Arduino to your computer. You'll need a couple of supporting libraries to be able to communicate to it. 
- In arduino_code.ino, update these two lines:
    - ESP8266WebServer server(5646);   // Update 5646 to whatever port you  would like to have the Arduino's webserver running on
    - wifiMulti.addAP("yourSSID", "yourPassword");   // add Wi-Fi networks you want to connect to (multiple can be added and it'll join the  strongest)

- In your router, find the MAC address for the Arduino  and give it a static IP address. The address that you give doesn't matter, we just don't want it changing.  
- In the router, set up port forwarding. You want to expose whatever port is set up on the Arduino.  
- Once the port forwarding is set up, get your public IP address by going to http://icanhazip.com/
- In your browser, go to your IP address : your port. Ex: http://14.35.66.21:5646 You should see the motor move. 

### Set up the 1-click button
- If you don't already have one, you'll need an AWS account to use the 1-click button. 
- Run through the setup on your 1-click button using the phone app. Make sure it's added to a project, the device is enabled, etc. 
- Set the action when a button is pressed to trigger a lambda function.

### Update the Lambda function
- In the lambda function that the button creates, clear out the code and paste in the code from lambda_function.py
- Replace the IP and port with the IP and port of your Arduino.


### Package
- Install the Arduino and servo in the housing. Ensure that when the button is pressed and the servo  moves, that it initially moves CCW. If it moves clockwise initially, flip it over. 
- Use small/short screws to lock the servo into place. 

### Adjust
- Put the assembly over the button you're trying to press
- The servo arm can be moved by removing the screw on the front, and then pulling/rotating/reinstalling the arm. This is a great first adjustment for the arm angle. 
- If you need the arm to press less on the button, you can put a spacer under the motor/Arduino assembly so that it's less low at the bottom of its travel


Happy Button Pressing!