# coding=UTF-8

import zipfile
import threading


def extractfile(file, password):
    try:
        file.extractall(pwd=password)
        print('Found Password:', password)
        return password
    except:
        pass


def main():
    with open('file.config', 'r') as f:
        files = f
    for file in files.read().splitlines():
        if file == '':
            continue
        zfile = zipfile.ZipFile(file=file)
        with open('passdics.config', 'r') as f:
            passdics = f
        for passdic in passdics.read().splitlines():
            if passdic == '':
                continue
            with open(passdic, 'r') as f:
                passwords = f
                for password in passwords:
                    t = threading.Thread(target=extractfile, args=(zfile, password))
                    t.start()


if __name__ == '__main__':
    main()
