import serial
import time
ser = serial.Serial('COM3', 9600, timeout=0,parity=serial.PARITY_NONE, rtscts=0)

#ser.write('verbose 0\r\n')
serialcmd = "PC 0\r\n"
ser.write(serialcmd.encode())
#ser.write('PC 0\r\n')
#ser.write('VS 0\r\n')
time.sleep(.1)
#ser.flush()
ser.readline()
ser.readline()