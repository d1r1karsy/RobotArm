import pyservos
import sys
from pyservos import Packet
from pyservos import ServoSerial

if len(sys.argv) < 2:
	print('Please give an angle')
	print('Example: {} 150'.format(sys.argv[0]))
	exit(1)

# you will need to CHANGE this to the correct port
port = "/dev/ttyS0"
ID = 1
angle = int(sys.argv[1])

print('Setting servo[{}] to {:.2f} on port {}'.format(ID, angle, port))

try:
	serial = ServoSerial(port=port)
	serial.open()
except Exception as e:
	print(e)
	print('Oops, wrong port')
	print('bye ....')
	exit(1)

if True:
	servo = Packet(pyservos.AX12)
	print('We are talking to an AX12 servo')
else:
	servo = Packet(pyservos.XL320)
	print('We are talking to an XL320 servo')

pkt = servo.makeServoMovePacket(ID, angle)
ans = serial.sendPkt(pkt)  # send packet to servo
ans = servo.processStatusPacket(ans)

if ans:
	print('status: {}'.format(ans))
