
# coding: utf-8

# In[ ]:

import pygame  

class Board:
    
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.count = 0
        
 
    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size
        
    def render(self):
	global screen
        for i in range(self.width):
            for j in range(self.height):
                if self.board[j][i] == 1:
                    pygame.draw.line(screen, (0,0,255), [ 2 + self.left + i*self.cell_size, 2 + self.top+j*self.cell_size], [self.left+(i+1)*self.cell_size-2, self.top+(j+1)*self.cell_size-2], 2)
                    pygame.draw.line(screen, (0,0,255), [ 2 + self.left + i*self.cell_size, -2 + self.top+(j+1)*self.cell_size], [-2+self.left+(i+1)*self.cell_size, -2+self.top+j*self.cell_size], 2)
                elif self.board[j][i] == 2: 
                    pygame.draw.circle(screen, (255,0,0), [self.left+int((i+0.5)*self.cell_size), self.top+int((j+0.5)*self.cell_size)], self.cell_size//2-2, 2)
                                   
                pygame.draw.rect(screen, (255, 255, 255), [self.left+i*self.cell_size, self.top+j*self.cell_size, self.cell_size, self.cell_size], 1)
                
                
    def get_cell(self, mouse_pos):
        if (self.left <= mouse_pos[0] <= self.left+self.cell_size*self.width) and (self.top <= mouse_pos[1] <= self.top+self.cell_size*self.height):
            return mouse_pos
        else:
            return None
            
            
    def on_click(self, cell_coords):
        if cell_coords != None:
            q = ((cell_coords[0] - self.left)//self.cell_size, (cell_coords[1] - self.top)//self.cell_size)            
            if self.board[q[1]][q[0]] == 0:
                if self.count % 2 == 0:
                    self.board[q[1]][q[0]] = 1
                else: 
                    self.board[q[1]][q[0]] = 2
            else:
                print('Not empty')
            self.count += 1
            
        else:
            print(cell_coords)
        
            
    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)

