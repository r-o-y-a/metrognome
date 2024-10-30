Metrognome is a simple visual metronome to sync multiple people in the same room.

It uses a host computer that runs SuperCollider and Python, and mobile devices view it through the web.


Instructions for OSX:
- Requirements: SuperCollider, Python, router or phone with wifi hospot that devices can connect to
- Connect to hotspot from computer
- In Terminal, run ifconfig to get the router/hotspot ip address
- Edit server.py "network_ip" variable and index.html "socket" variable to match the ip address (keep all port numbers the same)
- Run python3 server.py to start the web server
- Connect to http://your_ip_address:8080/ (you should see just a blank page, no error)
- Run metrognome.scd to start the metronome

Configuration:
- Change the BPM in metrognome.scd
- Change the number counting in index.html
