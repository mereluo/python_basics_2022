my_file = open('test.txt')

# print(my_file.read())  # my name is meredith luo
# print(my_file.read())  # the cursor is at the end
# my_file.seek(0)
# print(my_file.read())  # my name is meredith luo

print(my_file.readline())  # my name is meredith luo
print(my_file.readline())  # how are you
print(my_file.readline())  # :)

my_file.seek(0)
# ['my name is meredith luo\n', 'how are you\n', ':)']
print(my_file.readlines())

my_file.close()
