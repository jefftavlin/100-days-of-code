def spin():
    for i in range(3):
        turn_left()

def one_turn():
    move()
    turn_left()
    
def cycle():
    one_turn()
    move()
    spin()
    move()
    spin()
    one_turn()

for i in range(6):
    cycle()
