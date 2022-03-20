import os

path = 'files\\'
files = []
for file in os.listdir(path):
    path_to_file = os.path.join(path, file)
    current_file_list = []
    with open(path_to_file, 'r', encoding='utf-8') as current_file:
        current_text = current_file.readlines()
        current_len = len(current_text)
        files.append([current_len, file, current_text])

# создаем/очищаем файл с результатом
with open('result.txt', 'w', encoding='utf-8') as output_file:
    pass

with open('result.txt', 'a', encoding='utf-8') as output_file:
    for file in sorted(files):
        print(file[1], file=output_file)
        print(file[0], file=output_file)
        print(*file[2], sep='', file=output_file)
