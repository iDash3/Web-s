# -*-coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

LOGIN_URL = 'https://miscursos.tecmilenio.mx'
URL_COURSES = 'https://miscursos.tecmilenio.mx/webapps/portal/execute/tabs/tabAction?tab_tab_group_id=_2_1'

USERNAME = 'al02764018'
PASSWORD = '276Bu018!'

browser = webdriver.Firefox()
file_name = 'all_info.txt'

def main():
	# Temporal use of main.
	'''
	temporal_user = raw_input('Enter username: ')
	temporal_passwd = raw_input('Enter password: ')
	file = open('f.txt','w') 
	file.write('Idiota /n' ) 
	file.write(temporal_user + 'n') 
	file.write(temporal_passwd + '/n') 
	file.write('Wink.') 
	file.close() 
	'''
	# GET
	browser.get(LOGIN_URL)
	#GET
	'''
	user_input = browser.find_element_by_id('user_id')
	user_input.send_keys(temporal_user)
	password_input = browser.find_element_by_id('password')
	password_input.send_keys(temporal_passwd)
	'''
	user_input = browser.find_element_by_id('user_id')
	user_input.send_keys(USERNAME)
	password_input = browser.find_element_by_id('password')
	password_input.send_keys(PASSWORD)
	browser.find_element_by_id('entry-login').click()
	print('Logging in...')

#Get courses.
def get_courses():
	print('Logged in.')
	browser.get(URL_COURSES)
	div_courses = browser.find_element_by_id('div_22_1')
	sleep(2)
	ul_courses = div_courses.find_element_by_tag_name('ul')
	li_courses = ul_courses.find_elements_by_tag_name('li')
	courses = []

	for course in li_courses:
		course_a = course.find_element_by_tag_name('a')
		course_href = str(course_a.get_attribute('href'))
		courses.append(course_href)

	get_menu(courses)

def get_menu(cs):
	for c in cs:
		print(c)
		browser.get(c)
		sleep(2)
		c_menu = browser.find_element_by_id('courseMenuPalette_contents')
		li_menu = c_menu.find_elements_by_tag_name('li')
		menu = {}

		for item in li_menu:
			a_item = item.find_element_by_tag_name('a')
			href_item = a_item.get_attribute('href')
			s_item = a_item.find_element_by_tag_name('span')
			span = s_item.text
			menu[span.lower()] = href_item

		if 'mi curso' in menu: 
			 print('Course online.')
			 href = menu['mi curso']
			 enter(href)

		elif 'my course' in menu:
			print('Course online.')
			href = menu['my course']
			enter(href)

		else:
			print('Not a course.')
		
def enter(href):
	browser.get(href)
	sleep(2)
	a_el = browser.find_element_by_id('anonymous_element_8')
	my_course = a_el.find_element_by_tag_name('a')
	span_my_course = my_course.find_element_by_tag_name('span').text
	# Except French course.
	exceptions = ['francés I', 'francés II', 'francés III']
	if span_my_course.lower() in exceptions:
		print('We will not take info from French.')
		return
	href_my_course = my_course.get_attribute('href')
	browser.get(href_my_course)
	sleep(2)
	# Check below for differnent browsers or semtrhing.
	nav_bar = browser.find_element_by_class_name('navbar-inner')
	c_nav_bar = nav_bar.find_element_by_class_name('container')
	a_nav_bar = c_nav_bar.find_element_by_tag_name('a').click()
	sleep(1)
	browser.find_element_by_class_name('dropdown-toggle').click()
	drop_menu = browser.find_element_by_class_name('dropdown-menu')
	li_drop_menu = drop_menu.find_elements_by_tag_name('li')

	for li in li_drop_menu:
		a_li = li.find_element_by_tag_name('a')
		href_li = a_li.get_attribute('href')
		t_li = a_li.text.lower()

		if  t_li == 'syllabus':
			print('Syllabus:')
			get_syllabus(href_li)
			break

		elif t_li == 'temario':
			print('Syllabus:')
			get_syllabus(href_li)
			break

		else:
			continue

def get_syllabus(href):
	browser.get(href)
	sleep(1)
	tbody = browser.find_element_by_tag_name('tbody')
	tr_items = tbody.find_elements_by_tag_name('tr')
	main_topics = [
		'topic 1.', 'topic 2.', 'topic 3.', 'topic 4.', 'topic 5.', 'topic 6.',
		'topic 7.', 'topic 8.', 'topic 9.', 'topic 10.', 'topic 11.','topic 12.',
		'topic 13.','topic 14.', 'topic 15.',
		'tema 1.','tema 2.','tema 3.','tema 4.','tema 5.','tema 6.','tema 7.','tema 8.',
		'tema 9.','tema 10.','tema 11.','tema 12.','tema 13.','tema 14.','tema 15.',
	]
	topics = []
	href_bool = False

	for tr in tr_items:
		td_s = tr.find_elements_by_tag_name('td')

		for td in td_s:
			low_td = td.text.lower()

			if low_td in main_topics:
				href_bool = True
			
			elif href_bool:
				a_td = td.find_element_by_tag_name('a')
				href_td = a_td.get_attribute('href')
				topics.append(href_td) 
				href_bool = False

			else:
				continue
		
	get_topic(topics)

def get_topic(topics):

	#Check just a topic. Must iterate later.
	for topic in topics:		

		browser.get(topic)
		sleep(2)
		try:
			ul_tab = browser.find_element_by_id('tab')
		except Exception:
			print('There was an error finding tab. Error: {}'.format(Exception))
			get_info('ok')
			state = False
		else:
			state = True
		if state:

			li_s = ul_tab.find_elements_by_tag_name('li')
			main_tab = ['explanation', u'explicación']
			s_topics = ['topic explanation 1', 'topic explanation 2']

			for li in li_s:
				a_li = li.find_element_by_tag_name('a')
				t_a_li = a_li.text.lower()

				if t_a_li in main_tab:
					print('Were good.')
					get_info('ok')
				elif t_a_li == 'conceptual learning':
					# Check for the other a until topic explnation.
					href_topics = []
					print('Look for topic explanation.')
					a_li.click()
					drop = browser.find_element_by_tag_name('dropdown open')
					ul_drop = drop.find_element_by_tag_name('ul')
					li_s_drop = ul_drop.find_elements_by_tag_name('li')

					for li in li_s_drop:
						s_li = li.find_element_by_tag_name('a')
						a_s_li = s_li.text

						if a_s_li.lower() in s_topics:
							href_s_li = s_li.get_attribute('href')
							href_topics.append(href_s_li)
						else:
							continue
					get_info(href_topics)
				
def store_info():
	# Store on txt file temporarily. Must change file format.
	try:
		main = browser.find_element_by_id('explica')
	except Exception:
		print(Exception)
	else:
		paragraphs = main.find_elements_by_tag_name('p')
		for paragraph in paragraphs:
			try:
				txt_p = paragraph.text.encode('utf-8')
				with open(file_name, 'a+') as file:
					file.write(txt_p)
					file.write('\n')

			except Exception as e:
				print('Something went wrong.')
				print(e)
				continue
		
def get_info(h):
	if h == 'ok':
		sleep(1)
		store_info()
	else:
		for link in h:
			browser.get(link)
			sleep(1)
			store_info()


if __name__ == '__main__':
	main()
	get_courses()
	browser.close()