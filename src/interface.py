import html


class signal():

    def __init__(self, sName=None, iWidth=None, sDescription=None):
        self.name = sName
        self.width = iWidth
        self.description = sDescription

    def create(self):
        lHtml = []
        lHtml.append('<tr>')
        lHtml.append('<td>' + self.name + '</td><td>' + str(self.width) + '</td><td>' + self.description + '</td>')
        lHtml.append('</tr>')
        return lHtml


class protocol():

    def __init__(self, sName=None):
        self.name = sName
        self.paragraphs = None
        self.imageLink = None

    def add_paragraph(self, sText):
        if not self.paragraphs:
            self.paragraphs = []
        self.paragraphs.append(sText)

    def create(self):
        lHtml = []
        lHtml.append('<h4>' + self.name + '</h4>')
        if self.paragraphs:
            for paragraph in self.paragraphs:
                lHtml.append('<p>' + paragraph + '</p>')
        if self.imageLink:
            lHtml.append('<img src="' + self.imageLink + '" class="img-responsive">')
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

    def create(self):
        lHtml = []
        lHtml.append('<h3>Interface 1</h3>')
        if self.paragraphs:
            for text in self.paragraphs:
                lHtml.append('<p>' + text + '</p>')
        if self.signals:
            lHtml.append('<table class="table table-striped table-bordered">')
            lHtml.append('<tr>')
            lHtml.append('<th>Signal</th><th>Width</th><th>Description</th>')
            lHtml.append('</tr>')
            for signal in self.signals:
                lHtml.extend(signal.create())
            lHtml.append('</table>')
        if self.protocols:
            for protocol in self.protocols:
                lHtml.extend(protocol.create())

        return lHtml
