import numpy as np

# Rule number
rule = 150

# Binary representation of rule number
output_pattern = [int(x) for x in np.binary_repr(rule, width=8)]
print("Output pattern" + str(output_pattern))

# Binary representations of all numbers going down from 8
input_pattern = np.zeros([8, 3])
for i in range(8):
    input_pattern[i, :] = [int(x) for x in np.binary_repr(7-i, width=3)]

print("Input pattern" + str(input_pattern))

# Size of Cellular Automata grid defined by steps of lifecrycle of the CA
steps = 100
columns = steps + 1
rows = int(columns/2)+1
grid = np.zeros([rows, columns+2])

# TODO: Allow for different starting states
# Starting state of CA
grid[0, int(columns/2)+1] = 1

# Applies rule to grid according to starting position
for i in np.arange(0, rows-1):
    for j in np.arange(0, columns):
        for k in range(8):
            if np.array_equal(input_pattern[k, :], grid[i, j:j+3]):
                grid[i+1, j+1] = output_pattern[k]

# Key for the composition
key = "a"

# All available notes (whole tone scale)
all_notes = ["a", "a#", "b", "c", "c#", "d", "d#", "e", "e#", "f", "f#", "g", "g#"]
start = all_notes.index(key)

# Shift the the notes list to begin with the key
for _ in range(start):
    all_notes.append(all_notes.pop(0))

# Degrees for minor blues scale
degrees = [0, 3, 6, 7, 11]

# Converts list of scale degrees to corresponding notes
def to_notes(sequence):
    notes = []
    for degree in sequence:
        notes.append(all_notes[degree])
    return notes

# Scale converted to corresponding notes
scale = to_notes(degrees)
print("Key: " + key.upper() + " Minor - " + str(scale))

# Algorithm for generating compositions. The sum of the alive cells every
# generation is recording and checked if it exists in the scale.
sequence = []
for c in grid:
    sum = 0
    for num in c:
        sum = (sum + num) % 13
    if sum in degrees:
        sequence.append(int(sum))

comp = to_notes(sequence)
print("Composition: " + str(comp))