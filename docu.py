d={"Eno":123,"Ename":"abc"}
print(d)
print(d["Eno"])
print(d.get("Ename"))
d["Ename"]="xyz"
print(d)
d["age"]=19
print(d)
for key in d:
     print(key)
for value in d:
    print(value)
