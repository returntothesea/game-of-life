import random, os

clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

print("running")

HEIGHT = 20
WIDTH = 40
RANDOM_THRESHOLD = 0.5

def dead_state (height, width):
	print("height is " + str(height))
	print("width is " + str(width))
	arr = [[0] * width for i in range(height)]
	return arr

def random_state (height, width):
	state = dead_state(height, width)

	for x in range(height):
		for y in range(width):
			random_number = random.random()
			if random_number <= RANDOM_THRESHOLD:
				state[x][y] = 1

	return state

def print_line(line):
	string = "|"
	for i in range(len(line)):
		if line[i] == 0:
			string += " "
		if line[i] == 1:
			string += "#"
	string += "|"
	print(string)

def render (state):
	# clear()
	print("-" * (WIDTH + 2))
	for i in range(len(state)):
		print_line(state[i])
	print("-" * (WIDTH + 2))


r = random_state(HEIGHT, WIDTH)

render(r)