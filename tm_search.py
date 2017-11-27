# -*-encoding: utf-8 -*-

# import nltk
# CHECK NLTK

def main(question):
	main_questions = ['what', 'who', 'where', 'when', 'how', ]
	non_important = ['¿','?']
	new_question = []
	for word in question.split(' '):
		word = word.lower()
		if word.lower() in main_questions:
			continue
		elif word in non_important:
			continue
		else:
			new_question.append(word)

	return ' '.join(new_question) 

def read(question):
	print(question)
	'''
	with open('ws.txt', 'r') as f:
		f.read()
		# CHECK MMAP
	'''


if __name__ == '__main__':
	print('START')
	question = raw_input('Enter your question here: ')
	n_question = main(question)
	read(n_question)