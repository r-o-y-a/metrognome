Metrognome is a simple visual metronome.

Instructions for OSX:
- Requirements: SuperCollider, Python, router or phone with wifi hospot for connection by mobile devices
- Connect to hotspot from computer
- In Terminal, run ifconfig to get the router/hotspot ip address
- Edit server.py "network_ip" variable and index.html "socket" variable to match the ip address (keep all port numbers the same)
- Run python3 server.py to start the web server
- Connect to http://172.20.10.2:8080/ (you should see just a blank page, no error)
- Run metrognome.scd to start the metronome

Configuration:
- Change the BPM in metrognome.scd
- Change the number counting in index.html
