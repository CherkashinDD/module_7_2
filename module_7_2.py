def custom_write(file_name, strings):
    strings_positions = {}
    f_n_write = open(file_name, 'w', encoding='utf-8')
    for index, string in enumerate(strings, start=1):
        byte_position = f_n_write.tell()
        f_n_write.write(string + '\n')
        strings_positions[(index, byte_position)] = string
    return strings_positions


info = [
    'Text for tell.',
    'Используйтекодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
