

def encrypt(text, shift):
    characters = 'abcdefghijklmnopqrstuvwxyz'
    result = ""
    for i in range(len(text)):
        charnum = characters.find(text.lower()[i])
        newcharnum = charnum + shift
        if newcharnum >= 26:
            newcharnum -= 26
        newcharletter = characters[newcharnum]
        result += newcharletter
    return result


if __name__ == '__main__':
    print("=========================")
    print("====CAESAR ENCRYPTION====")
    print("=========================")
    i = int(input('Enter \n1 to start \n0 to end \nNumber: '))
    while i == 1:
        print("====PROGRAM STARTED====")
        txt = input("Enter text to encrypt: ")
        shft = int(input("Enter number to shift: "))
        res = encrypt(txt, shft)
        print("Encrypted text is: " + res)
        print("====THANK YOU FOR USING THIS PROGRAM====")
        i = int(input('Enter \n1 to start \n0 to end \nNumber: '))
    print("====PROGRAM ENDED====")

