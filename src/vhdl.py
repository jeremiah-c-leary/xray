
class port():

    def __init__(self, sName, sDirection, sType, sComment):
        self.name = sName
        self.direction = sDirection
        self.type = sType
        self.comment = sComment


class interface():

    def __init__(self, sName):
        self.name = sName
        self.ports = None

    def add_port(self, oPort):
        if not self.ports:
            self.ports = []
        self.ports.append(oPort)


class port_map():

    def __init__(self):
        self.interfaces = None

    def add_interface(self, oInterface):
        if not self.interfaces:
            self.interfaces = []
        self.interfaces.append(oInterface)


class entity():

    def __init__(self, sName=None, oPortMap=None):
        self.name = sName
        self.portMap = oPortMap
