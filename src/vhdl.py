
import html
import re


class port():

    def __init__(self, sName, sDirection, sType, sComment):
        self.name = sName
        self.direction = sDirection
        self.type = sType
        self.comment = sComment

    def std_logic_vector_size(self, sStdLogicVector):
        lIndices = re.split('\W+', sStdLogicVector)
        return abs(int(lIndices[1]) - int(lIndices[3])) + 1

    def build_html(self):
        oTr = html.tr()
        oTr.add_tag(html.td(self.name))
        if 'std_logic_vector' in self.type:
            oTr.add_tag(html.td(str(self.std_logic_vector_size(self.type))))
        else:
            oTr.add_tag(html.td('1'))
        oTr.add_tag(html.td(self.direction))
        if 'std_logic_vector' in self.type:
            oTr.add_tag(html.td('std_logic_vector'))
        else:
            oTr.add_tag(html.td(self.type))
        oTr.add_tag(html.td(self.comment))
        return oTr


class interface():

    def __init__(self, sName):
        self.name = sName
        self.ports = None

    def add_port(self, oPort):
        if not self.ports:
            self.ports = []
        self.ports.append(oPort)

    def build_html(self):
        lHtml = []
        # Build spanning row for interface name
        oTr = html.tr()
        oTd = html.td(self.name)
        oTd.colspan = 5
        oTr.add_tag(oTd)
        lHtml.append(oTr)
        # Build signal rows
        for oPort in self.ports:
            lHtml.append(oPort.build_html())
        return lHtml


class port_map():

    def __init__(self):
        self.interfaces = None

    def add_interface(self, oInterface):
        if not self.interfaces:
            self.interfaces = []
        self.interfaces.append(oInterface)

    def build_html(self):
        oTable = html.table()
        oTable.add_class('table')
        oTable.add_class('table-striped')
        oTable.add_class('table-bordered')
        oTr = html.tr()
        oTr.add_tag(html.th('Name'))
        oTr.add_tag(html.th('Size'))
        oTr.add_tag(html.th('Direction'))
        oTr.add_tag(html.th('Type'))
        oTr.add_tag(html.th('Description'))
        oTable.add_tag(oTr)
        for oInterface in self.interfaces:
            for oTag in oInterface.build_html():
                oTable.add_tag(oTag)
        return oTable


class entity():

    def __init__(self, sName=None, oPortMap=None):
        self.name = sName
        self.portMap = oPortMap

    def build_html(self):
        return [self.portMap.build_html()]
