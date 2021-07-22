from selenium import webdriver

browser = webdriver.Chrome(executable_path="/Users/alex/Desktop/DevOps-Course/Selenium drivers/chromedriver")
browser.get("https://www.walla.co.il")
print(browser.title)
browser.close()
