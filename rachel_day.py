"""
    KGS Research Junior Software Engineer Test
    File: rachel_day.py
    Date: 07/09/2021

    Answers are below the questions.

"""

def delete_duplicates(list):
    unique = []
    for element in list:
        if not(element in unique):
            unique.append(element)
    return unique


def score_probablity(statement):
    key_words = ['age', 'year', 'born', 'date of birth']
    words_total = 0
    occurrences = 0
    for word in statement:
        words_total += 1
        if (word in key_words):
            occurrences += 1
    return (occurrences / words_total) > 0.7


""" QUESTIONS
Write three different solutions to the function below.
Please use different algorithms and ensure none are brute force.

def is_ordered(list):
    '''
    (list[int]) --> boolean

    Determine if a list of elements are in ascending order.

    >>> is_ordered([1, 1, 1, 1, 1])
    >>> True
    >>> is_ordered([1, 2, 3])
    >>> True
    >>> is_ordered([7, -4, 8, 12, 0])
    >>> False
    '''
    pass

Given the text stream:
```
1.  What is your age?

1.  18 - 34
2.  35- 44
3.  45- 54
4.  55-64
5.  Over 65
6.  Don't know

2.  What province do you live in?

1.  Ontario
2.  Quebec
3.  Manitoba
4.  Alberta
5.  Other (specify)
```
Write a function to parse out a file with a text stream of this format to create the following variables:
Questions = ['What is your age?', 'What province do you live in?']
QuestionNumbers = ['1', '2']
Answpers = [['18-34', '35-44', '45-54', 'Over 65', 'Don't know'], ['Ontario', 'Quebec', 'Manitoba', 'Alberta', 'Other (specify)']]
AnswerNumbers[['1', '2', '3', '4', '5', '6'], ['1', '2', '3', '4', '5']]

Please ensure your function works even if the questions and answers change! If you need to make any assumptions (you may need to), please note them.
"""

# ANSWERS

def is_ordered1(list):
    """
    Determines if a list of elements are in ascending order.

    Args:
        list -- list[int]

    Returns:
        boolean

    """
    dup_list = list

    sorted_list = dup_list[:]
    sorted_list.sort()

    return (sorted_list == dup_list)


def is_ordered2(list):
    """
    Determines if a list of elements are in ascending order.

    Args:
        list -- list[int]

    Returns:
        boolean

    """

    return (list == sorted(list))


def is_ordered3(list):
    """
    Determines if a list of elements are in ascending order.

    Args:
        list -- list[int]

    Returns:
        boolean

    """

    return all(list[i] <= list[i +1] for i in range(len(list)-1))


def parse_file(file_name):
    """
    Parse file and returns questions, answers and their corresponding numbers

    Args:
        file_name -- string, file name of text stream

    Returns:
        dict of requested variable arrays 
        [Questions, QuestionNumbers, Answers, AnswerNumbers]

    Assumptions:
        - Assumes all questions have a '?' mark AND assumes all answers do not
        - Assumes numbers are followed by a '.'
        
    """
    questions = []
    question_numbers = []
    answers = []
    answer_numbers = []

    with open(file_name) as file:
        line = file.readline()
        while line:
            line = file.readline()

            if "." in line:
                temp = line.split(".", 1)

                if "?" in line:
                    questions.append(temp[1].strip())
                    question_numbers.append(temp[0])

                else:
                    answers.append(temp[1].strip())
                    answer_numbers.append(temp[0])


    file_vars = dict()
    file_vars['Questions'] = questions
    file_vars['QuestionNumbers'] = question_numbers
    file_vars['Answers'] = answers
    file_vars['AnswerNumbers'] = answer_numbers

    return file_vars


# TESTS

print("Q1. All is_ordered functions should return: True, True, False")
print("is_ordered1:", is_ordered1([1, 1, 1, 1, 1]), is_ordered1([1, 2, 3]), is_ordered1([7, -4, 8, 12, 0]))
print("is_ordered2:", is_ordered2([1, 1, 1, 1, 1]), is_ordered2([1, 2, 3]), is_ordered2([7, -4, 8, 12, 0]))
print("is_ordered3:", is_ordered3([1, 1, 1, 1, 1]), is_ordered3([1, 2, 3]), is_ordered3([7, -4, 8, 12, 0]))

print("\n")

print("Q2. Function should create 4 variables: Questions, QuestionNumbers, Answers, AnswerNumbers")
q = parse_file('file.txt')

print("Questions:", q['Questions'])
print("QuestionNumbers:", q['QuestionNumbers'])
print("Answers:", q['Answers'])
print("AnswerNumbers:", q['AnswerNumbers'])