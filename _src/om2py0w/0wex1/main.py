#-*- coding: utf-8 -*- 
import time
from sys import exit

my_diary = open('diary.txt', 'a+')
while True:
	print "Previous record:"
	my_diary.seek(0)
	print my_diary.read()
	line = raw_input(">")
	if line == 'q': break
	my_diary.write(line+'\n')
