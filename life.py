print("running")

def create_dead_state (height, width):
	print("height is " + str(height))
	print("width is " + str(width))
	arr = [[0] * height for i in range(width)]
	return arr


r = create_dead_state(5, 5)

print(r)