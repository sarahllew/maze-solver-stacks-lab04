'''contains the solveMaze function'''
from Stack import Stack

def solveMaze(maze, startX, startY):
    '''
    - maze: 2D list maze
    - startX and startY: starting coordinates { maze[startX][startY] }
    - assume this is a valid position, no + or G value exists in that position
    - function utilizes a Stack and updates the maze elements with number of steps at each position
    - returns True if the path exists and the goal was reached
    - returns False if the no path exists to goal
    '''
    s = Stack()
    coordinates = (startX, startY)
    s.push(coordinates)
    step = 1 
    maze[startX][startY] = step 
    
    while s.isEmpty() == False:
        startX, startY = s.peek()

        if maze[startX][startY] == 'G':
            return True
        if maze[startX-1][startY] == 'G':
            return True
        if startX-1 >= 0 and maze[startX-1][startY] == ' ' or maze[startX-1][startY] == 'G': # checking north 
            step += 1
            maze[startX-1][startY] = step
            coordinates = (startX-1,startY)
            s.push(coordinates)
            continue
        if maze[startX][startY-1] == 'G':
            return True
        if startY-1 >= 0 and maze[startX][startY-1] == ' ' or maze[startX][startY-1] == 'G':  # checking west
            step += 1
            maze[startX][startY-1] = step
            coordinates = (startX, startY-1)
            s.push(coordinates)
            continue
        if maze[startX+1][startY] == 'G':
            return True
        if maze[startX+1][startY] == ' ' or maze[startX+1][startY] == 'G':  # checking south
            step += 1
            maze[startX+1][startY] = step
            coordinates = (startX+1, startY)
            s.push(coordinates)
            continue
        if maze[startX][startY+1] == 'G':
            return True
        if maze[startX][startY+1] == ' ' or maze[startX][startY+1] == 'G': # checking east
            step += 1
            maze[startX][startY+1] = step
            coordinates = (startX, startY+1)
            s.push(coordinates)
            continue
        s.pop()
        
    return False        
          

def printMaze(maze):
	for row in range(len(maze)):
		for col in range(len(maze[0])):
			print("|{:<2}".format(maze[row][col]), sep='',end='')
		print("|")
	return

##maze = [
##['+','+','+','+','G','+'],
##['+',' ','+',' ',' ','+'],
##['+',' ',' ',' ','+','+'],
##['+',' ','+','+',' ','+'],
##['+',' ',' ',' ',' ','+'],
##['+','+','+','+','+','+'] ]
##print(solveMaze(maze,4,4))
##
##printMaze(maze)
##
##maze1 = [
##['+','+','G','+'],
##['+','+',' ','+'],
##['+',' ','+','+'],
##['+',' ','+','+'],
##['+',' ',' ','+'],
##['+',' ',' ','+'],
##['+',' ',' ','+'],
##['+',' ',' ','+'],
##['+',' ',' ','+'],
##['+','+','+','+'] ]
##print(solveMaze(maze1,8,2))
##printMaze(maze1)

    

