"""This module collects user input,
opens the dataset file, compares the user input to our key words,
returning a response based on the intersection of user input and data set keyword.
"""

import os
import csv
import random

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
ANSWERS = os.path.join(THIS_FOLDER, 'answers.txt')


def random_greet():
    """ Returns an item from random_list chosen randomly """
    random_list = ['Hi', 'Hi there', 'Hello',
                   'Here we go', 'I got it', 'Ok', 'Well']
    return random.choice(random_list)


def answers(answer_this):
    """ Takes one argument, answer_this. Opens the csv file, reads the contents
        compares answer_this to csv keywords, returns one list with closest word
        match.
    """

    answer_this = answer_this.lower().split()
    answers_csv = open(ANSWERS, 'r')
    reader = csv.reader(answers_csv, delimiter='|')

    answers_dict = {}
    for row in reader:
        keyword, description, link = row
        answers_dict[keyword] = [description, link]
    answers_csv.close()

    finalists = []
    for k in answers_dict.keys():
        if bool(set(k.split()) & set(answer_this)):
            finalists.append((k, answers_dict[k][0], answers_dict[k][1]))

    if len(finalists) == 0:
        message = (f"Sorry, something went wrong, we don't have that information.\n\n"
                   f'Can I help you with anything else?')
        return message

    else:
        random_one = random.choice(finalists)
        message = (f'{random_greet()}! {random_one[1]} For more information, please visit {random_one[2]}.\n\n'
                   f'Can I help you with anything else?')
        return message


if __name__ == "__main__":
    answer = answers('Python Library')
    print()
    print(answer)
