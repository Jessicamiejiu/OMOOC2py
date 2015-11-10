#_*_ coding:utf-8 _*_
from Tkinter import *
import tkMessageBox
import pickle

import sys


class App(Frame): #创建一个叫App的类，继承了Tkinter中的Frame
	def __init__(self, master=None): #类App有一个__init__接收self和mater作为参数
		Frame.__init__(self, master) #父类的初始化
		self.pack() #实现布局
		self.createWidgets() #调用创建工具
	
	def write(self):
		target = open('diary.txt','a')
		line = self.Input.get()
		target.write('>\n'+line)
		target.close()
		
	
	
	def read(self):
		target = open('diary.txt', 'r')
		tkMessageBox.showinfo('diary',target.read())
		
	def save(self):
		pickle_file = open('diary.txt','w')
		line = self.Input.get()
		pickle.dump(line,pickle_file)
		
	def createWidgets(self): #定义工具
		
		w1 = Label(self, text ="Input") #输入标签
		w1.pack()	
		
		self.Input= Entry(self)
		self.Input.pack()
		
		b1 = Button(self, text="save",command=self.save)
		b1.pack()
		
		b2 = Button(self, text="read", command=self.read)
		b2.pack()
		
		b3 = Button(self, text="quit", command=self.quit)
		b3.pack()		
		


	
	
App = App() #实例化APP ?不知道为什么要这一步
App.master.title("Diary")
App.mainloop()
	
if __name__ == "__main__":
    main()	
