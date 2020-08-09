import pyperclip

text = pyperclip.paste()

file_name = 'test_file.txt'
with open(file_name, 'a') as f:
    start = 0
    stop = len(text)
    step = int(len(text)/100)
    for i in range(step):
        f.write(text[start:stop])
        start += stop
        stop += stop
