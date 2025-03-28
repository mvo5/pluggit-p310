# Trivial CLI app to display pluggit P310 status

Display some stats about the ventilation unit P310. The
unit needs to be connected to the network.

Example output:
```
$ pluggit-p310
# Pluggit info
Mode of operaton: demand mode
Current date/time: 2019-03-01 15:22:43
Speed level of fans: 1 
VOC sensor value: 454 ppm
RH relative humidity sensor value: 43 %
Remaining filter lifetime: 240  days
Number of the Active Week Program (for Week Program mode): 10 
Work time of system: 249 days
Outside air: 10.9 C
Supply temp: 19.9 C
Extract temp: 21.6 C
Exhaust temp: 12.6 C
```

## How to install

On Ubuntu/Debian just run:

```
$ sudo apt install -y python3-pymodbus
```

With that all dependencies are installed.

## Hacking

Run unit tests with:
```
$ python3 -m unittest
```


## TODO
 * top-like display
 * add argparse
 * display more regs
 * auto-detect IP of the unit
 * provide a mode to connect via usb serial port
 * add write settings (like switching to manual mode)

