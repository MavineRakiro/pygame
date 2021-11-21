from pygame import color
from pygame.event import event_name
import sorting_algorithms
import time
import os
import sys
import pygame

dimensions = [1024, 512]

algorithms = {
    "selectionsort": sorting_algorithms.selectionsort(),
    "bubblesort": sorting_algorithms.bubblesort(),
    "insertionsort": sorting_algorithms.insertionsort(),
    "mergesort": sorting_algorithms.mergesort(),
    "quicksort": sorting_algorithms.quicksort(),
}

if len(sys.argv) > 1:
    if sys.argv[1] == "list":
        for key in algorithms.keys(): print(key, end=" ")
        print("")
        sys.exit(0)

pygame.init()

display = pygame.display.set_mode((dimensions[0], dimensions[1]))

display.fill(pygame.Color("#a48be0"))

def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit();
            sys.exit;



def update(algorithm, swap1 = None, swap2 = None, display = display):
    display.fill(pygame.Color("#a48be0"))
    pygame.display.set_caption("SORTING VISUALIZER      Algorithm: {}     Time: {:.3f}       Status: Sorting...".format(algorithm.name, time.time()  -  algorithm.start_time))
    k = int(dimensions[0]/len(algorithm.array))

    for i in range(len(algorithm.array)):
        colour = (80, 0, 255)

        if swap1 == algorithm.array[i]:
            colour = (0, 255, 0)
        elif swap2 == algorithm.array[i]:
            colour = (255, 0, 0)

        pygame.draw.rect(display, colour, (i*k, dimensions[1], k, -algorithm.array[i]))

    check_events()
    pygame.display.update()


def keep_open(algorithm, display, time):
    pygame.display.set_caption("SORTING VISUALIZER     Algorithm: {}     Time: {:.3f}       Status: Done!".format(algorithm.name, time))
    
    while True:
        check_events()
        pygame.displayupdate()

def main():
    if len(sys.argv) < 2:
        print("Please select a sorting algorithm.")
        
    else:
        try:
            algorithm = algorithms[sys.argv[1]]
            try:
                time_elapsed = algorithm.run()[1]
                keep_open(algorithm, sys.display, time_elapsed)
                pass
            except:
                pass
        except:
            print("Error.")

if __name__ == "__main__":
   main()


"""
import algorithms
import time
import os
import sys
import pygame as pg

DARK_GRAY = '#65696B'
LIGHT_GRAY = '#C4C5BF'
BLUE = '#0CA8F6'
DARK_BLUE = '#4204CC'
WHITE = '#FFFFFF'
BLACK = '#000000'
RED = '#F22810'
YELLOW = '#F7E806'
PINK = '#F50BED'
LIGHT_GREEN = '#05F50E'
PURPLE = '#BF01FB'

 # Set the window length and breadth  
 # (Make sure that the breadth is equal to size of array. [512])
dimensions = (1024, 512)
# List all the algorithms available in the project in dictionary and call the
#  necessary functions from algorithms.py
algorithms = {"SelectionSort": algorithms.SelectionSort(), "BubbleSort": algorithms.BubbleSort(), "InsertionSort": algorithms.InsertionSort(), "MergeSort": algorithms.MergeSort(), "QuickSort": algorithms.QuickSort()}

# Set the dimensions of the window and display it
display = pg.display.set_mode(dimensions)
# Fill the window with purple hue
display.fill(pg.Color("#000000"))

def check_events(): # Check if the pg window was quit
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()


def update(algorithm, swap1=None, swap2=None, display=display):
    # The function responsible for drawing the sorted array on each iteration
    display.fill(pg.Color("#a48be0"))
    pg.display.set_caption("Sorting Visualizer     Algorithm: {}     Time: {:.3f}      Status: Sorting...".format(algorithm.name, time.time() - algorithm.start_time)) # Display on title bar
    k = int(dimensions[0]/len(algorithm.array))
    for i in range(len(algorithm.array)):
        colour = (80, 0, 255)
        if swap1 == algorithm.array[i]:
            colour = (0,255,0)
        elif swap2 == algorithm.array[i]:
            colour = (255,0,0)
        # The most important step that renders the rectangles to the screen that gets sorted.
        # pg.draw.rect(dsiplay_window, color_of_rectangle, size_of_rectangle)
        pg.draw.rect(display, colour, (i*k,dimensions[1],k,-algorithm.array[i]))
    check_events()
    pg.display.update()



def keep_open(algorithm, display, time): # Keep the window open until sort completion
    pg.display.set_caption("Sorting Visualizer     Algorithm: {}     Time: {:.3f}      Status: Done!".format(algorithm.name, time))
    while True:
        check_events()

def main(args):
    # Case: user failed to choose an algorithm    
    if len(args) < 2:
        print("Please select a sorting algorithm.")
    # Case: user requests list of algorithms
    elif args[1] == "list":
            print("Available algorithms:\n\t" + "\n\t".join(algorithms.keys()))
            sys.exit(0)
    # Case: user selected an algorithm
    else:
        try:
            algorithm = algorithms[args[1]] # Collect algorithm
            _, time_elapsed = algorithm.run() # Run algorithm and time it
            keep_open(algorithm, display, time_elapsed) # Display results
        except:
            print("Error.")

if __name__ == "__main__":
    sys.argv.append("BubbleSort")
    main(sys.argv)
"""