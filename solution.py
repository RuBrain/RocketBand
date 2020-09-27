from store import data
from operator import itemgetter
from datetime import datetime, timedelta


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
    for employee in data:
        if datetime.now() - timedelta(days=1825) >= datetime.strptime(employee['last_salary_up_day'], '%Y/%m/%d'):
            employees.append(employee)
    return employees

#11
def sortBySalaryUpReverse():
    return sorted(data, key=itemgetter('last_salary_up_day'), reverse = True)

#12
def listToDict():
    result = {}
    for employee in data:
        result['{}:{}'.format( employee['first_name'], employee['Last_name'] )] = {
            'age': employee['age'],
            'gender': employee['gender'],
            'last_salary_up_day': employee['last_salary_up_day']
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
    result = {}
    for employee in enumerate(data):
        result['{}.{}:{}'.format( employee[0], employee[1]['first_name'], employee[1]['Last_name'] )] = {
            'age': employee[1]['age'],
            'gender': employee[1]['gender'],
            'last_salary_up_day': employee[1]['last_salary_up_day']
        }
    return result

#15
def getEmployeesNameAndLastnameMoreThan12Symbols():
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

print(listToDictWithCounter())
