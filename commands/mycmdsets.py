from commands.command import CmdEcho
from evennia import CmdSet

class MyCmdSet(CmdSet):
    
    key = MyCmdSet

    def at_cmdset_creation(self):
        self.add(CmdEcho())
