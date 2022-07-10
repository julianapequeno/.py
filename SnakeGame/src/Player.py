#Snake class - define player - Snake
from enum import auto
import random

class Snake:
    def __init__(self,x,y):
        self._x = x
        self._y = y

    def update_pos(self,x,y):
        self._x = x
        self._y = y

class Player:
    def __init__(self,rows,cols) -> None:
        self.dim_rows = rows
        self.dim_cols = cols

        self.rastro = []
        self.m_way = []
    
    def update_player(self,rows,cols,assembly_maze,pos_food_x,pos_food_y):
        self.dim_rows = rows
        self.dim_cols = cols
        self.assembly_maze = assembly_maze
        self.pos_food_x = pos_food_x
        self.pos_food_y = pos_food_y

        self.m_way = []
        self.rastro = []
        self.initialize_snake_pos() #reinicializa a posição da cobra
    
    def initialize_arrays(self):
        self.rastro.clear()
        self.m_way.clear()
    
    def initialize_snake_pos(self):
        while(True):
            x = int(random.random()*(self.dim_rows-1))
            y = int(random.random()*(self.dim_cols-1))
            if(self.assembly_maze[x][y] == 1):
                self.Snake = Snake(x,y)
                break
            else:
                continue
    
    def encontrou(self,x,y):
        if((x < self.dim_rows and x>=0) and( y < self.dim_cols and y>=0)):
            if((x == self.pos_food_x) and (y == self.pos_food_y)):
                return True
            else:
                return False
        else:
            return False

    def permitido(self,x,y):
        if(((x < self.dim_rows) and (x>=0)) and( (y < self.dim_cols) and (y>=0))):
            if(self.assembly_maze[x][y] == 0):
                return False
            else:
                return True
        else:
            return False
    
    def visitado(self,x,y):
        if((x < self.dim_rows and x>=0) and( y < self.dim_cols and y>=0)):
            if (x,y) in self.rastro:
                #print("Está!!")
                return True
            else:
                return False
        else:
            return False
    
    def recebe_dados(self,assembly_maze,pos_food_x,pos_food_y):
        self.assembly_maze = assembly_maze
        self.pos_food_x = pos_food_x
        self.pos_food_y = pos_food_y

    def find_solution(self,x,y):
        if self.encontrou(x,y):
            return True
        else:
            if self.permitido(x+1,y) and not self.visitado(x+1,y): #DOWN
                self.m_way.append(2)
                #para o rastro
                pair = (x+1,y)
                self.rastro.append(pair)

                if self.find_solution(x+1,y):
                    return True
                else:
                    self.m_way.clear()

            if self.permitido(x-1,y) and not self.visitado(x-1,y): #UP
                self.m_way.append(1)
                pair = (x-1,y)#para o rastro
                self.rastro.append(pair)

                if self.find_solution(x-1,y):
                    return True
                else:
                    self.m_way.clear()

            if self.permitido(x,y+1) and not self.visitado(x,y+1): #RIGHT
                self.m_way.append(4)
                pair = (x,y+1)#para o rastro
                self.rastro.append(pair)

                if self.find_solution(x,y+1):
                    return True
                else:
                    self.m_way.clear()
            if self.permitido(x,y-1) and not self.visitado(x,y-1): #LEFT
                self.m_way.append(3)
                pair = (x,y-1)#para o rastro
                self.rastro.append(pair)

                if self.find_solution(x,y-1):
                    return True
                else:
                    self.m_way.clear()
        return False

    def next_move(self):
        if(len(self.m_way) != 0):
            move = self.m_way[0]
            self.m_way.pop(0)
            return move
        else:
            return 0

#Level class
class Level:
    def __init__(self,rows,cols):
        self.Levels = 4
        self.player_level = 0
        self.dim_rows = rows
        self.dim_cols = cols
        self.player = Player(self.dim_rows,self.dim_cols)
    
    def initialize_player(self):
        self.player.update_player(self.dim_rows,self.dim_cols,self.assembly_maze,self.pos_food_x,self.pos_food_y)
        self.player.find_solution(self.player.Snake._x,self.player.Snake._y)

    def initialize_level(self):
        self.initialize_maze()
        self.initialize_food()
        self.assembler_maze()
        self.player.recebe_dados(self.assembler_maze,self.pos_food_x,self.pos_food_y)
        

    def currently_level(self):
        if self.player_level > self.Levels:
            return False
        else:
            return True

        
    def next_level(self,rows,cols):
        self.dim_rows =  rows
        self.dim_cols = cols
        self.player_level += 1
        self.player.initialize_arrays()

    def initialize_maze(self):
        self.maze = [[' # ' for x in range(self.dim_cols)] for i in range(self.dim_rows)]
    
    def initialize_food(self):
        self.pos_food_y = int(random.random()*(self.dim_cols-1))
        self.pos_food_x = int(random.random()*(self.dim_rows-1))
        self.maze[self.pos_food_x][self.pos_food_y] = ' 🍎 '
        
    def assembler_maze(self):
        self.assembly_maze = [[1 if (self.maze[i][x] == ' # ' or  self.maze[i][x]==' 🐍 ' or self.maze[i][x]==' 🍎 ') else 0  for x in range(self.dim_cols)] for i in range(self.dim_rows)]
        #for i in range(0, self.dim_rows):
           # for j in range(0, self.dim_cols):
              #  print(self.assembly_maze[i][j],sep=' ',end='')
        #    print(end='\n')