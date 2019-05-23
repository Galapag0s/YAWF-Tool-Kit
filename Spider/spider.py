#Create Class for Spider
class SpiderSite:
	def __init__(self,url,parent,level):
		#URL is the url found in html
		self.url = url
		#Parent is the URL above it
		self.parent = parent
		#Level is the number of levels from the initial site
		self.level = level

