'''
Polymorphism
Sources:
http://blog.thedigitalcatonline.com/blog/2014/08/21/python-3-oop-part-4-polymorphism/
'''
import sys
print sys.version # Python version
a = 9
print(a)
print type(a) 	# Data type of a
print id(a)  	# Address of a

class Data_wrapper:
	def __init__(self,data):
		self.data = data
	def disp(self):
		self.data.disp()

class Number:
	def __init__(self,val):
		self.val = val
	def disp(self):
		print "data",self.val,"is a number"
		print "val + 1 = ", self.val+1

class String_number:
	def __init__(self,val):
		self.val = val
	def disp(self):
		print "data",self.val,"is a string"
		print "val + 1 = ", int(self.val)+1

x = Number(3)
y = String_number(3)
wx = Data_wrapper(x)
wy = Data_wrapper(y)
wx.disp()
wy.disp()
