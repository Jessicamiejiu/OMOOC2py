# _*_ coding: utf-8 _*_
from bottle import route, get, post, request,run,template,debug
import sys
from time import localtime, strftime

def read_my_diary():
	f = open('diary.txt', 'a+')
	f.seek(0)
	return f.read()
	f.close()

def write_new_diary(newdiary):
	f = open ('diary.txt', 'a+')
	edit_time = strftime("%Y %b %d %H: %M:%S", localtime())
	f.write('%s  %s\n' %(edit_time, newdiary))
	f.close()

@route('/diary')
def browse():
	file = read_my_diary()
	return template('diaryweb', diarylog=file)
    

@route('/diary', method='POST')
def newDiary():
    newdiary = request.POST.get('newdiary')
    write_new_diary(newdiary)
    print "Typing:", newdiary
    file = read_my_diary()
    return template("diaryweb", diarylog = file)

if __name__ == '__main__':
	run(host='localhost', port=8080, debug=True, reloader=True)
