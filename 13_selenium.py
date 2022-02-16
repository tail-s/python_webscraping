from selenium import webdriver

browser = webdriver.Chrome() # "./chromedriver.exe"
browser.get("http://naver.com")

elem = browser.find_element_by_class_name("link_login")
elem.click