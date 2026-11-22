import threading
import time
import turtle
import random
import math
from enum import Enum

class CellType(Enum):
    NORMAL = 1
    HEAD = 2
    BODY = 3
    FRUIT = 4
    OBSTACLE = 5

class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

class Snake():
    def __init__(self, length, pos, width, height, direction):
        self.length = length
        self.pos = pos
        self.width = width
        self.height = height
        self.direction = direction

    def get_head_pos(self):
        head =  self.get_pos()[0]
        return (head[0], head[1])

    def increase_length(self):
        self.length += 1

    def get_length(self):
        return self.length

    def get_pos(self):
        return self.pos

    def head_at(self, loc):
        """
        check if head is at given loc
        :param loc:
        :return:
        """

        return self.pos[0] == loc

    def change_direction(self, new_direction):
        invalids = [[Direction.LEFT, Direction.RIGHT], [Direction.UP, Direction.DOWN], [Direction.RIGHT, Direction.LEFT], [Direction.DOWN, Direction.UP]]
       #print(f'move {self.direction=}')
        if self.direction != new_direction and [self.direction, new_direction] not in invalids and [new_direction, self.direction] not in invalids:
            self.direction = new_direction
        #print(f'changed {self.direction=}')

    def contain(self, x, y):
        return [y,x] in self.get_pos()

    def _move_or_increase(self, increase=False):
        """
        1. delete last pos
        2. calaculate new pos using direction (x,y)
        3. append (x,y) to front of pos
        :return:
        """
        if not increase:
            self.pos = self.pos[:-1]
        first = self.pos[0]

        if self.direction == Direction.RIGHT:
            newPos = [first[0], (first[1] + 1) % self.width]
        elif self.direction == Direction.UP:
            newPos = [(first[0] + 1) % self.height, first[1]]
        elif self.direction == Direction.LEFT:
            newPos = [first[0], (first[1] - 1) % self.width]
        elif self.direction == Direction.DOWN:
            newPos = [(first[0] - 1) % self.height, first[1]]

        self.pos = [newPos] + self.pos

    def move(self):
        self._move_or_increase(increase=False)

    def increase(self):
        self._move_or_increase(increase=True)



class Board():

    def __init__(self, screen, height, width):
        self.height = height
        self.width = width
        self.screen = screen
        self.screen.setworldcoordinates(0, 0, self.screen.window_width() , screen.window_height())
        self.reset_state()

    def reset_state(self):
        self.state = [[CellType.NORMAL for x in range(self.height)] for x in range(self.width)]

    def square(self, colour, size):
        turtle.color(colour)
        turtle.begin_fill()
        for x in range(4):
            turtle.forward(size)
            turtle.right(90)
        turtle.end_fill()

    def draw(self):
        turtle.tracer(0, 0)
        turtle.speed(0)
        turtle.hideturtle()
        turtle.penup()
        turtle.reset()

        screen_w, screen_h = self.screen.screensize()
        square_size = screen_w / self.width

        start_x = 0
        start_y = square_size

        colours = ('cornsilk', 'burlywood')

        for y in range(self.height):
            turtle.setpos(start_x, start_y + y * square_size)
            turtle.setheading(0)

            for x in range(self.width):
                turtle.pendown()
                colour = colours[(x + y) % 2]
                if self.state[x][y] == CellType.HEAD:
                    colour = 'deeppink'

                if self.state[x][y] == CellType.BODY:
                    colour = 'lightpink'

                if self.state[x][y] == CellType.FRUIT:
                    colour = 'red'

                if self.state[x][y] == CellType.OBSTACLE:
                    colour = 'blue'
                self.square(colour, square_size)
                turtle.penup()
                turtle.forward(square_size)
        turtle.color('Black')
        turtle.goto(100,100)

        turtle.update()

    def change_cell_type(self, x, y, type):

        self.state[y][x] = type

class Score():
    def __init__(self, score):
        self.score = score

    def increase_score(self):
        self.score += 10

    def get_score(self):
        return self.score

class Obstacle():
    def __init__(self, snake, board):

        def get_next(prev):
            x = prev[0]
            y = prev[1]
            directions = ['l', 'r', 'u', 'd']

            direction = random.choice(directions)
            if direction == 'l':
                x -=1
            elif direction == 'r':
                x +=1
            elif direction == 'u':
                y +=1
            else:
                y -=1

            return [x, y]

        number = random.randint(1, 5)
        directions = ['l', 'r', 'u', 'd']

        x = random.randint(1, board.width-1)
        y = random.randint(1, board.height-1)

        while snake.contain(x, y):
            x = random.randint(1, board.width - 1)
            y = random.randint(1, board.height - 1)

        positions = [[x, y]]

        for _ in range(number):
            new_pos = get_next(positions[-1])
            while snake.contain(new_pos[0], new_pos[1]):
                new_pos = get_next(positions[-1])

            positions.append(new_pos)

        self.pos = positions


    def get_pos(self):
        return self.pos

    def contain(self, x, y):
        for position in self.pos:
            if position[0] == y and position[1] == x:
                return True
        return False

class Fruit():
    def __init__(self, snake, board):
        x = random.randint(1, board.width - 1)
        y = random.randint(1, board.height - 1)

        while snake.contain(x, y):
            x = random.randint(1, board.width - 1)
            y = random.randint(1, board.height - 1)

        self.x = x
        self.y = y

    def get_pos(self):
        return [self.x, self.y]








class Game():
    def __init__(self, board, snake, screen, score):
        self.board = board
        self.snake = snake
        self.screen = screen
        self.score = score




    def draw(self):
        snake_pos = self.snake.get_pos()

        self.board.change_cell_type(snake_pos[0][0], snake_pos[0][1], CellType.HEAD)
        for pos in snake_pos[1:]:
            self.board.change_cell_type(pos[0], pos[1], CellType.BODY)

        x, y = self.fruit.get_pos()
        self.board.change_cell_type(y, x, CellType.FRUIT)


        obstacle_positions = self.obstacle.get_pos()
        for obstacle in obstacle_positions:
            self.board.change_cell_type(obstacle[1], obstacle[0], CellType.OBSTACLE)

        self.board.draw()




    def create_obstacle(self):
        self.obstacle = Obstacle(self.snake, self.board)



    def create_fruit(self):
        self.fruit = Fruit(self.snake, self.board)



    def play(self):
        def move_down():
            self.snake.change_direction(Direction.DOWN)

        def move_left():
            self.snake.change_direction(Direction.LEFT)

        def move_right():
            self.snake.change_direction(Direction.RIGHT)

        screen.listen()
        screen.onkeypress(lambda: self.snake.change_direction(Direction.UP), "w")
        screen.onkeypress(move_down, "s")
        screen.onkeypress(move_left, "a")
        screen.onkeypress(move_right, "d")

        self.create_fruit()
        self.create_obstacle()

        while True:

            self.board.reset_state()
            if self.obstacle.contain(*self.snake.get_head_pos()):
                print('poisoned')
                turtle.write("POISONED".format(self.score.get_score()), font=("Arial", 100, "normal"))
                break


            if self.snake.head_at(self.fruit.get_pos()[::-1]):
                self.create_fruit()
                self.create_obstacle()
                self.snake.increase()
                self.score.increase_score()
                print(self.score.get_score())


            else:
                self.snake.move()


            positions = self.snake.get_pos()

            for x in positions[1:]:

                if self.snake.head_at(x):
                    print('YOU LOSEEE')
                    turtle.write("YOU LOSEE".format(self.score.get_score()), font=("Arial", 200, "normal"))
                    break

            self.draw()

            turtle.setpos(0, 0)

            turtle.write("Score: {}".format(self.score.get_score()), font=("Arial", 20, "normal"))


            time.sleep(0.00005)




turtle.setup(width=750, height=500)
screen = turtle.Screen()

myBoard = Board(screen=turtle.Screen(), height=20, width=30)
turtle.hideturtle()
mySnake = Snake(2, [[10, 10], [10, 11]], width=30, height=20, direction=Direction.UP)
myScore = Score(0)
myGame = Game(myBoard, mySnake, screen, myScore)

mySnake.move()
myGame.play()


















turtle.done()



