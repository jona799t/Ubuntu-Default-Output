# Ubuntu Default Output
A Python script which selects a desired output device on startup

# Configuration
To start run this command in the terminal: ``pactl list short sinks`` and find the device name of the desired output  
Open defaultOutput.py and change ``output = "..."`` to your device name  
Move defaultOutput.py to /bin/ with the following command ``sudo mv defaultOutput.py /bin/``  
Configure the following command to run on startup: ``python3 /bin/defaultOutput.py``
