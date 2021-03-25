#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String
import pymodbus
from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from pymodbus.register_read_message import ReadHoldingRegistersResponse
from time import sleep
import datetime
import requests
import json
modbus = ModbusClient(method='rtu', port='/dev/ttyUSB0', baudrate=19200, parity = 'N', timeout=1)
modbus.connect()
sleep(1)

def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(60) # 10hz
    #r = modbus.read_holding_registers(0x0000, unit =1)
    while not rospy.is_shutdown():
	    time = str(datetime.datetime.now())
	    r = modbus.read_holding_registers(0x0000, unit =1)
	    print(r.registers)
	    if r.registers[0]==0:
		station = "waiting for input"
		#pub.publish(station)
	    elif r.registers[0]==1:
	 	station1 = "call from station 1"
		pub.publish(station1)
	    elif r.registers[0]==2:
		station2 = "call from station 2"
		pub.publish(station2)
	    elif r.registers[0]==3:
		station3 = "warning multiple switch pressed"
		pub.publish(station3)
	    elif r.registers[0]==4:
		station4 = "call from station 3"
		pub.publish(station4)
	    elif r.registers[0]==5:
		station5 = "warning multiple switch pressed"
		pub.publish(station5)
 	    elif r.registers[0]==6:
		station6 = "warning multiple switch pressed"
		pub.publish(station6)
	    elif r.registers[0]==7:
		station7 = "warning multiple switch pressed"
		pub.publish(station7)
	    sleep(0.4)

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

