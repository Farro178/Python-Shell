from cmd import Cmd
import os
import sys

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
		try:
			path = "."
			if len(args) == 0:
				path = "."
			else:
				path = args
				
			files = os.listdir(path)
			for name in files:
				print(name)
		except NotADirectoryError:
			print("Error: This is not a directory: " + path)
		except FileNotFoundError:
			print("Error: File or Directory not found: " + path)



	def do_cd(self, args):
		"""Changes the current directory"""
		try:
			if len(args) == 0:
				print(os.getcwd())
			else:   
				path = args 
				os.chdir(path)
				prompt.prompt = "~" + os.getcwd() + ": >" 
		except NotADirectoryError:
			print("Error: This is not a directory: " + path)
		except FileNotFoundError:
			print("Error: File or Directory not found: " + path)

	def do_clr(self, args):
		"""Clears the screen"""
		print("\033c")

	def do_environ(self, args):
		"""should print out the same as the env command"""
		for key in os.environ.keys():
			print("{} : {}".format(key, os.environ[key]) + "\n")


	def do_echo(self, args):
		"""Echoes the arguement."""
		words = args.split()
		new_word = ""
		for word in words:
			new_word = new_word + " " + word
		print(new_word[1:])

	def do_pause(self, args):
		input("Program is paused, press enter to continue.")

	def do_help(self, args):
		print("poop")


if __name__ == '__main__':
	prompt = MyPrompt()
	prompt.prompt = "~" + os.getcwd() + "/myshell: >"
	if len(sys.argv) == 2:
		with open(sys.argv[1], "r") as f:
			lines = f.readlines()
		for line in lines:
			line = line.strip("\n")
			print(line)
			MyPrompt().onecmd(line)
	else:
		prompt.cmdloop("Starting prompt")