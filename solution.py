from store import data
from operator import itemgetter

#1
def getNames(): 
    names = []
    for employee in data:
        names.append(employee['first_name'])
    return names

#2
def getEmployeesOver30YearsOld(age=30): 
    employeeList = []
    for employee in data:
        if int(employee['age']) > age:
            employeeList.append(employee)
    return employeeList

#3
def getLastnamesStartsS(): 
    employeeList = []
    for employee in data:
        if employee['Last_name'].startswith('S'):
            employeeList.append(employee)
    return employeeList

#4
def getFemales():
    employeeList = []
    for employee in data:
        if employee['gender'] == 'F':
            employeeList.append(employee)
    return employeeList

#5
def getFemalesUnder30YearsOld(age=30):
    employeeList = []
    for employee in data:
        if employee['gender'] == 'F' and int(employee['age']) < age:
            employeeList.append(employee)
    return employeeList

#6
def getNamesAndLastnamesOver30YearsOld(age=30):
    nameList = []
    for employee in data:
        if int(employee['age']) > age:
            name = '{} {}'.format(employee['first_name'], employee['Last_name'])
            nameList.append(name)
    return nameList

#7
def sortByAge():
    return sorted(data, key=itemgetter('age'))

#8
def sortByName():
    return sorted(data, key=lambda employee: employee['first_name'])

#9
def sortByAgeReverse():
    return sorted(data, key=itemgetter('age'), reverse = True)
    
# print(getNames())
# print(getEmployeesOver30YearsOld())
# print(getLastnamesStartsS())
# print(getFemales())
# print(getFemalesLess30YearsOld())
# print(getFemalesUnder30YearsOld())
# print(getNamesAndLastnamesOver30YearsOld())
# print(sortByAge())
# print(sortByName())
# print(sortByAgeReverse())

