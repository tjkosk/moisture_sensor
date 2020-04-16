from serial import *

def queryArduino(ser):
  ser.write(b'1')
  line  = ser.readline().decode('utf-8').rstrip()
  line  = int(line,16)
  line = line + 4
  return line

def openSerial():
  port = '/dev/ttyUSB0'
  ser = Serial(port,9600)
  return ser
