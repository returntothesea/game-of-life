import random

print("running")

HEIGHT = 5
WIDTH = 5
RANDOM_THRESHOLD = 0.5

def create_dead_state (height, width):
	print("height is " + str(height))
	print("width is " + str(width))
	arr = [[0] * height for i in range(width)]
	return arr

def create_random_state (height, width):
	state = create_dead_state(height, width)

	# TODO: randomize each element of 'state' to 0 or 1

	for x in range(height):
		for y in range(width):
			random_number = random.random()
			if random_number >= RANDOM_THRESHOLD:
				state[x][y] = 1

	return state

def render (state):
	print(state)


r = create_random_state(HEIGHT, WIDTH)

render(r)