from splinter.browser import Browser

with Browser() as browser:
	url = "http://baidu.com"
	browser.visit(url)
	#button = browser.find_by_name('go')