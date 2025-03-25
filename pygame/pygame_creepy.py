
# coding: utf-8

# In[1]:


import pygame, sys
pygame.init()
window=pygame.display.set_mode((300, 300))

size = width, height = 400, 400
screen = pygame.display.set_mode(size)

k=1

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
                
        elif event.type == pygame.ACTIVEEVENT:
            
            if  (event.state == 1) or ((event.state == 2) & (event.gain == 1) ):
                window.fill((255, 255, 255))
                font = pygame.font.Font(None, 50)
                text = font.render("{}".format(k), 1, (102, 105, 160))
                text_x = width // 2 - text.get_width() // 2
                text_y = height // 2 - text.get_height() // 2
                text_w = text.get_width()
                text_h = text.get_height()
                screen.blit(text, (text_x, text_y))

            elif event.state == 2:
                if event.gain == 0:
                    k+=1
    
    pygame.display.flip()

