import os
import random
from playsound import playsound
import config

Score = 0
Counter = 0
soundright = os.listdir(config.Right_answer_sound_path)
soundwrong = os.listdir(config.Wrong_answer_sound_path)


def addition(firstnum, secondnum):
    num1 = firstnum
    num2 = secondnum
    global Score, Counter
    print(num1, "+", num2, "=")
    inpt = input()
    if inpt:
        try:
            result = int(inpt)
        except ValueError:
            print("Only integer is accepted")
            result = -1
    else:
        result = -1
    if result == (num1 + num2):
        playsound(config.Right_answer_sound_path + random.choice(soundright))
        Counter += 1
        Score += 10
    else:
        playsound(config.Wrong_answer_sound_path + random.choice(soundwrong))
        Counter += 1
        addition(num1, num2)


def subtraction(firstnum, secondnum):
    num1 = firstnum
    num2 = secondnum
    global Score, Counter
    print(num1, "-", num2, "=")
    inpt = input()
    if inpt:
        try:
            result = int(inpt)
        except ValueError:
            print("Only integer is accepted")
            result = -1
    else:
        result = -1
    if result == (num1 - num2):
        playsound(config.Right_answer_sound_path + random.choice(soundright))
        Counter += 1
        Score += 10
    else:
        playsound(config.Wrong_answer_sound_path + random.choice(soundwrong))
        Counter += 1
        subtraction(num1, num2)


def multipilication(firstnum, secondnum):
    num1 = firstnum
    num2 = secondnum
    global Score, Counter
    print(num1, "×", num2, "=")
    inpt = input()
    if inpt:
        try:
            result = int(inpt)
        except ValueError:
            print("Only integer is accepted")
            result = -1
    else:
        result = -1
    if result == (num1 * num2):
        playsound(config.Right_answer_sound_path + random.choice(soundright))
        Counter += 1
        Score += 10
    else:
        playsound(config.Wrong_answer_sound_path + random.choice(soundwrong))
        Counter += 1
        multipilication(num1, num2)


def devision(firstnum, secondnum):
    num1 = firstnum
    num2 = secondnum
    global Score, Counter
    print(num1, "÷", num2, "=")
    inpt = input()
    if inpt:
        try:
            result = int(inpt)
        except ValueError:
            print("Only integer is accepted")
            result = -1
    else:
        result = -1
    if result == (num1 / num2):
        playsound(config.Right_answer_sound_path + random.choice(soundright))
        Counter += 1
        Score += 10

    else:
        playsound(config.Wrong_answer_sound_path + random.choice(soundwrong))
        Counter += 1
        devision(num1, num2)


while True:
    # Initilizing first and second numbers for each operations, and call for testing functions.
    # For choose which operations you want to train and range for them, please look at the config.py
    operator = random.choice(config.Operations)
    if operator == "+":
        First_num = random.randint(config.Range_addition1[0], config.Range_addition1[1])
        Second_num = random.randint(config.Range_addition2[0], config.Range_addition2[1])
        addition(First_num, Second_num)

    elif operator == "-":
        First_num = random.randint(config.Range_subtraction1[0], config.Range_subtraction1[1])
        Second_num = random.randint(config.Range_subtraction2[0], min(First_num, config.Range_subtraction2[1]))
        subtraction(First_num, Second_num)

    elif operator == "×":
        First_num = random.randint(config.Range_multiplication[0], config.Range_multiplication[1])
        if First_num == 0:
            Second_num = random.randint(config.Range_multiplication0[0], config.Range_multiplication0[1])
        elif First_num == 1:
            Second_num = random.randint(config.Range_multiplication1[0], config.Range_multiplication1[1])
        elif First_num == 2:
            Second_num = random.randint(config.Range_multiplication2[0], config.Range_multiplication2[1])
        elif First_num == 3:
            Second_num = random.randint(config.Range_multiplication3[0], config.Range_multiplication3[1])
        elif First_num == 4:
            Second_num = random.randint(config.Range_multiplication4[0], config.Range_multiplication4[1])
        elif First_num == 5:
            Second_num = random.randint(config.Range_multiplication5[0], config.Range_multiplication5[1])
        elif First_num == 6:
            Second_num = random.randint(config.Range_multiplication6[0], config.Range_multiplication6[1])
        elif First_num == 7:
            Second_num = random.randint(config.Range_multiplication7[0], config.Range_multiplication7[1])
        elif First_num == 8:
            Second_num = random.randint(config.Range_multiplication8[0], config.Range_multiplication8[1])
        elif First_num == 9:
            Second_num = random.randint(config.Range_multiplication9[0], config.Range_multiplication9[1])
        elif First_num == 10:
            Second_num = random.randint(config.Range_multiplication10[0], config.Range_multiplication10[1])
        multipilication(First_num, Second_num)

    elif operator == "÷":
        devidor = random.randint(config.Range_devidor[0], config.Range_devidor[1])
        if devidor == 1:
            Second_num = random.randint(config.Range_devision_result1[0], config.Range_devision_result1[1])
        elif devidor == 2:
            Second_num = random.randint(config.Range_devision_result2[0], config.Range_devision_result2[1])
        elif devidor == 3:
            Second_num = random.randint(config.Range_devision_result3[0], config.Range_devision_result3[1])
        elif devidor == 4:
            Second_num = random.randint(config.Range_devision_result4[0], config.Range_devision_result4[1])
        elif devidor == 5:
            Second_num = random.randint(config.Range_devision_result5[0], config.Range_devision_result5[1])
        elif devidor == 6:
            Second_num = random.randint(config.Range_devision_result6[0], config.Range_devision_result6[1])
        elif devidor == 7:
            Second_num = random.randint(config.Range_devision_result7[0], config.Range_devision_result7[1])
        elif devidor == 8:
            Second_num = random.randint(config.Range_devision_result8[0], config.Range_devision_result8[1])
        elif devidor == 9:
            Second_num = random.randint(config.Range_devision_result9[0], config.Range_devision_result9[1])
        elif devidor == 10:
            Second_num = random.randint(config.Range_devision_result10[0], config.Range_devision_result10[1])
        First_num = Second_num * devidor
        devision(First_num, Second_num)
    else:
        continue

    # Displaying Score
    if Counter == 10:
        message = "Your Score for 10 Questions is:  " + str(Score)
        print(message)
        Counter = 0
        Score = 0
