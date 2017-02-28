import sys
from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice,MonkeyImage
from com.android.monkeyrunner.easy import EasyMonkeyDevice
from com.android.monkeyrunner.easy import By

class MyMonkeyRunner:
	idSearchStr = 'id/top_view_search'
	idMainBarStr = 'id/main_bar'
	def getDevice(self):
		self.dev = MonkeyRunner.waitForConnection()
		return self.dev
	
	def getEasyDevice(self, dev):
		self.eDevice = EasyMonkeyDevice(dev)
		return self.eDevice

	def getHierarchyViewer(self):
		self.hDevice = self.dev.getHierarchyViewer()
		return self.hDevice
	
	def touchByID(self, id):
		self.eDevice.touch(By.id(id), MonkeyDevice.DOWN_AND_UP)
		

if __name__ == "__main__":
	mmr = MyMonkeyRunner()	

	dev = mmr.getDevice()
	eDev = mmr.getEasyDevice(dev)
	hDev = mmr.getHierarchyViewer()

	#mmr.touchByID(mmr.idSearchStr)
	memView = hDev.findViewById(mmr.idMainBarStr)

	i = 0
	for view in memView:
		print "i = " + str(i)
		print view
		i=i+1
