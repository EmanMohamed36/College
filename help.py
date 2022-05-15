from queue import PriorityQueue
from getpass import getpass
import os
import time
from msvcrt import getch        # for windows users

students_ids = PriorityQueue()
teachers_ids = PriorityQueue()

existance_student_id = [False for i in range(205)]
existance_teacher_id = [False for i in range(205)]

def press_any():
    print("Press any key to return back...", end='')
    getch()
    print()

def Directing():
    print('Redicrecting', end='')
    for i in range(3):
        print('.', end='')
        time.sleep(0.5)
    os.system("cls")

def Returning():
    print('Returning', end='')
    for i in range(3):
        print('.', end='')
        time.sleep(0.5)
    os.system("cls");

def init_student_ids():
    with open("Student.txt", 'r') as student_file:
        for record in student_file:
            fields = record.split('\t')
            existance_student_id[int(fields[0])] = 1;
        for i in range(1, 205, 1):
            if not existance_student_id[i]:
                students_ids.put(i);

def init_teacher_ids():
    with open("Teachers.txt", 'r') as teacher_file:
        for record in teacher_file:
            fields = record.split('\t')
            existance_teacher_id[int(fields[0])] = 1;
        for i in range(1, 205, 1):
            if not existance_teacher_id[i]:
                teachers_ids.put(i);
