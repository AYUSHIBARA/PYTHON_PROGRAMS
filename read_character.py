with open('example.txt', 'r', encoding='utf-8') as file:
    while True:
        char = file.read(1)

        if not char:
            print('Reached end of file')
            break

        print(char)
