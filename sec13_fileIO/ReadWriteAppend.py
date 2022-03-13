
# mode r-read,
# w-write, rewrite the whole thing
# r+-read and writing,
# a-append at the end

# with open('test.txt', mode='a') as my_file:
#     text = my_file.write('\nyeah yeah')
#     print(text)

with open('sad.txt', mode='w') as my_file:  # create a new file
    text = my_file.write(':(')
    print(text)
