sudo apt -y purge python2.7-minimal

sudo apt-get update
sudo apt-get upgrade

sudo apt-get install -y python-smbus
sudo apt-get install -y i2c-tools

sudo raspi-config

sudo apt-get -y  install python3-pip 
sudo pip3 install --upgrade setuptools
pip3 install RPI.GPIO
pip3 install adafruit-pureio
pip3 install adafruit-blinka
python3 blinkatest.py

sudo pip3 install adafruit-circuitpython-motorkit
