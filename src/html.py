
class htmlFile():

    def __init__(self):
        self.item=[]

    def add_item(self,string):
        self.item.append(string)

class body():

  def __init__(self):
    self.item=[]

class header():

  def __init__(self):
    self.item=[]

  def add_item(self,string):
    self.item.append(string)

  def add_bootstrap(self):
    self.item.append('<meta charset="utf-8">')
    self.item.append('<meta name="viewport" content="width=device-width, initial-scale=1">')
    self.item.append('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">')
    self.item.append(script('https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js'))
    self.item.append(script('https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js'))

  def create(self):
    self.header = []
    self.header.append('<head>')
    for oItem in self.item:
      self.header.append(oItem.create())
    self.header.append('</head>')
    return self.header

class script():

  def __init__(self,source):
    self.source=source

  def create(self):
    return '<script>' + self.source + '</script>'

