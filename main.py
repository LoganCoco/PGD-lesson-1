student={
"name" : "Logan",
"age" : 12,
"hobby" : "football"
}
print(student)
print(student["age"])
print(student ["name"])
print (student.keys())

print(student.values())
for key in student.keys():
    print(key,":",student[key])
if "marks" in student:
    print("key exists")
else:
    print("key does not exist")

student["favSubject"]="English"

print(student)

del (student["hobby"])

print(student)

choice=input("choose your favourite subject")

student["favSubject"]=choice

print(student)

student["marks"]=[98,67,90,94,100]
print(student)

print(student["marks"][2])

classroom={
"James":{
    "age" : 12,
    "hobby" : "Dancing"
},
"Olivia" : {
    "age":11,
    "hobby":"Singing"
}
}
print(classroom)
print(classroom.keys())

print(classroom.values())