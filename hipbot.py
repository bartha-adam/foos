# Dependency: pip install python-simple-hipchat
import config
import hipchat
from gl.foos_gui import GuiState

class HipBot(object):
    def __init__(self):
        self.hc = hipchat.HipChat(token=config.hipchat_token)
        self.room = config.hipchat_room
        self.name = 'FooBot'

    def send_message(self, msg, color='yellow', notify=False):
        print msg, color, notify
        self.hc.message_room(self.room, self.name, msg, color=color, notify=notify)

    def send_info(self, state):
        if state.bScore == state.yScore == 0:
            msg = "New match!"
        else:
            msg = "Goal! Score: Black {} - {} Yellow".format(state.bScore, state.yScore)
        self.send_message(msg)
