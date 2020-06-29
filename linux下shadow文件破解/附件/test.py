import crypt

def testPass(cryptPass):
    salt = cryptPass[0:20]
    try:
        dictFile = open('dictionary', 'r')
        try:
            for word in dictFile.readlines():
                word = word.strip('\n')
                cryptWord = crypt.crypt(word, salt)
                if cryptWord == cryptPass:
                    print('[+] Found Password: ' + word + "\n")
                    return
            print('[-] Password not Found.\n')
            return
        except:
            dictFile.close()
    except:
        print('[-] dictionary can not OPEN')
        exit(0)



def main():
    try:
        passFile = open('shadow')
        try:
            for line in passFile.readlines():
                if ":" in line:
                    user = line.split(':')[0]
                    cryptPass = line.split(':')[1].strip(' ')
                    print('[*] Cracking Password For : ' + user)
                    testPass(cryptPass)
        except:
            passFile.close()
    except:
        print('[-] shadow CAN not open')

if __name__ == '__main__':
    main()
