#!/usr/bin/env python
#O robo deve entrar por uma porta, se mover ate o ponto designado
#ser inspecionado, e sair por outra porta.

#1 - O avaliador vai surgir em frente ao robo que deve evitar a #colisao.
#2 - Sera avaliada a voz do robo.
#3 - Devera reconhecer um codigo QR para continuar depois que #parar.
import rospy
from pocketsphinx import LiveSpeech
from std_msgs.msg import String

def entrada():
	entrada = rospy.Publisher("entrada",String,queue_size=1)#mudei o tamanho da fila
	controle = rospy.Publisher("controle",String,queue_size=1)#mudei o tamanho da fila
	rospy.init_node('comandos',anonymous=True)
	rate = rospy.Rate(1) #Taxa de 1Hz(1 vez por segundo)
	while not rospy.is_shutdown():
		for phrase in LiveSpeech():
			com = phrase
			hello_str = str(com)
			rospy.loginfo(hello_str)
			entrada.publish(str(com))
			controle.publish(str(com))
			rate.sleep()
if __name__ == '__main__':
	try:
		entrada()
	except rospy.ROSInterruptException:
		pass
