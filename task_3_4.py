string = str(input())

mid = len(string) // 2

print(string[mid])

if string[0] == string[mid]:
    stringPart = string[1:(len(string) - 1)]
    print(stringPart)