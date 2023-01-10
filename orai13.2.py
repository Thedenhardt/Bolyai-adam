def mysplit(string):
    if string == "":
        return []
    else:
        return string.split(" ")
print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))

