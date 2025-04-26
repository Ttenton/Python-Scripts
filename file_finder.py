import os

def finder(name_or_ext, start_dir):
    found = False
    for root, dirs, files in os.walk(start_dir):
        for file in files:
            if file == name_or_ext or file.endswith(name_or_ext):
                full_path = os.path.join(root, file)
                print(f'[+] PATH FOUND: {full_path}')
                found = True
    if not found:
        print('[-] FILE NOT FOUND -_-')


def main():
    search = input('Enter file name or ext: ')
    start_dir = input('Enter start directory: ')
    finder(search, start_dir)
    




if __name__ == '__main__':
    main()
