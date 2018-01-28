#!/usr/bin/env python
import rospy
from pyfirmata import Arduino, util
from std_msgs.msg import String

board = Arduino('/dev/ttyACM0')
def callback(data):
	rospy.loginfo("Recebi: %s\n\n", data.data)
	rec = str(data.data)
	if rec == 'forward' or rec == 'four':
		engine.say(str(data.data))
		board.digital[5].write(0)
		board.digital[6].write(1)
		board.digital[7].write(0)
		board.digital[8].write(1)
		board.digital[13].write(1)
	elif rec == 'stop' or rec == 'wait':
		engine.say(str(data.data))
		board.digital[5].write(0)
		board.digital[6].write(0)
		board.digital[7].write(0)
		board.digital[8].write(0)
		board.digital[13].write(0)
def sensor(data):
	dist = str(data.data)#Essa string vai ser recebida pelo arduino que estiver 
	if dist == 'parar':#conectado ao sensor de distancia
		board.digital[5].write(0)
		board.digital[6].write(0)
		board.digital[7].write(0)
		board.digital[8].write(0)
	elif dist == 'direita':
		board.digital[5].write(0)# Para o motor da direita
		board.digital[6].write(0)
		#board.digital[7].write(0)
		#board.digital[8].write(0)
	elif dist == 'esquerda':
		#board.digital[5].write(0)
		#board.digital[6].write(0)
		board.digital[7].write(0)#Para o motor da esquerda
		board.digital[8].write(0)
def portas():
	alvo = str(data.data)
	if alvo == 'parar':
		board.digital[5].write(0)
		board.digital[6].write(0)
		board.digital[7].write(0)
		board.digital[8].write(0)
	elif alvo == 'direita':
		board.digital[5].write(0)# Para o motor da direita
		board.digital[6].write(0)
		#board.digital[7].write(0)
		#board.digital[8].write(0)
	elif alvo == 'esquerda':
		#board.digital[5].write(0)
		#board.digital[6].write(0)
		board.digital[7].write(0)#Para o motor da esquerda
		board.digital[8].write(0)
def kinect():
	ver = str(data.data)#Aqui chega a mensagem do no do kinect
	if ver == 'centro':#Essa funcao usa os motores para ajustar a direcao
		board.digital[5].write(0)#de locomocao do Capek para ele ir em direcao ao 
		board.digital[6].write(1)#alvo.
		board.digital[7].write(0)
		board.digital[8].write(1)
	elif ver == 'direita':
		board.digital[5].write(0)#Para o motor da direita
		board.digital[6].write(0)
		#board.digital[7].write(0)
		#board.digital[8].write(0)
	elif ver == 'esquerda':
		#board.digital[5].write(0)
		#board.digital[6].write(0)
		board.digital[7].write(0)#Para o motor da esquerda
		board.digital[8].write(0)
	if ver == 'parar':
		board.digital[5].write(0)#Para tudo
		board.digital[6].write(0)
		board.digital[7].write(0)
		board.digital[8].write(0)
def listener():
	# No ROS os nos sao nomeados unicamente. Se dois nos com o mesmo
	# nome sao lancados, o anterior e encerrado. A flag anonymous=True
	# significa que o rospy vai escolher um nome unico para nosso 
	# no 'listener' para que multiplos listeners possam rodar simultaneamente.

	rospy.init_node('movimentos', anonymous=True)
	rospy.Subscriber("controle", String,callback)
	rospy.Subscriber("obstaculos",String,sensor)
	rospy.Subscriber("portas",String,portas)
	rospy.Subscriber("alvo",String,kinect)

	# O spin() evita que o python seja encerrado ate que o no seja interrompido
	
	rospy.spin()

if __name__ == '__main__':
	listener()
