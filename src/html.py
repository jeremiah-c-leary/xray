
class tag():
    def __init__(self, name):
        self.name = name
        self.tags = None
        self.source = None
        self.closeTag = True
        self.rel = None
        self.href = None
        self.meta_items = None
        self.language = None
        self.classes = None
        self.linkText = None
        self.dataToggle = None
        self.id = None
        self.colspan = None

    def add_tag(self, item):
        if not self.tags:
            self.tags = []
        self.tags.append(item)

    def add_class(self, item):
        if not self.classes:
            self.classes = []
        self.classes.append(item)

    def create(self, indent=0, level=0):
        self.tag = []
        self.indent = ' ' * indent * level
        self.openTag = self.indent + '<' + self.name

        if self.id:
            self.openTag = self.openTag + ' id="' + self.id + '"'

        if self.source:
            self.openTag = self.openTag + ' src="' + self.source + '"'

        if self.rel:
            self.openTag = self.openTag + ' rel="' + self.rel + '"'

        if self.href:
            self.openTag = self.openTag + ' href="' + self.href + '"'

        if self.colspan:
            self.openTag += ' colspan="' + str(self.colspan) + '"'

        if self.meta_items:
            for metaItem in self.meta_items:
                self.openTag = self.openTag + ' ' + metaItem

        if self.language:
            self.openTag = self.openTag + ' lang="' + self.language + '"'

        if self.classes:
            self.openTag = self.openTag + ' class="'
            for sClass in self.classes:
                self.openTag = self.openTag + sClass + ' '
            self.openTag = self.openTag[:-1] + '"'

        if self.dataToggle:
            self.openTag = self.openTag + ' data-toggle="' + \
                           self.dataToggle + '"'

        self.openTag = self.openTag + '>'
        self.tag.append(self.openTag)
        if self.tags:
            for oItem in self.tags:
                self.tag.extend(oItem.create(indent=indent, level=level + 1))
        if self.linkText:
            self.tag.append(self.indent + ' ' * indent + self.linkText)
        if self.closeTag:
            self.tag.append(self.indent + '</' + self.name + '>')
        return self.tag


class html(tag):

    def __init__(self):
        tag.__init__(self, 'html')
        self.language = 'en'


class body(tag):

    def __init__(self):
        tag.__init__(self, 'body')


class link(tag):

    def __init__(self):
        tag.__init__(self, 'link')
        self.closeTag = False


class meta(tag):

    def __init__(self):
        tag.__init__(self, 'meta')
        self.closeTag = False
        self.meta_items = []

    def add_meta_item(self, meta):
        self.meta_items.append(meta)


class head(tag):

    def __init__(self):
        tag.__init__(self, 'head')


class script(tag):

    def __init__(self, source):
        tag.__init__(self, 'script')
        self.source = source


class nav(tag):

    def __init__(self):
        tag.__init__(self, 'nav')


class div(tag):

    def __init__(self):
        tag.__init__(self, 'div')


class ul(tag):

    def __init__(self):
        tag.__init__(self, 'ul')


class li(tag):

    def __init__(self, linkText=None):
        tag.__init__(self, 'li')
        self.linkText = linkText


class p(tag):

    def __init__(self, text):
        tag.__init__(self, 'p')
        self.linkText = text


class a(tag):

    def __init__(self, linkText):
        tag.__init__(self, 'a')
        self.linkText = linkText


class h1(tag):

    def __init__(self, linkText):
        tag.__init__(self, 'h1')
        self.linkText = linkText


class h2(tag):

    def __init__(self, linkText):
        tag.__init__(self, 'h2')
        self.linkText = linkText


class h(tag):

    def __init__(self, level, sText):
        tag.__init__(self, 'h' + str(level))
        self.linkText = sText


class tr(tag):

    def __init__(self):
        tag.__init__(self, 'tr')


class td(tag):

    def __init__(self, sText):
        tag.__init__(self, 'td')
        self.linkText = sText


class th(tag):

    def __init__(self, sText):
        tag.__init__(self, 'th')
        self.linkText = sText


class img(tag):

    def __init__(self, sText):
        tag.__init__(self, 'img')
        self.closeTag = False
        self.source = sText


class table(tag):

    def __init__(self):
        tag.__init__(self, 'table')
