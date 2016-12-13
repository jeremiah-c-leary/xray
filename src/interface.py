import html


class signal():

    def __init__(self, sName=None, iWidth=None, sDescription=None):
        self.name = sName
        self.width = iWidth
        self.description = sDescription

    def build_html(self):
        oTr = html.tag('tr')

        oTd = html.tag('td')
        oTd.linkText = self.name
        oTr.add_tag(oTd)

        oTd = html.tag('td')
        oTd.linkText = str(self.width)
        oTr.add_tag(oTd)

        oTd = html.tag('td')
        oTd.linkText = self.description
        oTr.add_tag(oTd)

        return oTr

    def create(self):
        return self.build_html().create()


class protocol():

    def __init__(self, sName=None):
        self.name = sName
        self.paragraphs = None
        self.imageLink = None

    def add_paragraph(self, sText):
        if not self.paragraphs:
            self.paragraphs = []
        self.paragraphs.append(sText)

    def build_html(self):
        lHtml = []
        lHtml.append(html.h(4, self.name))
        if self.paragraphs:
            for paragraph in self.paragraphs:
                lHtml.append(html.p(paragraph))
        if self.imageLink:
            oImg = html.img(self.imageLink)
            oImg.add_class('img-responsive')
            lHtml.append(oImg)
        return lHtml


class create():

    def __init__(self, sName=None):
        self.name = sName
        self.paragraphs = None
        self.protocols = None
        self.signals = None

    def add_paragraph(self, sText):
        if not self.paragraphs:
            self.paragraphs = []
        self.paragraphs.append(sText)

    def add_signal(self, oSignal):
        if not self.signals:
            self.signals = []
        self.signals.append(oSignal)

    def add_protocol(self, oProtocol):
        if not self.protocols:
            self.protocols = []
        self.protocols.append(oProtocol)

    def build_html(self):
        lHtml = []
        lHtml.append(html.h(3, self.name))
        if self.paragraphs:
            for text in self.paragraphs:
                lHtml.append(html.p(text))
        if self.signals:
            oTable = html.tag('table')
            oTable.add_class('table')
            oTable.add_class('table-striped')
            oTable.add_class('table-bordered')
            oTr = html.tr()
            oTr.add_tag(html.th('Signal'))
            oTr.add_tag(html.th('Width'))
            oTr.add_tag(html.th('Description'))
            oTable.add_tag(oTr)
            for signal in self.signals:
                oTable.add_tag(signal.build_html())
            lHtml.append(oTable)

        if self.protocols:
            for protocol in self.protocols:
                lHtml.extend(protocol.build_html())

        return lHtml

    def create(self):
        lHtml = []
        for oHtml in self.build_html():
            lHtml.extend(oHtml.create())
        return lHtml
