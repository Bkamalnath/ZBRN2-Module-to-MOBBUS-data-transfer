# ZBRN2-Module-to-MOBBUS-data-transfer
Step 1: power the module with 24VDC or single phase AC supply.
		{ It will take few seconds to switch and to get ready position in display. When it is ready it will display as “rdy” in lcd screen.}

Step 2: press the rotating button for once then “config” will display. Again press the same button. Then it will show haw many devices are connected.

Step 3: Then you need to press again to show to which slot or number the new device to connect. Or if new modify the already configured device then select the number by rotation the button and press to go for its properties of already configured push button or switch.

Step 4: For configuring new device then select new free slot in the module and it will display “E” then press button in the module and select the type  transmitter[in our case type 05] and then press push button three times to pair with the module. After parring double click the button in the module to come back. Double click the button in the module untill you reach home position till it display “rdy” in lcd screen.

Alter:
	when “E” is dislpayed rotate the button in module and select the type  transmitter[in our case type 05] and then it will display “Id” in lcd screen then press again button in the module and enter the id of the push button by rotating and click the button in the module. Then return to home position by double clicking untill it displays “rdy” in the lcd display.

{ After configuring and pairing the push button with module check if the led in the top of module glows while the button is pressed for once. The led glows in green colour if the signal is high else it glow in orange color if the singal is low and the led will not glow if the push button signal is out of reach or not pressed.}

Step 5: Press the button in the module and after clicking on “config” then rotate the button to reach “sl” to set baud rate.
Step 6: Connect the ethernet cable(RJ45) in anyone of ethernet port in module and connect other end [usb type  data pins D0,D1 blue and white with blue respectively ] to your computer or controller and use modbus library file in python code to get data from this module.
