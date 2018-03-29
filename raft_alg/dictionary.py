
class Dictionary(object):

    def __init__(self):
        self.dictionary = []

    def set_owner(self, owner):
        self.owner = owner

    def post_message(self, message):
        self.dictionary.append(message)

        self.dictionary = sorted(self.dictionary,
                     key=lambda e: e.timestamp, reverse=True)

    def rcv_message(self, message):
        if(len(self.dictionary) > 0):
            return self.dictionary.pop()
        else:
            return None
