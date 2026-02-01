# read file contents
with open('myTextFile.txt', 'r') as file:
    content = file.read()
    print(content)

# read file line by line
with open('myTextFile.txt', 'r') as file:
    for line in file:
        print(line.strip())


# read file 
file = open('myTextFile.txt', 'r')
content = file.readlines()
for line in content:
    print(line.strip())
file.close()    




