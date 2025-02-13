'''
Faith Burgette
Program - High Ranking Student 
This program will be able to determine if the student
made either the Dean's List or Honour Role.
'''
#varialbles
gpa = 0
last_name = ''
first_name = ''
student = []


#user input infor
while True:
    last_name = input("Enter the student's last name: ")
    if last_name.upper() == 'ZZZ':
        break
    first_name = input("Enter student's first name: ")
    gpa = float(input("Enter student's GPA: "))    
    
    if gpa >= 3.5:  #Deans list
        print('This student made the Deans List.')
    elif 3.25 <= gpa < 3.5 : #honor roll range
        print('This student made the Honor Roll.')
    else:
        print('This student did not recieve any academic achievements.')
        