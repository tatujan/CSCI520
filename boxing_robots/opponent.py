import random, time

class Opponent(object):

    def __init__(self, id):
        self.id = id
        self.state = 'idle'
        self.state_frames = 60

    def Opp_get_damage(self):
        if not ((self.state == 'block_left' and direction == 'left') or \
                (self.state == 'block_right' and direction == 'right') or \
                (self.state == 'block_both' and direction == 'center')):
            return random.random() < probability

        else:
            # Attack was blocked
            return False
