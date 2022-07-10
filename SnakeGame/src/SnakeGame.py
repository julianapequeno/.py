import random
import time
from os import system, name

from Player import Player
from Player import Snake
from Player import Level

#clear method
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

#game class    
class SnakeGame:
    def __init__(self,rows,cols):
        self.dim_rows = rows
        self.dim_cols = cols
        self.initialize_game()

    def mostrar_menu(self):
        while(True):
            print('----- S N A K E - G A M E 🐍(python)------')
            print('1 - Iniciar jogo')
            print('2 - Sair')
            choice = int(input(''))
            if choice == 1:
                return True
            elif choice == 2:
                return False

    def initialize_game(self): #primeira vez
        running = self.mostrar_menu()
        if(running):
            self.Level = Level(self.dim_rows,self.dim_cols)


    def game_loop(self): #indução em n
        while(self.Level.currently_level()):
            self.Level.initialize_level()
            self.Level.initialize_player()
            self.rodar_solution() #roda a solução do primeiro
            time.sleep(2)
            print(' PASSANDO PARA O PRÓXIMO NÍVEL!!! ')
            time.sleep(3)
            clear()
            #updating maze in SnakeGame
            self.dim_rows +=1
            self.dim_cols +=1
            time.sleep(1)
            #updating everything in Level
            self.Level.next_level(self.dim_rows,self.dim_cols)


    def desenhar_maze(self):
        self.Level.maze = [[' # ' for x in range(self.dim_cols)] for i in range(self.dim_rows)]
        self.mostrar_food()
        self.mostrar_snake()

    def mostrar_maze(self):
        for i in range(0,self.dim_rows):
            for j in range(0,self.dim_cols):
                print(self.Level.maze[i][j],sep=' ',end='')
            print(end='\n')
    
    def mostrar_snake(self):
        self.Level.maze[self.Level.player.Snake._x][self.Level.player.Snake._y] = ' 🐍 '
    
    def mostrar_food(self):
        self.Level.maze[self.Level.pos_food_x][self.Level.pos_food_y] = ' 🍎 '


    def rodar_solution(self):
       while(True):
            i = self.Level.player.next_move()
            if(i == 1):
                self.Level.player.Snake.update_pos(self.Level.player.Snake._x-1,self.Level.player.Snake._y)
            elif(i == 2):
                self.Level.player.Snake.update_pos(self.Level.player.Snake._x+1,self.Level.player.Snake._y)
            elif(i == 3):
                self.Level.player.Snake.update_pos(self.Level.player.Snake._x,self.Level.player.Snake._y-1)
            elif(i == 4):
                self.Level.player.Snake.update_pos(self.Level.player.Snake._x,self.Level.player.Snake._y+1)
            elif(i == 0):
                self.desenhar_maze()
                self.mostrar_maze()
                break
            self.desenhar_maze()
            self.mostrar_maze()
            time.sleep(0.15)
            clear()

if __name__ == '__main__':
    sG = SnakeGame(10,10)
    sG.game_loop()