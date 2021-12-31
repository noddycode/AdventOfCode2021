# Can we calculate the veloctiy from each of the ending positions and select the one with the highest arc?

# Start from possible landing positions and calculate
def get_pos(velocity, pos):
    x, y = pos
    vx, vy = velocity

# We can consider x and y velocity separately?
# x = (max(vx - t, 0))t
# y = (vy-t)t