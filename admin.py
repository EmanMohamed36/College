from help import *

def admin():
    print('1- sign in  ')
    print('2- return back  ')
    Reg_sign = print('choose: ')

    if Reg_sign == 2:
        Returning()
    else :
        Directing()
        print('Admin page: ')
        print('Enter: ')
        id = input('ID: ')
        password = input('Password: ')
        Directing()
        found = 1
        if found:
            while 1:
                print('Admin Page: ')
                print('choose: ')
                print('1- Control Teacher',end = '')
                print('2- Control Student',end = '')
                print('3- Log out')
                Admin_choice = input('Choice: ')
                #if Admin_choice == 1:
                #control teacher
                
                
                if Admin_choice == 2:
                    #control student
                    while 1:
                        print('Admin Page (Control Student)')
                        print('choose: ')
                        print('1- Show All Student ',end = '')
                        print('2- Search Student ',end = '')
                        print('3- Add ',end = '')
                        print('4- Remove ',end = '')
                        print('5- Edit ',end = '')
                        print('6- Return ')
                        Ad_Stud_choice = input('Choise: ')
                                                


                



