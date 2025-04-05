# *** P ***
# Input: number_of_available_blocks (int)
# Output: int - number of blocks left over
#
# Q: Can there be sets of four blocks in a layer that DON'T have a block on top?
# e.g.: (side view)
#               x
#              x x x
# This seems to be valid according to the explicit rules.
#
# The straightforward approach seems to be to start with the top layer
# as a single block and move downward, increasing the base with each
# step, resulting in a pyramid. As soon as you are unable to complete
# the current base, all the available blocks you would have used in that
# base become left over.
#
# If approaching this way, each layer simply becomes a square with a
# side of n+1.


# *** e ***
#
# Provided test cases:
# print(calculate_leftover_blocks(0) == 0)  # True
# print(calculate_leftover_blocks(1) == 0)  # True
# print(calculate_leftover_blocks(2) == 1)  # True
# print(calculate_leftover_blocks(4) == 3)  # True
# print(calculate_leftover_blocks(5) == 0)  # True
# print(calculate_leftover_blocks(6) == 1)  # True
# print(calculate_leftover_blocks(14) == 0) # True
#
# These confirm the straightforward approach mental model.

# *** d ***
#
# Not sure a data structure is needed. Maybe a list of layers.

# *** a ***
#
# 1. set remaining_blocks equal to number_of_available_blocks
# 2. set current_layer to 1
# 3. loop forever:
#    a. increment current_layer
#    b. set new_layer_blocks_used equal to current_layer squared
#    c. if new_layer_blocks_used > remaining_blocks
#           then return remaining_blocks -- this is the leftover
#    d. else remaining_blocks -= new_layer_blocks_used


# *** c ***

def calculate_leftover_blocks(number_of_available_blocks):
    if not isinstance(number_of_available_blocks, int) or \
        number_of_available_blocks < 0:
        raise ValueError("Argument must be a positive integer.")
    remaining_blocks = number_of_available_blocks
    current_layer = 0
    while True:
        current_layer += 1
        new_layer_blocks_used = current_layer**2
        if new_layer_blocks_used > remaining_blocks:
            return remaining_blocks
        remaining_blocks -= new_layer_blocks_used

print(calculate_leftover_blocks(0) == 0)  # True
print(calculate_leftover_blocks(1) == 0)  # True
print(calculate_leftover_blocks(2) == 1)  # True
print(calculate_leftover_blocks(4) == 3)  # True
print(calculate_leftover_blocks(5) == 0)  # True
print(calculate_leftover_blocks(6) == 1)  # True
print(calculate_leftover_blocks(14) == 0) # True
print(calculate_leftover_blocks(-1))
