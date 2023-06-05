def print_message() :
    print("CS101 is fantastic!")
    print("Programming is fun!")

def repeat_message() :
    print_message()
    print_message()


# create a robot with one beeper
hubo = Robot(beepers = 1)

# move one step forward
hubo.move()

# turn left 90 degress
hubo.turn_left()
