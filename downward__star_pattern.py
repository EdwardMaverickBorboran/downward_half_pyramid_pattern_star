# Create a program that will --

# Print a downward Half-Pyramid Pattern of Star(asterisk).

# Expected results: 
# * * * * *  
# * * * *  
# * * *  
# * *  
# *

# DEADLINE: JANUARY 26, 2024

# pseudocode

# Using for loop and range
for downward in range (6, 0, -1):
    for pattern in range(0, downward - 1):
        print("*", end=" ")
    print("")