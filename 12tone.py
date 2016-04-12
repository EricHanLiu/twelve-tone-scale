import math
import random
import sys

NOTES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
numbers = []


def show_scale():
    print [NOTES[i] for i in numbers]

def get_new_scale():
    return random.sample(range(12), 12)
    
def invert():
    diff = [b - a for (a, b) in zip(numbers[:-1], numbers[1:])]
    for a in range(11):
        numbers [a+1] = (numbers[a] - diff[a] + 12) % 12
    return numbers

def transpose():
    print "By how many semitones?"
    x = input()
    return [(numbers[a] + x + 12) % 12 for a in range(12)]
    
def print_stuff():
    print
    print "1: Retrograde"
    print "2: Inversion"
    print "3: Transposition"
    print "4: New 12-Tone Scale"
    print "Other: Quit"



if input("1: Generate New 12-Tone Scale \n") == 1:
    numbers = get_new_scale()
    show_scale()
else:
    sys.exit(0)

while True:
    print_stuff()
    x = input()
    if x == 1:
        #retrograde code
        numbers.reverse()
        show_scale()
    elif x == 2:
        numbers = invert()
        show_scale()
    elif x == 3:
        numbers = transpose()
        show_scale()
    elif x == 4:
        numbers = get_new_scale()
        show_scale()
    else:
        sys.exit(0)

    


