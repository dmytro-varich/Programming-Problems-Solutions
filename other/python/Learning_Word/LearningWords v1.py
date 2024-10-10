import os
from random import choice
from tabulate import tabulate

incorrect_lst = []

def open_file(path) -> dict: 
    with open(path, 'r', encoding='utf-8') as my_file:
        lines = my_file.readlines()

    lst = [(item.rstrip().split(" - ")) for item in lines]
    # print(lst)
    translation_dict = {}
    for item in lst:
    	slovakian_word, russian_translation = item[0], item[1]
    	translation_dict[slovakian_word] = russian_translation
    return translation_dict

def random_word(dict_words) -> str:
	random_value = choice(list(dict_words.values()))
	return random_value

def remove_word(answer, ru_word, dict_words) -> dict:
	new_dict = dict(dict_words)
	for slovakian_word, russian_translation in dict_words.items():
		if (answer == slovakian_word or answer != slovakian_word) and ru_word == russian_translation:
			del new_dict[slovakian_word]
	return new_dict

def check_answer(answer, word, dict_words):
    global incorrect_lst 
    correct_word = ''
    for slovakian_word, russian_translation in dict_words.items():
    	if (answer == slovakian_word and word == russian_translation): 
    		return 1  
    	if russian_translation == word: 
        	correct_word = slovakian_word
    incorrect_lst.append((word, answer, correct_word))
    return 0

def game(dict_words):
    i, point = 1, 0
    length = len(dict_words)
    while i <= length:
    	# print(dict_words)
    	word = random_word(dict_words)
    	answer = input(f"{i}. {word} - ").strip()
    	if answer == "stop": break
    	point += check_answer(answer, word, dict_words) 
    	dict_words = remove_word(answer, word, dict_words) 
    	i += 1
    print()
    print(f"Your result is {point}/{length}. ({int((point/length) * 100)} %)")
    table = tabulate(incorrect_lst, headers=["Translate Word", "Your Answer", "Correct Word"], tablefmt="pretty")
    print("Incorrect Answers:")
    print(table)
    print()
    user_input = input("Press 'Q' to exit or 'R' to restart: ")

    while user_input.strip().lower() not in ['r', 'q']:
        print("Invalid input. Please press 'Q' or 'R'.")
        user_input = input("Press 'Q' to exit or 'R' to restart: ")
    
    if user_input.strip().lower() == 'q':
        print("Exiting the program. Goodbye!")
    elif user_input.strip().lower() == 'r':
        print("Restarting the program.")
        os.system('cls')
        menu_start()
        

def menu_start():
    global incorrect_lst
    incorrect_lst = []
    print("""Welcome to our «LearningWords» program!""")
    print()
    print("---------------------------------------------")
    print("| The file must have the following format:  |")
    print("|-------------------------------------------|")
    print("| Foreign word - Translation                |")
    print("| Foreign word - Translation                |")
    print("| Foreign word - Translation                |")
    print("| ...                                       |")
    print("|___________________________________________|")
    print()

    file_path_input = input('Please copy and paste the full file path here to the dictionary file (for example: "C:\\Users\\admin\\Desktop\\dictionary.txt"): ')
    file_path_input = file_path_input.strip('"')
    file_path = r"{}".format(file_path_input)
    dict_words = open_file(file_path)
    game(dict_words)


if __name__ == '__main__':
    menu_start()
