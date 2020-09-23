from store import data
from operator import itemgetter

data2 = [
{
"first_name": "Nikolay",
"Last_name": "Ivanov",
"age": 43,
"gender": "M",
"last_salary_up_day": "2016/01/31"
}
]
#1
def getName(): 
    for i in data:
        print(i["first_name"])

#2
def getEmployeesOver30YearsOld(): 
    employeeList = []
    for i in data:
        if int(i["age"]) > 30:
            employeeList.append(i)
    return employeeList

#3
def getSurnameOnS(): 
    employeeList = []
    for i in data:
        if i["Last_name"].startswith("S"):
            employeeList.append(i)
    return employeeList

#4
def getFemales():
    employeeList = []
    for i in data:
        if i["gender"] == "F":
            employeeList.append(i)
    return employeeList

#5
def getFemalesLess30YearsOld():
    employeeList = []
    for i in data:
        if i["gender"] == "F" and int(i["age"]) < 30:
            employeeList.append(i)
    return employeeList

#6
def getNamesAndSurnamesOver30YearsOld():
    nameList = []
    for i in data:
        if int(i["age"]) > 30:
            name = {
                "first_name": i["first_name"],
                "last_name": i["Last_name"]
                }
            nameList.append(name)

    return nameList

#7
def sortByAge():
    dataCopy = data.copy()
    dataCopy.sort(key=itemgetter("age"))
    print(dataCopy)

#8
def sortByName():
    dataCopy = data.copy()
    dataCopy.sort(key=itemgetter("first_name"))
    print(dataCopy)

#9
def sortByAgeReverse():
    dataCopy = data.copy()
    dataCopy.sort(key=itemgetter("age"), reverse = True)
    print(dataCopy)
    
#getName()
#print(getEmployeesOver30YearsOld())
#print(getSurnameOnS())
#print(getFemales())
#print(getFemalesLess30YearsOld())
#print(getNamesAndSurnamesOver30YearsOld())
#sortByAge()
#sortByName()
#sortByAgeReverse()

