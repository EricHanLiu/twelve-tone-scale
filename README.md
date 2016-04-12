# Twelve Tone Scale
This is a music theory related script, made for facilitating the creation and manipulation of 12-tone scale compositions.

## What is it?
The 12-tone scale is a musical scale that places equal importance on all 12 notes of the scale.
Every note must be used once before repeating another note is allowed.

## What does this program do?
This program generates random 12-tone scale passages, called **primes**, and allows the user to manipulate them in the following ways:

*Note: the scale's range is from 0-11, not 1-12, and the following examples use 6 notes instead of 12 to simplify.*
- Retrograde: Makes the prime backwards (0-3-2-6-9-4 becomes 4-9-6-2-3-0)
- Inversion: Inverts the intervals between each note (0-3-6-7-8-11 becomes 0-9-6-5-4-1)
- Transposition: Takes the prime as a whole and moves it (3-5-6-7-9-11 up 3 becomes 6-8-9-10-0-2)
- Any Combination: For example, you can invert then retrograde then transpose up a 5th

## How to use?
Simple!

Just run the file '12tone.py' using python (`python 12tone.py`) and follow the onscreen instructions.

