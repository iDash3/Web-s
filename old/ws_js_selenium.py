from selenium import webdriver
from selenium.webdriver.common.keys import Keys

LOGIN_URL = 'https://miscursos.tecmilenio.mx'
URL_COURSES = 'https://miscursos.tecmilenio.mx/webapps/portal/execute/tabs/tabAction?tab_tab_group_id=_2_1'

browser = webdriver.Firefox()
browser.get(LOGIN_URL)


USERNAME = 'al02764018'
PASSWORD = '276Bu018!'

user_input = browser.find_element_by_id('user_id')
user_input.send_keys(USERNAME)
password_input = browser.find_element_by_id('password')
password_input.send_keys(PASSWORD)
browser.find_element_by_id('entry-login').click()

#Get courses.
browser.get(URL_COURSES)
div_courses = browser.find_element_by_id('div_22_1')
ul_courses = div_courses.find_element_by_tag_name('ul')
courses = ul_courses.find_elements_by_tag_name('li')
for course in courses:
	course_href = course.getAttribute('href')


	

# browser.switch_to_frane()
# browser.find_elements_by_xpath(""/option[text() = ])   .click()
#						  id                  			.clear()
#						  css_selesctor()	  			.send_keys()
#	

# posts = browser.find_elements_by_class_name("")
# for post in posts:
#     print(post.text)

'''

# open tab
driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't') 

# Load a page 
driver.get('http://stackoverflow.com/')
# Make the tests...

# close the tab
driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'w') 
driver.close()

'''