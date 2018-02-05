#!/usr/bin/env python
import rospy
import pyttsx
from std_msgs.msg import String
from pyfirmata import Arduino, util
#board = Arduino('/dev/ttyACM0')
def callback(data):
	rospy.loginfo("I heard:  %s", data.data)
	engine = pyttsx.init()
	engine.runAndWait()
	rec = str(data.data)
	if rec == 'forward' or rec == 'four':
		engine.say("start walking")
		engine.runAndWait()
		#board.digital[7].write(1)
		#board.digital[8].write(0)
	elif rec == 'stop' or rec == 'wait':
		engine.say("stopping")
		engine.runAndWait()
		#board.digital[7].write(0)
		#board.digital[8].write(0)
	else:
		engine.say("command unrecognized")
		engine.runAndWait()
def listener():

	# No ROS os nos sao nomeados unicamente. Se dois nos com o mesmo
	# nome sao lancados, o anterior e encerrado. A flag anonymous=True
	# significaque o rospy vai escolher um nome unico para nosso 
	# no 'listener' para que multiplos listeners possam rodar simultaneamente.

	rospy.init_node('confirma', anonymous=True)
	rospy.Subscriber("entrada", String, callback)

	# O spin() evita que o python seja encerrado ate que o no seja interrompido
	
	rospy.spin()

if __name__ == '__main__':
	listener()
