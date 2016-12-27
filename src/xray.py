
import string


import html
import interface
import vhdl
import asciidoc


def build_head():

    # Generate head
    oHeadTag = html.head()

    oTag = html.meta()
    oTag.add_meta_item('charset="utf-8"')
    oHeadTag.add_tag(oTag)

    oTag = html.meta()
    oTag.add_meta_item('name="viewport"')
    oTag.add_meta_item('content="width-device-width, initial-scale=1"')
    oHeadTag.add_tag(oTag)

    oTag = html.link()
    oTag.rel = 'stylesheet'
    oTag.href = 'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css'
    oHeadTag.add_tag(oTag)

    oTag = html.script('https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js')
    oHeadTag.add_tag(oTag)

    oTag = html.script('https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js')
    oHeadTag.add_tag(oTag)

    return oHeadTag


def build_drop_menu(sName, lMenuItems):

    oLi = html.li()

    oA = html.a(sName)
    oA.add_class('dropdown-toggle')
    oA.href = '#'
    oA.dataToggle = 'dropdown'

    oLi.add_tag(oA)

    oUl = html.ul()
    oUl.add_class('dropdown-menu')

    for oMenuItem in lMenuItems:
        oUl.add_tag(oMenuItem)

    oLi.add_tag(oUl)

    return oLi


def build_navbar(sBrandLink, sBrand, lMenuItems):

    oNavTag = html.nav()
    oNavTag.add_class('navbar')
    oNavTag.add_class('navbar-inverse')
#    oNavTag.add_class('navbar-fixed-top')

    oDiv = html.div()
    oDiv.add_class('container-fluid')

    oTag = html.div()
    oTag.add_class('navbar-header')

    oA = html.a(sBrand)
    oA.add_class('navbar-brand')
    oA.href = sBrandLink

    oTag.add_tag(oA)
    oDiv.add_tag(oTag)

    if lMenuItems:
        oUl = html.ul()
        oUl.add_class('nav')
        oUl.add_class('navbar-nav')

        for oMenuItem in lMenuItems:
            oUl.add_tag(oMenuItem)

        oDiv.add_tag(oUl)

    oNavTag.add_tag(oDiv)

    return oNavTag


def menu_item(sHref, sName):

    oLi = html.li()
    oA = html.a(sName)
    oA.href = sHref
    oLi.add_tag(oA)

    return oLi


class interface():

    def __init__(self, sFilename=None):
        self.sFilename = sFilename

    def build_html(self):
        return asciidoc.file(self.sFilename).build_html()


class system():

    def __init__(self, sFilename=None):
        self.sFilename = sFilename

    def build_html(self):
        return asciidoc.file(self.sFilename).build_html()


class document():

    def __init__(self):
        self.lObjects = None

    def add_object(self, oObject):
        if not self.lObjects:
            self.lObjects = []
        self.lObjects.append(oObject)

    def build_filename(self, sString, sFileType):
        return sString.lower().replace(' ', '_') + '-' + sFileType.lower().replace(' ', '_') + '.html'

    def create_navbar(self):
        lDevices = None
        oDeviceMenu = None
        for oObject in self.lObjects:
            if isinstance(oObject, system):
                lHtmlObjects = oObject.build_html()
                sSystemHtmlFileName = self.build_filename(lHtmlObjects[0].create()[1], 'system')
                sSystemName = lHtmlObjects[0].create()[1]
            if isinstance(oObject, device):
                lHtmlObjects = oObject.build_html()
                sDeviceFileName = self.build_filename(sSystemName, lHtmlObjects[0].create()[1])
                sDeviceName = lHtmlObjects[0].create()[1]
                if not lDevices:
                    lDevices = []
                lDevices.append(menu_item(sDeviceFileName, sDeviceName))
        if lDevices:
            if len(lDevices) == 1:
                oDeviceMenu = lDevices[0]
            else:
                oDeviceMenu = build_drop_menu('Devices', lDevices)
        if oDeviceMenu:
          return build_navbar(sSystemHtmlFileName, sSystemName, [oDeviceMenu])
        else:
          return build_navbar(sSystemHtmlFileName, sSystemName, None)

    def create_html(self):
        oNavBar = self.create_navbar()

        for oObject in self.lObjects:
            if isinstance(oObject, system):
                lHtmlObjects = oObject.build_html()
                sSystemHtmlFileName = self.build_filename(lHtmlObjects[0].create()[1], 'system')
                sSystemName = lHtmlObjects[0].create()[1]

                oHtmlFile = html.html()
                oHtmlFile.add_tag(build_head())
                oBody = html.body()
                oBody.add_tag(oNavBar)
                for lHtmlObject in lHtmlObjects:
                    oBody.add_tag(lHtmlObject)
                oHtmlFile.add_tag(oBody)

                with open(sSystemHtmlFileName, 'w') as oFile:
                    for sTag in oHtmlFile.create():
                        oFile.write(sTag + '\n')

            if isinstance(oObject, device):
                lHtmlObjects = oObject.build_html()
                sDeviceFileName = sSystemName.lower().replace(' ', '_') + '-' + lHtmlObjects[0].create()[1].lower().replace(' ', '_') + '.html'
                sDeviceName = lHtmlObjects[0].create()[1]

                oHtmlFile = html.html()
                oHtmlFile.add_tag(build_head())
                oBody = html.body()
                oBody.add_tag(oNavBar)
                for lHtmlObject in lHtmlObjects:
                    oBody.add_tag(lHtmlObject)
                oHtmlFile.add_tag(oBody)

                with open(sDeviceFileName, 'w') as oFile:
                    for sTag in oHtmlFile.create():
                        oFile.write(sTag + '\n')


class device():

    def __init__(self, sFilename=None):
        self.sFilename = sFilename

    def build_html(self):
        return asciidoc.file(self.sFilename).build_html()
