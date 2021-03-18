n = int(input("Enter number of rows and columns: "))
arr = []
for num in range(n):
	arr.append([])
	for numb in range(n):
		arr[num].append(0)



def game_input():
	feedback = ''
	while feedback != 'X':
		feedback = input('Enter X to exit input, A to make a cell alive and D to make a cell dead: ')
		if feedback == 'A':
			row = int(input('Enter row value of the cell you want to make alive: '))
			column = int(input('Enter column value of the cell you want to make alive: '))
			if row > -1 and row < n and column > -1 and column <n:
				arr[row][column] = 1
			else:
				print("invalid input for row or column")
		elif feedback == 'D':
			row = int(input('Enter row value of the cell you want to kill: '))
			column = int(input('Enter column value of the cell you want to kill: '))
			if row > -1 and row < n and column > -1 and column <n:
				arr[row][column] = 0
			else:
				print("invalid input for row or column")
		elif feedback == 'X':
			print('exiting input......')
		else:
			print('invalid input')



def simulation():
	for row in range(n):
		for col in range(n):
			count = 0
			a = arr[row][col]
			if a == 1:
				if row-1 > -1:
					if arr[row-1][col] == 1:
						count += 1
				if row+1 < n:
					if arr[row+1][col] == 1:
						count += 1
				if col-1>-1:
					if arr[row][col-1] == 1:
						count += 1
				if col+1<n:
					if arr[row][col+1] == 1:
						count += 1
				if col-1>-1 and row-1>-1:
					if arr[row-1][col-1] == 1:
						count += 1
				if col+1<n and row+1<n:
					if arr[row+1][col+1] == 1:
						count += 1
				if col+1<n and row-1>-1:
					if arr[row-1][col+1] == 1:
						count += 1
				if col-1>-1 and row+1<n:
					if arr[row+1][col-1] == 1:
						count += 1
				if count < 2:
					arr[row][col] = 0
				elif count == 2 or count ==3:
					arr[row][col] = 1
				elif count > 3:
					arr[row][col] = 0
			elif a == 0:
				if row-1 > -1:
					if arr[row-1][col] == 1:
						count += 1
				if row+1 < n:
					if arr[row+1][col] == 1:
						count += 1
				if col-1>-1:
					if arr[row][col-1] == 1:
						count += 1
				if col+1<n:
					if arr[row][col+1] == 1:
						count += 1
				if col-1>-1 and row-1>-1:
					if arr[row-1][col-1] == 1:
						count += 1
				if col+1<n and row+1<n:
					if arr[row+1][col+1] == 1:
						count += 1
				if col+1<n and row-1>-1:
					if arr[row-1][col+1] == 1:
						count += 1
				if col-1>-1 and row+1<n:
					if arr[row+1][col-1] == 1:
						count += 1
				if count == 3:
					arr[row][col] = 1
				


game_exit = ''
game_input()
print('Enter E to exit simulation')
print(arr)
while game_exit != 'E':
	simulation()
	print(arr)
	game_exit = input()