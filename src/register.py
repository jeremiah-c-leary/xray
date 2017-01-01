

class base():

    def __init__(self):
        self.lDescription = None

    def add_description(self, sDescription):
        if not self.lDescription:
            self.lDescription = []
        self.lDescription.append(sDescription)


class field(base):

    def __init__(self, sType, sBits, sDefault):
        base.__init__(self)
        self.sType = sType
        self.sBits = sBits
        self.iWidth = self.calculate_bit_width(self.sBits)
        self.sDefault = sDefault

    def calculate_bit_width(self, sBits):
        if ':' in sBits:
            lBits = sBits.split(':')
            return abs(int(lBits[0]) - int(lBits[1])) + 1
        else:
            return 1


class register(base):

    def __init__(self, sName, iWidth):
        base.__init__(self)
        self.sName = sName
        self.iWidth = iWidth
        self.lFields = None

    def add_field(self, oField):
        if not self.lFields:
            self.lFields = []
        self.lFields.append(oField)


class map_entry():

    def __init__(self, sAddress, sName, oObject):
        self.sAddress = sAddress
        self.sName = sName
        self.oObject = oObject

class map(base):

    def __init__(self, sName):
        base.__init__(self)
        self.sName = sName
        self.lObjects = None

    def add_entry(self, sAddress, sName, oObject):
        if not self.lObjects:
            self.lObjects = []
        self.lObjects.append(map_entry(sAddress, sName, oObject))

