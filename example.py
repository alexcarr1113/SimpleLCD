import simplelcd
from time import sleep

mylcd = simplelcd.lcd() #auto detect address and create lcd object

mylcd.write("Hello World!") #write to default line (1)
sleep(2)
mylcd.write("Good morning", 2) #write to line two
sleep(3)
mylcd.clear() #clear display
sleep(1)
mylcd.writepos("Hello", 2, 4) #write to row 2, column 4
sleep(3)
mylcd.clear() #clear display
mylcd.backlight(0) #turn off backlight - good for when idle
