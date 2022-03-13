from translate import Translator

translator = Translator(to_lang="zh")

try:
    with open('test.txt', mode='r') as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        with open('test-ch.txt', mode='w') as my_file_ch:
            my_file_ch.write(translation)
except FileNotFoundError:
    print('check your file path silly!')
