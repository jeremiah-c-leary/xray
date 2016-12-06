
class tag():
  def __init__(self,name):
    self.name = name
    self.items = None
    self.source = None
    self.closeTag = True
    self.rel = None
    self.href = None

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
    self.openTag = self.openTag + '>'
    self.tag.append(self.openTag)
    if self.items:
      for oItem in self.items:
        self.tag.extend(oItem.create(indent=indent, level=level + 1))
    if self.closeTag:
      self.tag.append(self.indent + '</' + self.name + '>')
    return self.tag

class htmlFile():

  def __init__(self):
    self.items=[]

  def add_item(self,item):
    self.items.append(item)

  def create(self,indent=2):
    self.html = []
    self.html.append('<html lang="en">')
    for oItem in self.items:
      self.html.extend(oItem.create(indent))
    self.html.append('</html>')
    return self.html


class body():

  def __init__(self):
    self.items=[]

class link(tag):

  def __init__(self):
    tag.__init__(self,'link')
    self.closeTag = False

class meta():

  def __init__(self):
    self.items=[]

  def add_item(self,item):
    self.items.append(item)

  def create(self,indent=0):
    self.meta = ' '*indent + '<meta'
    for item in self.items:
      self.meta = self.meta + ' ' + item
    self.meta = self.meta + '>'
    return self.meta

class header():

  def __init__(self):
    self.items=[]

  def add_item(self,item):
    self.items.append(item)

  def add_bootstrap(self):
    oMeta = meta()
    oMeta.add_item('charset="utf-8"')
    self.items.append(oMeta)
    oMeta = meta()
    oMeta.add_item('name="viewport"')
    oMeta.add_item('content="width=device-width, initial-scale=1"')
    self.items.append(oMeta)
    oLink = link()
    oLink.rel = 'stylesheet'
    oLink.href = 'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css'
    self.items.append(oLink)
    self.items.append(script('https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js'))
    self.items.append(script('https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js'))

  def create(self,indent=0):
    self.header = []
    self.header.append(' '*indent + '<head>')
    for oItem in self.items:
      self.header.append(' '*indent + oItem.create(indent))
    self.header.append(' '*indent + '</head>')
    return self.header

class script():

  def __init__(self,source):
    self.source=source

  def create(self,indent=0):
    return ' '*indent + '<script src="' + self.source + '"></script>'

