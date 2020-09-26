from store import data
from operator import itemgetter
from datetime import date
import datetime

#1
def getNames(): 
    names = []
    for employee in data:
        names.append(employee['first_name'])
    return names

#2
def getEmployeesOverAge(age=30): 
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
def getFemalesUnderAge(age=30):
    employeeList = []
    for employee in data:
        if employee['gender'] == 'F' and int(employee['age']) < age:
            employeeList.append(employee)
    return employeeList

#6
def getNamesAndLastnamesOverAge(age=30):
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
    
#10
def getEmployeesWithoutSalaryIncrease5years():
    employees = []
    currentDate = date.today()
    fiveYearsAgoDate = datetime.date(currentDate.year - 5, currentDate.month, currentDate.day)
    for employee in data:
        lastSalaryUp = employee['last_salary_up_day'].split('/')
        lastSalaryUpDate = datetime.date(int(lastSalaryUp[0]), int(lastSalaryUp[1]), int(lastSalaryUp[2]))
        if lastSalaryUpDate < fiveYearsAgoDate:
            employees.append(employee) 
    return employees

#11
def sortBySalaryUpReverse():
    return sorted(data, key=itemgetter('last_salary_up_day'), reverse = True)

#12
def listToDict():
    result = {}
    for item in data:
        # result[item['first_name'] + ':' + item['Last_name']] = {
        result['{}:{}'.format( item['first_name'], item['Last_name'] )] = {
            'age': item['age'],
            'gender': item['gender'],
            'last_salary_up_day': item['last_salary_up_day']
        }
    return result   

#13
def getLastnamesStartsSOver20(): 
    employeeList = []
    for employee in data:
        if employee['Last_name'].startswith('S') and employee['age'] > 20 \
                        and employee['gender'] == 'M':
            employeeList.append(employee)
    return employeeList

#14
def listToDictWithCounter():
    counter = 1
    result = {}
    for employee in data:
        # result[employee['first_name'] + ':' + employee['Last_name']] = {
        result['{}.{}:{}'.format( counter, employee['first_name'], employee['Last_name'] )] = {
            'age': employee['age'],
            'gender': employee['gender'],
            'last_salary_up_day': employee['last_salary_up_day']
        }
        counter += 1
    return result

#15
def getEmployeesNameAndSurnameMoreThan12Symbols():
    employees = []
    for employee in data:
        if len(employee['first_name'] + employee['Last_name']) > 12:
            employees.append(employee)
    return employees

#16
def sumOfAges():
    count = 0
    for employee in data:
        count += employee['age']
    return count