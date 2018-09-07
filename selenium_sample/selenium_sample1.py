from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.keys import Keys


chrome_option = ChromeOptions()
# chrome_option.set_headless()

driver = Chrome(executable_path='/home/xuananh/Downloads/chromedriver_linux64/chromedriver',
                chrome_options=chrome_option)

driver.get('http://www.python.org')
assert "Python" in driver.title

element = driver.find_element_by_name('q')
element.clear()
element.send_keys("pycon")
element.send_keys(Keys.RETURN)

assert "No results found." not in driver.page_source
driver.close()
