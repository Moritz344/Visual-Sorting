import pygame
import random
import sys

width = 1920
height = 1080
screen = pygame.display.set_mode((width,height))
arr = [random.randint(1,500) for _ in range(100)]
clock = pygame.time.Clock()
swaps = 0
color = "white"
delay = 0
pygame.display.set_caption("Quick Sort")
pygame.font.init()
font = pygame.font.SysFont("Open Sans",30)

def debug_info():
    fps_text = font.render(f"FPS: {clock.tick(60)}",False,"white")
    swaps_text = font.render(f"Swaps: {swaps}",False,"white")
    screen.blit(fps_text,(10,10))
    screen.blit(swaps_text,(10,50))

def draw_arr(arr,current_index=None,):
    global color
    block_width = width // len(arr)
    for i,val in enumerate(arr):
        if i == current_index:
            color = "green"
        else:
            color = "white"

        pygame.draw.rect(screen,color,(i * block_width,height - val,block_width,val ))

def quick_sort_visual(arr, start, end):
    global clock, swaps,  delay, running
    
    if start >= end:
        return

    # teilt das Array in zwei Teile
    pivot_index = partition_visual(arr, start, end)
    
    # Sortieren rekursiv
    quick_sort_visual(arr, start, pivot_index - 1) # Linkes Teil Array
    quick_sort_visual(arr, pivot_index + 1, end) # Rechter Teil Array

def partition_visual(arr, start, end):
    global swaps,  running, clock
    
    pivot = arr[end] # pivot ist das letzte element
    i = start - 1  # Index für kleinere Elemente
    
    for j in range(start, end):
        # Zeichne aktuelle Array-Situation
        screen.fill("black")
        debug_info()
        draw_arr(arr, current_index=j)
        pygame.time.delay(delay)
        pygame.display.update()
        
        # Vergleiche mit dem Pivot
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            swaps += 1
            
            # Zeige den Swap
            screen.fill("black")
            debug_info()
            draw_arr(arr, current_index=j)
            pygame.time.delay(delay)
            pygame.display.update()
        
        # Überprüfe auf Beenden
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit(0)
    
    # kleineren Elemente links und größere rechts
    arr[i+1], arr[end] = arr[end], arr[i+1]
    swaps += 1
    
    # Zeige das Platzieren des Pivots
    screen.fill("black")
    debug_info()
    draw_arr(arr,current_index=i + 1)
    pygame.time.delay(delay)
    pygame.display.update()
    
    return i + 1

quick_sort_visual(arr,0,len(arr) - 1)

run: bool = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run: bool = False
