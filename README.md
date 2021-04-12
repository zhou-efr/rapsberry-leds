# raspberry-leds

## General Purpose Input Output
We'll use only the pin ground for the common ground of leds strip and a GPIO pin (for the beginning the 18th one)<br/>
<img src="https://www.framboise314.fr/wp-content/uploads/2018/02/kit_composants_GPIO_01.png" alt="raspberry io scheme" width="500"/>

### GPIO with python
To interact with the GPIO of the raspberry it's usual to use the *GPIO Zero* library offer by python.

[basic tutorial](https://www.raspberrypi.org/documentation/usage/gpio/python/README.md) <br/>
[gpiozero documentation](https://gpiozero.readthedocs.io/en/stable/)

However, we use WS2811 LEDs controller then we'll use the library *Adafruit CircuitPython NeoPixel* 

[adafruit CircuitPython neopixel documentation](https://circuitpython.readthedocs.io/projects/neopixel/en/latest/) <br/>
[link to the used LEDs](https://fr.aliexpress.com/item/32862966303.html?spm=a2g0s.9042311.0.0.12936c373rwYV7)

Then to use a LED strip with a raspberry we wire the strip to an external source of current (if your strip is short and 
in 5V you can wire it directly to the raspberry). Then we wire the ground of the LED strip to the ground of the 
raspberry and the data output to a GPIO pin of the raspberry (see below) <br/> 
<img src="https://tutorials-raspberrypi.de/wp-content/uploads/Raspberry-Pi-WS2812-Steckplatine-600x361.png" alt="raspberry io scheme" width="500"/> 

[source](https://raspberrypi-tutorials.fr/connectez-et-controlez-bandes-led-ws2812-rgb-via-raspberry-pi/)

# Installation
First you must install some packages :

`sudo apt-get install gcc make build-essential python-dev git scons swig`

then you can clone this repository

`git clone https://github.com/zhou-efr/rapsberry-leds.git`

don't forget to install *Adafruit CircuitPython NeoPixel* 

`sudo pip3 install adafruit-circuitpython-neopixel`

then you're ready to code. Launch the code through a IDE or with the terminal 

`sudo python3 main.py`