Raspberry-Pi-PiGlow-project
===========================

This is a little project that allows you to control the LEDs on your PiGlow LED board attached to the RaspberryPi via a webUI.

It consists of little bit of PHP, CSS and some Python to do the actual lightshow. 

TODO:
Implement a python script(network.py) to display the network load in a sensible way. scan ethernet port(eth0) for traffic and display them in the following way:
green LED for bandwith >= 0 && <= 199 kb/s
orange LED for bandwith >=  200 && <= 599 kb/s (?)
red LED for >= 600 kb/s? 
