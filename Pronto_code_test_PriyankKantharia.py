user_input = input("Enter the comma seperated commands for the robot to move").split(",")
letter = []
number = []
for each in user_input:
    letter.append(each[0].lower())
    number.append(int(each[1]))
initial_location = [0, 0, 1]                        # The initial location or the starting point of the Robot is the start point with x and y co-ordinates both at 0
                                                    # The default direction for start location is 1, which is North.
location = [0, 0, 1]
for i in range(len(letter)):
    if (letter[i] == "f"):
        if (location[2] == 1):                      # The robot is in the north direction and wants to move forward.
            y = location[1] + number[i]
            location = [location[0], y, location[2]]
        elif (location[2] == 2):                    # The robot is in the east direction and wants to move forward.
            x = location[0] + number[i]
            location = [x, location[1], location[2]]
        elif (location[2] == 3):                    # The robot is in the south direction and wants to move forward.
            y = location[0] - number[i]
            location = [location[0], y, location[2]]
        elif (location[2] == 4):                    # The robot is in the west direction and wants to move forward.
            x = location[0] - number[i]
            location = [x, location[1], location[2]]
    elif (letter[i] == "b"):
        if location[2] == 1:                        # The robot is in the north direction and wants to move backward.
            y = location[1] - number[i]
            location = [location[0], y, location[2]]
        elif location[2] == 2:                         # The robot is in the east direction and wants to move backward.
            x = location[0] - number[i]
            location = [x, location[1], location[2]]
        elif location[2] == 3:                        # The robot is in the south direction and wants to move backward.
            y = location[2] + number[i]
            location = [location[0], y, location[2]]
        elif location[2] == 4:                          # The robot is in the west direction and wants to move backward.
            x = location[0] + number[i]
            location = [x, location[1], location[2]]
    elif (letter[i] == "r"):                            # The robot wants to turn right by 90 degrees dependig on his current direction.
        z = (location[2] + number[i]) % 4
        location = [location[0], location[1], z]
    elif (letter[i] == "l"):                             # The robot wants to turn left by 90 degrees dependig on his current direction.
        z = (location[2] - number[i]) % 4
        location = [location[0], location[1], z]

print(location)
min_distance = abs(location[0]) + abs(location[1])         # The minimum distance is found by adding the absolute values of the two co-ordinates.

print('The minimum distance from the start point is:' , min_distance , 'units' )
