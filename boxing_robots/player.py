import random, time

class Player(object):
    def __init__(self,id):
        self.id = id
        self.left_arm_state = 'idle'
        self.right_arm_state = 'idle'
        self.probability = 0.1
        self.t_end = t_end

    def get_damage(self, punch_direction):
        if (punch_direction != 'left' or punch_direction != 'right'):
            raise ValueError('direction must be either left or right')

        if punch_direction == 'left':
            self.blocking()
            if block_direction == 'left':
                # probabilistically decide if damage is taken
                return random.random() < probability

        elif punch_direction == 'right':
            self.blocking()
            if block_direction == 'right':
                # probabilistically decide if damage is taken
                return random.random() < probability

        elif punch_direction is not None:
            self.blocking()
            if block_direction == '':
                # probabilistically decide if damage is taken
                return random.random() < probability

        else:
            print "No damage has been dealt"
            return False

    # Move it to the main maybe?
    def check_game_status(self):

        if self.get_damage():
            print "Game Over"


    def blocking(self, block_direction=''):
        if (block_direction != 'left' or block_direction != 'right' or block_direction != ''):
            raise ValueError('direction must be either left or right')

        if block_direction == 'left':
            self.left_arm_state = 'blocking'
            print self.left_arm_state + ' ' + self.block_direction
            return block_direction
            #time.sleep(3)

        if block_direction == 'right':
            self.right_arm_state = 'blocking'
            print self.right_arm_state + ' ' + self.block_direction
            return block_direction
            #time.sleep(3)

        # if there is no blocking
        if block_direction == '':
            return block_direction

    def unblock(self, block_direction=''):
        if (block_direction != 'left' or block_direction != 'right' or block_direction != ''):
            raise ValueError('direction mus

        if block_direction == '':
            self.left_arm_state = 'idle'
            self.right_arm_state = 'idle'
        elif direction == 'left':
            self.left_arm_state = 'idle'
        elif direction == 'right':
            self.right_arm_state = 'idle'
