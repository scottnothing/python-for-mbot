#!/usr/bin/env python

from lib.mBot import *
if __name__ == '__main__':
	def onDistance(dist):
		print "distance:",dist
		if dist<20 :
			bot.doMove(-100,-100)
			sleep(0.5)
			bot.doMove(100,-100)
			sleep(0.1)
		bot.doMove(100,100)

	bot = mBot()
	#bot.startWithSerial("/dev/ttyUSB0")
	bot.startWithHID()
	while(1):
		try:
			bot.requestUltrasonicSensor(1,1,onDistance)
		except Exception,ex:
			print str(ex)
		sleep(0.2)