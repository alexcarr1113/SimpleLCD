# SimpleLCD by Alex Carr - https://github.com/alexcarr1113
 An extension to Denis Pleic's I2C LCD library with the goal of being completely plug and play.

 First Time Setup:

	Open terminal inside of this directory then run 'sudo ./setup_i2c.sh'. This will enable I2C and install required tools

 Usage:

	Import simplelcd.py to your script then create an lcd object using 'lcdname = simplelcd.lcd()'
	This will run the auto address detection
	
	Essential methods:
	
	lcdname.write(string, int)
	lcdname.writepos(string, int, int)
	lcdname.backlight(int)
	lcdname.clear()
	
	Other methods are available to use as standard with the RPi_I2C_driver, linked below


Setup I2C Script taken from WittyPi software installation
RPi_I2C_driver created by Denis Pleic - https://gist.github.com/DenisFromHR