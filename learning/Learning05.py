file_Project = open('text', mode='r', encoding='UTF-8')
contents = file_Project.read()
print(contents)


with open('text', mode='a', encoding='UTF-8') as file_Project2:
    file_Project2.write('Ok！I get it \n')
    print(file_Project2)

