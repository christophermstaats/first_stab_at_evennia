"""
Characters

Characters are (by default) Objects setup to be puppeted by Accounts.
They are what you "see" in game. The Character class in this module
is setup to be the "default" character type created by the default
creation commands.

"""
from evennia import DefaultCharacter


class Character(DefaultCharacter):
    """
    The Character defaults to reimplementing some of base Object's hook methods with the
    following functionality:

    at_basetype_setup - always assigns the DefaultCmdSet to this object type
                    (important!)sets locks so character cannot be picked up
                    and its commands only be called by itself, not anyone else.
                    (to change things, use at_object_creation() instead).
    at_after_move(source_location) - Launches the "look" command after every move.
    at_post_unpuppet(account) -  when Account disconnects from the Character, we
                    store the current location in the pre_logout_location Attribute and
                    move it to a None-location so the "unpuppeted" character
                    object does not need to stay on grid. Echoes "Account has disconnected"
                    to the room.
    at_pre_puppet - Just before Account re-connects, retrieves the character's
                    pre_logout_location Attribute and move it back on the grid.
    at_post_puppet - Echoes "AccountName has entered the game" to the room.

    """
    # [...]
    def at_object_creation(self):
        """
        Called only at initial creation. This is a rather silly
        example since attribute scores should vary from Character to
        Character and is usually set during some character 
        generation step instead.
        """
        #tutorial values that only exist now to keep the code from breaking
        self.db.power = 1
        self.db.combat_score = 1
        #set persistent attributes
        self.db.cognition = 10
        self.db.coordination = 10
        self.db.intuition = 10
        self.db.reflexes = 10
        self.db.savvy = 10
        self.db.somatics = 10
        self.db.willpower = 10
        #set persistent skills
        self.db.academics = 5
        self.db.animalhandling = 5
        self.db.art = 5
        self.db.beamweapons = 5
        self.db.blades = 5
        self.db.climbing = 5
        self.db.clubs = 5
        self.db.control = 5
        self.db.deception = 5
        self.db.demolitions = 5
        self.db.disguise = 5
        self.db.xenosmelee = 5
        self.db.xenosranged = 5
        self.db.flight = 5
        self.db.fray = 5
        self.db.freefall = 5
        self.db.freerunning = 5
        self.db.gunnery = 5
        self.db.hardware = 5
        self.db.impersonation = 5
        self.db.infiltration = 5
        self.db.infosec = 5
        self.db.interfacing = 5
        self.db.intimidation = 5
        self.db.investigation = 5
        self.db.kinesics = 5
        self.db.kineticweapons = 5
        self.db.linguistics = 5
        self.db.medicine = 5
        self.db.navigation = 5
        self.db.palming = 5
        self.db.perception = 5
        self.db.persuasion = 5
        self.db.pilot = 5
        self.db.programming = 5
        self.db.protocol = 5
        self.db.psiassault = 5
        self.db.psychosurgery = 5
        self.db.research = 5
        self.db.scrounging = 5
        self.db.seekerweapons = 5
        self.db.sense = 5
        self.db.sprayweapons = 5
        self.db.swimming = 5
        self.db.thrownweapons = 5
        self.db.unarmedcombat = 5
        ### etc

    def get_attributes(self):
        """
        Simple access method to return attribute 
        scores as a tuple (str, agi, mag)
        """
        return self.db.cognition, self.db.coordination, self.db.intuition, self.db.reflexes, self.db.savvy, self.db.somatics, self.db.willpower

    def get_skills(self):
        """
        Simple access method to return skill 
        levels as a tuple (Academics, Animal Handling, etc.)
        """
        return self.db.academics, self.db.animalhandling, self.db.art, self.db.beamweapons, self.db.blades, self.db.climbing, self.db.clubs, self.db.control, self.db.deception, self.db.demolitions, self.db.disguise, self.db.xenosmelee, self.db.xenosranged, self.db.flight, self.db.fray, self.db.freefall, self.db.freerunning, self.db.gunnery, self.db.hardware, self.db.impersonation, self.db.infiltration, self.db.infosec, self.db.interfacing, self.db.intimidation, self.db.investigation, self.db.kinesics, self.db.kineticweapons, self.db.linguistics, self.db.medicine, self.db.navigation, self.db.palming, self.db.perception, self.db.persuasion, self.db.pilot, self.db.programming, self.db.protocol, self.db.psiassault, self.db.psychosurgery, self.db.research, self.db.scrounging, self.db.seekerweapons, self.db.sense, self.db.sprayweapons, self.db.swimming, self.db.thrownweapons, self.db.unarmedcombat

    #def get_abilities(self):
        #"""
        #Simple access method to return ability 
        #scores as a tuple (ability1, ability2, etc.)
        #"""
        ###return self.db.<ability1>, self.db.<ability2>, self.db.<etc.>, self.db.reflexes, self.db.savvy, self.db.somatics, self.db.willpower

	def return_appearance(self, looker):
		"""
		The return from  this method is what
		looker sees when looking at this object.
		"""
		text = super(Character, self).return_appearance(looker)
		cscore = " (combat score: %s)" % self.db.combat_score
		if "\n" in text:
			#text is multi-line, add score after first line
			first_line, rest = text.split("\n", 1)
			text = first_line + cscore + "\n" + rest
		else:
			#text is only one line; add score to end
			text += cscore
		return text

    pass
