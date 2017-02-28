import os
from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice
from com.android.monkeyrunner import MonkeyImage
from com.android.monkeyrunner import By

class MyMonkeyRunner:
	def getDevice(self):
		dev = MonkeyRunner.waitForConnection()
		return dev


if __name__ == "__main__":
	mmr = MyMonkeyRunner()	
