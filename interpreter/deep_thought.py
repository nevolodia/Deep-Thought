# Running interpreter: ./deep_thought.py [FILE]

import sys


def run(commands):
	mem = [0] * 420000
	mem_pointer = 0
	command_pointer = 0
	loop_stack = []

	while command_pointer < len(commands):
		command = commands[command_pointer]
		if command == 0:
			mem[mem_pointer] += 1
		elif command == 1:
			mem[mem_pointer] -= 1
		elif command == 2:
			mem_pointer += 1
		elif command == 3:
			mem_pointer -= 1
		elif command == 4:
			loop_stack.append(command_pointer)
		elif command == 5:
			if mem[mem_pointer] != 0:
				command_pointer = loop_stack[-1]
			else:
				loop_stack.pop()
		elif command == 6:
			print(chr(mem[mem_pointer]), end="")
		command_pointer += 1

	print()


def split_commands(code):

	command_list = [
		'101010',  # inc
		'010101',  # dec
		'000',     # shift right
		'001',     # shift left
		'100',     # loop start
		'111',     # loop end
		'\n',     # print
	]

	commands = []

	command = ""
	for c in code:
		command += c

		if command in command_list:
			commands.append(command_list.index(command))
			command = ""

	return commands


def read_file(filename):
	f = open(filename, "r")
	commands = split_commands(f.read())
	run(commands)
	f.close()


def main():
	if len(sys.argv) == 2:
		read_file(sys.argv[1])
	else:
		print("Should provide a file to interpret")


if __name__ == "__main__":
	main()