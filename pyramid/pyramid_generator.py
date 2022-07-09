# Get height from user (8 max)
while True:
    height = int(input("Height: "))
    if height > 0 and height <= 8:
        break

# Save original height
og_height = height

# Generating ASCII
while height != 0:
    # Variables
    gap = 2
    spaces = height - 1
    bricks = og_height - spaces

    # Draw spaces
    print(" " * spaces, end="")

    # Draw bricks
    print("#" * bricks, end="")

    # Draw a gap
    print(" " * gap, end="")

    # Draw bricks again
    print("#" * bricks, end="")

    # Prepare for a new row
    height -= 1
    print()