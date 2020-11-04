def encryption01():
    while True:
        print("*************************************")
        print("Welcome to Encryptor Version 0.1")
        print("*************************************")
        print(" Select an option")
        print("1. Encryption")
        print("2. Decryption")
        user = int(input("Option Selected : "))
        if user == 1:
            input_text = input("Enter the text to be encrypted : ")
            encrypt = ""

            for i in input_text:
                i = i + "*#"
                encrypt = encrypt + i

            print(encrypt[::-1])

            user2 = input("Try again ? :")
            if user2 == "Y":
                encryption01()
            else:
                exit()
        elif user == 2:
            input_text = input("Enter the text to be decrypted : ")
            decrypt = ""

            for i in input_text:
                if i != "#":
                    if i != "*":
                        decrypt = decrypt + i

            print(decrypt[::-1])

            user2 = input("Try again ? :")
            if user2 == "Y":
                encryption01()
            else:
                exit()

        else:
            print("Sorry wrong option ")


encryption01()









