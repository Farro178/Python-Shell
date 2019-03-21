from cmd import Cmd
import os, sys
class MyPrompt(Cmd):
	
	def do_hello(self, args): 
		"""Says hello. If you provide a name, it will greet you with it."""
		if len(args) == 0:
			name = "stranger"
		else:
			name = args
		print ("Hello, " + name)


	def do_quit(self, args):
		"""Quits the program."""
		print ("Quitting")
		raise SystemExit

	def do_ls(self, args):
		"""Names files and directories in current directory"""
		path = "."
		if len(sys.argv) == 2:
			path = sys.argv[1]

		files = os.listdir(path)
		for name in files:
			print(name)
	
	def do_cd(self, args):
		"""Changes the current directory"""
		if len(args) == 2:
			path = args		
		os.getcwd(path)


if __name__ == '__main__':
	prompt = MyPrompt()
	prompt.prompt = '>'
	prompt.cmdloop("Starting prompt...")