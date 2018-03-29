from main_msg import MainMsg

class AddEntryMsg(MainMsg):
    msg_type = MainMsg.addEntries

    def __init__(self, sender, receiver, term, content):
        MainMsg.__init__(self, sender, receiver, term, content)
