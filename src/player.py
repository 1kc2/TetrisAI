from board import Direction, Rotation
from random import Random
from exceptions import NoBlockException


class Player:
    def choose_action(self, board):
        raise NotImplementedError


class RandomPlayer(Player):
    def __init__(self, seed=None):
        self.random = Random(seed)

    def choose_action(self, board):
        return self.random.choice([
            Direction.Left,
            Direction.Right,
            Direction.Down,
            Rotation.Anticlockwise,
            Rotation.Clockwise,
        ])


class AutoPlayer(Player):
    def __init__(self, seed=None):
        self.best_pos = 0
        self.best_rot = 0

    def height(self, board):
        '''
        gets the height of each column and adds them to a list
        '''
        heights = []
        for x in range (board.width):
            for y in range (board.height):
                if (x,y) in board.cells:
                    heights.append(board.height  - y)
                    break
                elif y == 23:
                    heights.append(0)
        return heights

    def cleared_lines(self, old_score, board):
        new_score = board.score
        difference = new_score - old_score
        if 100 < difference < 125:
            return 1
        elif 400 < difference < 425:
            return 2
        elif 800 < difference < 825:
            return 3
        elif 1600 < difference < 1625:
            return 4
        else:
            return 0

    def check_holes(self, board):
        '''
        counts the number of holes on the board. A hole is an empty cell which has an occupied cell above it.
        '''    
        number_of_holes = 0
        for y in range(board.height):
            for x in range(board.width):
                if (x, y) not in board.cells and (x,(y - 1)) in board.cells:
                    number_of_holes += 1
        return number_of_holes

    def smoothness(self, heights):
        '''
        compares heights of columns
        '''
        smoothness = 0
        for x in range (len(heights)-1):
            smoothness += abs(heights[x]-heights[x+1])
        return smoothness

    def best_move(self, board):
        self.best_score = float('-inf')
        '''
        test all possible moves
        '''
        try:
            for rotations in range (4):
                for pos in range (-5,5):
                    clone = board.clone()
                    old_score = clone.score
                    for _ in range (rotations):
                        clone.rotate(Rotation.Clockwise)
                    if pos > 0:
                        for _ in range (abs(pos)):
                            clone.move(Direction.Right)
                    elif pos < 0:
                        for _ in range (abs(pos)):
                            clone.move(Direction.Left)
                    clone.move(Direction.Drop)

                    '''
                    collate all the heuristics
                    '''
                    heights = self.height(clone)
                    total_heights = sum(heights)
                    smoothness = self.smoothness(heights)
                    num_holes = self.check_holes(clone)
                    completed_lines = self.cleared_lines(old_score, clone)

                    '''
                    create scores for all heuristics and a total overall score for each move
                    '''
                    smoothness_score = smoothness * -0.184483
                    height_score = total_heights * -0.510066
                    completed_lines_score = completed_lines * 0.760666
                    holes_score = num_holes * -0.35663

                    score = (smoothness_score + height_score + completed_lines_score + holes_score)

                    '''
                    best score dictates which move is chosen
                    '''
                    if score > self.best_score:
                        self.best_score = score
                        self.best_pos = pos
                        self.best_rot = rotations
        except:
            pass

    def choose_action(self, board):
        move = []
        self.best_move(board)
        for _ in range (self.best_rot):
            move.append(Rotation.Clockwise)
        if self.best_pos > 0:
            for _ in range (abs(self.best_pos)):
                    move.append(Direction.Right)
        elif self.best_pos < 0:
            for _ in range (abs(self.best_pos)):
                    move.append(Direction.Left)
        move.append(Direction.Drop)
        return move


SelectedPlayer = AutoPlayer
