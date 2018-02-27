class SnakeGame(object):

    def __init__(self, width, height, food):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        :type width: int
        :type height: int
        :type food: List[List[int]]
        """

        self.width = width
        self.height = height
        self.food = food
        self.snake = [[0, 0]]
        self.score = 0


    def move(self, direction):
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down
        @return The game's score after the move. Return -1 if game over.
        Game over when snake crosses the screen boundary or bites its body.
        :type direction: str
        :rtype: int
        """

        x, y = self.snake[-1]
        if direction == "U":
            x -= 1
        elif direction == "L":
            y -= 1
        elif direction == "R":
            y += 1
        elif direction == "D":
            x += 1
        print(x, y)
        return self.count(x, y)

    def count(self, x, y):
        if x < 0 or x >= self.height or y < 0 or y >= self.width or [x, y] in self.snake[1:]:
            __import__('pdb').set_trace()
            return -1

        if self.food and x == self.food[0][0] and y == self.food[0][1]:
            self.food.pop(0) #eat food, length increases by 1
            self.score += 1
        else:
            self.snake.pop(0) # length remain the same
        self.snake.append([x, y])
        return self.score

if __name__ == "__main__":
    obj = SnakeGame(3, 3, [[2,0], [0,0], [0,2], [2,2]])
    __import__('pprint').pprint(obj.move("D"))
    __import__('pprint').pprint(obj.move("D"))
    __import__('pprint').pprint(obj.move("R"))
    __import__('pprint').pprint(obj.move("U"))
    __import__('pprint').pprint(obj.move("U"))
    __import__('pprint').pprint(obj.move("L"))
    __import__('pprint').pprint(obj.move("D"))
    __import__('pprint').pprint(obj.move("R"))
    __import__('pprint').pprint(obj.move("R"))
    __import__('pprint').pprint(obj.move("U"))
    __import__('pprint').pprint(obj.move("L"))
    __import__('pprint').pprint(obj.move("D"))
