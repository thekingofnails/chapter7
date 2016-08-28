import os

def run(**args)
	
	print "[*] In dirlister mode"
	files = os.listdir(".")
	return str(files)

