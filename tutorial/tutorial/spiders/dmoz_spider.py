import scrapy
from scrapy.selector import Selector
from tutorial.items import DmozItem
from tutorial.items import Website

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["cabrillo.blackboard.com"]
    start_urls = [
#        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
 #       "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/",
#	"http://www.google.com",
#	"http://cabrillo.edu/"
	"https://cabrillo.blackboard.com/webapps/login/"
    ]

    def parse(self,response):
    	print("mooness is the holyness of the cowness bitchness")
    	return scrapy.FormRequest.from_response(
		response,
		formname = "login",
		formdata={'user_id':'brhern7247','password':'qwerty123'},
		clickdata={'class':'submit button-1'},
		callback=self.after_login
	)

    def after_login(self,response):
    	print "-------------------------------------------"
   	sel = Selector(response)
	messago = sel.xpath('//div[@class="receipt bad editmode"]/text()').extract()
#	print messago
#	print "blalfasdlfasdfhsadf blah blah blah blah"
    	if "The username or password you entered is incorrect. Please try again." in messago:
		print("shit that didn't work")
		#select elect s:u
#		self.log("Login failed",level=log.ERROR)
		return
	else:
		print "didn't find error message, might be logged in" 
		return scrapy.http.Request(url="https://cabrillo.blackboard.com/webapps/portal/frameset.jsp?tab_tab_group_id=_2_1&url=%2Fwebapps%2Fblackboard%2Fexecute%2Flauncher%3Ftype%3DCourse%26id%3D_7673_1%26url%3D",
			callback=self.parse_tastypage)

    def parse_tastypage(self,response):
	print response.body
	sel = Selector(response)
#print response.body
#	container = sel.xpath('//ul[@class="portletList-img courseListing coursefakeclass "]/li') 

#	container = sel.css('//ul/li')
#	print len(container)
	print "claire is so nice"	
#	for row in container:
#		print "chicken noodle SOUPOOOOOO"
#		print row.extract()
#		if "PS-1-90478" == row.xpath('a/text()').extract():	
#		print row.xpath('a/text()').extract()
	#	print len(row) + " moness gracious"
		#print row.xpath('div[@class="item clearfix"]/h3/a/text()').extract()	
"""    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//ul[@class="directory-url"]/li')
        items = []
        for site in sites:
	    item = Website()
            item['name'] = site.xpath('a/text()').extract()
            item['url'] = site.xpath('a/@href').extract()
            item['description'] = site.xpath('text()').re('-\s[^\n]*\\r')
	    items.append(item)

        return items
"""

