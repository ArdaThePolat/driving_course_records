import datetime

def readFile(file_path):
    file = []
    try:
        with open(file_path["path"], file_path["readMode"]) as text_file:
            content = text_file.read()
            for row in content.split('\n'):
                if row != '':
                    file.append(row)
    except:
        print('Error while reading file!')
    return file

def writeToFile(file_path, data):
    try:
        with open(file_path["path"], file_path["writeMode"]) as text_file:
            for row in data:
                text_file.write(row + '\n')
    except:
        print('Error while writing to file!')
        return False
    return True

def checkAge(birthDate):
    try:
        age = datetime.datetime.now().year - birthDate.year
        if age < 18:
            return False
        else:
            return True
    except Exception as e:
        print("Something went wrong:", str(e))
        return False

def calculatePayment(birthDate):
    try:
        age = datetime.datetime.now().year - birthDate.year
        if 18 <= age <= 25:
            return 3000
        elif age > 25:
            return 4000
        else:
            return 0
    except Exception as e:
        print("Something went wrong:", str(e))
        return 0

def addStudent(list):
    numberOfStudents = int(input("Enter number of students you want to add: "))
    for i in range(numberOfStudents):
        name = input("Enter name: ")
        surname = input("Enter surname: ")
        studentId = 0
        keepGoing = True
        while keepGoing:
            keepGoing = False
            tempId = int(input("Enter student id: "))
            for row in list:
                if int(row.split(',')[2]) == tempId:
                    print("Student with same id already exists!")
                    keepGoing = True
                    continue
            if not keepGoing:
                studentId = tempId
        id = int(input("Enter id: "))
        phoneNumber = int(input("Enter phone number: "))
        birthDate = datetime.datetime.strptime("31.05.2023", "%d.%m.%Y")
        while not checkAge(birthDate):
            tempDate = datetime.datetime.strptime(input("Enter birth date (format: 31.05.2023): "), "%d.%m.%Y")
            if not checkAge(tempDate):
                print("Student should be at least 18 years old!")
                continue
            birthDate = tempDate
        payment = calculatePayment(birthDate)
        customer = name+"," + surname+"," + str(studentId)+"," + str(id)+"," + str(phoneNumber)+"," + str(birthDate)+"," + str(payment)
        list.append(customer)
    writeToFile(path, list)

def deleteStudent(list):
    stdId = int(input("Enter the student id of student you want to delete: "))
    for row in list:
        newRow = row.split(',')
        if int(newRow[2]) == stdId:
            list.remove(row)
            print("Student deleted!")
            break
    writeToFile(path, list)

def updateStudent(list):
    stdId = int(input("Enter the student id of student you want to update: "))
    stdFoundFlag = False
    for row in list:
        newRow = row.split(',')
        if int(newRow[2]) == stdId:
            newRow[0] = input("Enter name: ")
            newRow[1] = input("Enter surname: ")
            newRow[2] = 0
            keepGoing = True
            while keepGoing:
                keepGoing = False
                tempId = int(input("Enter student id: "))
                for trow in list:
                    if int(trow.split(',')[2]) == tempId and int(row.split(',')[2]) != tempId:
                        print("Student with same id already exists!")
                        keepGoing = True
                        continue
                if not keepGoing:
                    newRow[2] = tempId
                    
            newRow[3] = int(input("Enter id: "))
            newRow[4] = int(input("Enter phone number (format: 05555555555): "))
            newRow[5] = datetime.datetime.strptime("31.05.2023", "%d.%m.%Y")
            while not checkAge(newRow[5]):
                tempDate = datetime.datetime.strptime(input("Enter birth date (format: 31.05.2023): "), "%d.%m.%Y")
                if not checkAge(tempDate):
                    print("Student should be at least 18 years old!")
                    continue
                newRow[5] = tempDate
            newRow[6] = int(input("Enter new remaning payment: "))
            list[list.index(row)] = newRow[0]+"," + newRow[1]+"," + str(newRow[2])+"," + str(newRow[3])+"," + str(newRow[4])+"," + str(newRow[5])+"," + str(newRow[6])
            print("Student updated!")
            stdFoundFlag = True
            break
    if not stdFoundFlag:
        print("Student not found!")
    writeToFile(path, list)
        

def searchStudent(list):
    stdId = int(input("Enter the student id of student you want to search: "))
    for row in list:
        row = row.split(',')
        if int(row[2]) == stdId:
            print("Name: "+row[0] + '\nSurname: ' + row[1] + '\nStudent ID: ' + row[2] + '\nID: ' + row[3] + '\nPhone Number: ' + row[4] + '\nBirth Date: ' + row[5] + '\nPayment: ' + row[6] + '\n\n')
            return
    print("Student not found!")

def listStudents(list):
    for row in list:
        row = row.split(',')
        print("Name: "+row[0] + '\nSurname: ' + row[1] + '\nStudent ID: ' + row[2] + '\nID: ' + row[3] + '\nPhone Number: ' + row[4] + '\nBirth Date: ' + row[5] + '\nPayment: ' + row[6] + '\n\n')

def makePayment(list):
    stdId = int(input("Enter the student id of student you want to make payment for: "))
    for row in list:
        newRow = row.split(',')
        if int(newRow[2]) == stdId:
            payment = 5000
            while payment > int(newRow[6]):
                payment = int(input("Enter payment (maximum amount should not exceed remaning payment) : "))
            newRow[6] = int(newRow[6]) - payment
            list[list.index(row)] = newRow[0]+"," + newRow[1]+"," + str(newRow[2])+"," + str(newRow[3])+"," + str(newRow[4])+"," + str(newRow[5])+"," + str(newRow[6])
            print("Payment made, remaning amount that needs to be paid: " + str(newRow[6]) + " TL")
            break
    writeToFile(path, list)

def exit():
    print("Goodbye!")
    quit()

def callMenu(file):
    while True:
        print("1. Add Student")
        print("2. Delete Student")
        print("3. Update Student")
        print("4. Search Student")
        print("5. List Students")
        print("6. Make Payment")
        print("7. Exit")
        try:
            choice = int(input("Enter your choice: "))
        except:
            print("Invalid choice!")
            continue
        if choice < 1 or choice > 7:
            print("Invalid choice!")
            continue
        match choice:
            case 1:
                addStudent(file)
                continue
            case 2:
                deleteStudent(file)
                continue
            case 3:
                updateStudent(file)
                continue
            case 4:
                searchStudent(file)
                continue
            case 5:
                listStudents(file)
                continue
            case 6:
                makePayment(file)
                continue
            case 7:
                exit()
                break
            
        


path = {'path':'kayit.txt', 'readMode':'r', 'writeMode':'w'}
file = readFile(path)
callMenu(file)
