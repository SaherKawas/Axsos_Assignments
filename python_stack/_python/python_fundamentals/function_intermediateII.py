# Change value

def changeValue(x):
    for i in range(len(x)):  
        for j in range(len(x[i])):  
            if x[i][j] == 10: 
                x[i][j] = 15 
    return x

x = [ [5,2,3], [10,8,9] ]
print (changeValue(x))

# Change last name

def changeLaststname(students):
    for i in range(len(students)):
        if students[i] ["first_name"] == "Michael":
            students[i]["last_name"]= "Bryant"
        return students
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}]
print(changeLaststname(students))

# Change name

def changeName(sports_directory):
    for i in range(len(sports_directory["soccer"])):
        if sports_directory["soccer"][i]=="Messi":
            sports_directory["soccer"][i]="Andres"
        return sports_directory
    
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']}

print(changeName(sports_directory))

# Change value

def changeValue(z):
    for i in range(len(z)):
        if z[i]["y"]==20:
            z[i]["y"]=30
        return z
z = [ {'x': 10, 'y': 20} ]
print(changeValue(z))

# # Iterate Through a List of Dictionaries

def iterateDictionary(students):
    for i in range(len(students)):
         for key in students[i]:
            print(f"{key}: {students[i][key]}", end=", ")
    
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
print(iterateDictionary(students))

# Get Values From a List of Dictionaries

def iterateDictionary2(first_name, students):
    for i in students:  
        print(i[first_name])

    

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
iterateDictionary2("first_name", students)

# iterate 2

def iterateDictionary2(last_name, students):
    for i in students:  
                print(i[last_name])
    

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
iterateDictionary2("last_name", students)

# Iterate Through a Dictionary with List Values

def printInfo(dojo):
    for key in dojo:
        print(len(dojo[key]), key)
        for value in dojo[key]:
            print(value)
      
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)