import PyPDF2 as pd
filename = input('Path to the file: ')
file = open(filename,'rb')
pdfReader = pd.PdReader(file)

tried = 0

if not pdfReader.is_encrypted:
    print('The file is not password protected! You can successfully open it!')
else:
    wordlistFile = open("wordlist.txt","r",errors = "ignore")
    body = wordlistFile.read().lower()
    words = body.split("\n")
    for i in range(len(words)):
        word = words[i]
        print("Tryin to decode the password by  {}".format(word))
        result = pdfReader.decrypt(word)
        if result == 1:
            print("success the passowrd is {}".format(word))
            break
        elif result == 0:
            tried +=1
            print("password tried"+str(tried))
            continue

            


