import random
import pygame
import sys

pygame.init()

width: int = 1920
height: int = 1080
screen = pygame.display.set_mode((width,height))
numBlocks: int = 150
rounds: int = 0
delay: int = 0 # ms
swaps: int = 0
arr = [random.randint(1,400) for _ in range(numBlocks)]

pygame.font.init()
font = pygame.font.Font("MinecraftRegular.otf",30)
normal = pygame.font.SysFont("Times New Roman",30)
FPS = 120
color = "white"

pygame.display.set_caption("Sorting Algorithm")

def draw_arr(arr,current_index=None):
    block_width = width // len(arr)

    for i,val in enumerate(arr): # index + value
        if i - 1 == current_index:
            color = "green"
        else:
            color = "white"

        pygame.draw.rect(screen,color,(i * block_width ,height - val,block_width ,val))
        

def debug_info():
    fps_text = font.render(f"FPS: {clock.tick(60)}",False,"white")
    swaps_text = font.render(f"Swaps: {swaps}",False,"white")
    arr_text = font.render(f"Iteration: {rounds}",False,"white")
    screen.blit(fps_text,(10,10))
    screen.blit(swaps_text,(10,90))
    screen.blit(arr_text,(10,50))

    
    

def bubble_sort(arr):
    global clock
    global color
    global rounds
    global swaps
    n = len(arr)
    clock = pygame.time.Clock()
    running: bool = True

    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                screen.fill("black")
                debug_info()
                swaps += 1

                

                draw_arr(arr,current_index=j)
                pygame.time.delay(delay)
                pygame.display.update()
                clock.tick(FPS)
                


                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running: bool = False
            if not running:
                sys.exit(0)

        rounds += 1
    #print("everything is sorted!")

bubble_sort(arr)


run: bool = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run: bool = False

