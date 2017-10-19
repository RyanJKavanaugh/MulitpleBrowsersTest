from selenium import webdriver
#from selenium import selenium


# url = 'http://www.google.com'
#
# driver = webdriver.Ie()
#
# driver.get(url)

sel = selenium('localhost', 4444, '*firefox', 'http://www.google.com/')
sel.start()
sel.open('/')
sel.wait_for_page_to_load(10000)
sel.stop()