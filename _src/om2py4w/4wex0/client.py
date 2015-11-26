# -*- coding: utf-8 -*-
from bottle import*
import requests
import sys

	
def input_diary():
	print " Pls add your diary here."
	data = raw_input('>')
	if data:
		requests.post('http://localhost:8080/diary', data={'newdiary':data})

def print_history():
	r = requests.get('http://localhost:8080/diary')
	return r.text
		
def main():
	r = request.get('http://localhost:8080/diary')
	input_diary()
	print print_history()
		
if __name__=="__main__":
	main()
	
