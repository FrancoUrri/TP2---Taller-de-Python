def second_word_start_with_vowel(text):
	text_list = text.split("\n")
	vowels = ("A", "E", "I", "O", "U", "a", "e", "i", "o", "u")
	text_list_filtered = [line for line in text_list if line.split()[1][0] in vowels]
	text_filtered = ""
	for line in text_list_filtered:
		text_filtered += (line + "\n")
	print(text_filtered)

def has_more_words(texts):
    long_text = texts[0]
    for text in texts:
        if len(long_text.split()) < len(text.split()):
            long_text = text
    print(f'El título más largo es: "{long_text}"')
    
def contains_word(sentences, word):
	sentences_list = sentences.split(".\n")
	for sentence in sentences_list:
		if word in sentence:
			print(sentence)