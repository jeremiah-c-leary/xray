
class tag():
  def __init__(self,name):
    self.name = name
    self.items = None
    self.source = None
    self.closeTag = True
    self.rel = None
    self.href = None
    self.meta_items = None
    self.language = None

  def add_item(self,item):
    if not self.items:
      self.items = []
    self.items.append(item)

  def create(self,indent=0,level=0):
    self.tag = []
    self.indent = ' '*indent*level
    self.openTag = self.indent + '<' + self.name
    if self.source:
      self.openTag = self.openTag + ' src="' + self.source + '"'
    if self.rel:
      self.openTag = self.openTag + ' rel="' + self.rel + '"'
    if self.href:
      self.openTag = self.openTag + ' href="' + self.href + '"'
    if self.meta_items:
      for metaItem in self.meta_items:
        self.openTag = self.openTag + ' ' + metaItem
    if self.language:
      self.openTag = self.openTag + ' lang="' + self.language + '"'
    self.openTag = self.openTag + '>'
    self.tag.append(self.openTag)
    if self.items:
      for oItem in self.items:
        self.tag.extend(oItem.create(indent=indent, level=level + 1))
    if self.closeTag:
      self.tag.append(self.indent + '</' + self.name + '>')
    return self.tag

class htmlFile(tag):

  def __init__(self):
    tag.__init__(self,'html')
    self.language = 'en' 

class body(tag):

  def __init__(self):
    tag.__init__(self,'body')

class link(tag):

  def __init__(self):
    tag.__init__(self,'link')
    self.closeTag = False

class meta(tag):

  def __init__(self):
    tag.__init__(self,'meta')
    self.closeTag = False
    self.meta_items = []

  def add_meta_item(self,meta):
    self.meta_items.append(meta)

class header(tag):

  def __init__(self):
    tag.__init__(self,'head')

  def add_bootstrap(self):
    self.items = []
    oMeta = meta()
    oMeta.add_meta_item('charset="utf-8"')
    self.items.append(oMeta)
    oMeta = meta()
    oMeta.add_meta_item('name="viewport"')
    oMeta.add_meta_item('content="width=device-width, initial-scale=1"')
    self.items.append(oMeta)
    oLink = link()
    oLink.rel = 'stylesheet'
    oLink.href = 'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css'
    self.items.append(oLink)
    self.items.append(script('https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js'))
    self.items.append(script('https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js'))

class script(tag):

  def __init__(self,source):
    tag.__init__(self,'script')
    self.source=source


