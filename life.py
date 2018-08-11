import random, os, time

clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

print("running")

HEIGHT = 20
WIDTH = 40
RANDOM_THRESHOLD = 0.5

def dead_state (height, width):
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
	clear()
	print("-" * (WIDTH + 2))
	for i in range(len(state)):
		print_line(state[i])
	print("-" * (WIDTH + 2))

def update_cell(state, x, y):
	neighbors = 0

	if (x - 1 >= 0): # if cell is not on the top edge, check cells above
		if (state[x - 1][y]):
			neighbors += 1
		if (y - 1 >= 0):
			if (state[x - 1][y - 1]):
				neighbors += 1
		if (y + 1 <= (WIDTH - 1)):
			if (state[x - 1][y + 1]):
				neighbors += 1

	if (x + 1 <= (HEIGHT - 1)): # if cell is not on the bottom edge, check cells below
		if (state[x + 1][y]):
			neighbors += 1
		if(y - 1 >= 0):
			if (state[x + 1][y - 1]):
				neighbors += 1
		if(y + 1 <= (WIDTH - 1)):
			if (state[x + 1][y + 1]):
				neighbors += 1

	if (y - 1 >= 0): # if cell is not on the far left, check left cell
		if (state[x][y - 1]):
			neighbors += 1
	if (y + 1 <= WIDTH - 1): # if cell is not on the far right, check right cell
		if (state[x][y + 1]):
			neighbors += 1

	if not (state[x][y]): # if the cell is dead
		if (neighbors == 3):
			return 1
	if (state[x][y]): # if the cell is living
		if (neighbors == 2 or neighbors == 3):
			return 1
	return 0


def next_state(state):
	new_state = dead_state(len(state), len(state[0]))

	for x in range(len(state)):
		for y in range(len(state[0])):
			new_state[x][y] = update_cell(state, x, y)

	return new_state



r = random_state(HEIGHT, WIDTH)

render(r)
r = next_state(r)
render(r)

for x in range(100):
	render(r)
	r = next_state(r)
	time.sleep(.1)