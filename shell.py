from cmd import Cmd
import os

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

	def do_dir(self, args):
		"""Names files and directories in current directory"""
		path = "."

		if len(args) == 0:
			path = "."
		else:
			path = args
		
		files = os.listdir(path)
		for name in files:
			print(name)

	def do_cd(self, args):
		"""Changes the current directory"""
		if len(args) == 0:
			print(os.getcwd())
		else:	
			path = args	
			os.chdir(path)

	def do_clr(self, args):
		"""Clears the screen"""
		print("\033c")

	def do_environ(self, args):
		print(os.environ["HOME"])

	def do_echo(self, args):
		print("DAB")
	def do_pause(self, args):
		input()


if __name__ == '__main__':
	prompt = MyPrompt()
	prompt.prompt = '>'
	prompt.cmdloop("Starting prompt...")