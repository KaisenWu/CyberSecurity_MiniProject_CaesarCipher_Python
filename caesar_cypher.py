#!/usr/bin/python

# Define the function to display the header.
def showHeader():
    print("-------------------------------------")
    print("CyberSecurity_MiniProject: Caesar Cipher")
    print("Created by Kaisen Wu")
    print("-------------------------------------")

# Define the function to allow users choose the options.
def chooseOption():
    userOption = ""
    while userOption != "1" and userOption != "2":
        userOption = input("Do you want to 1) Encrypt 2) Decrypy?")
    return userOption

# Define the function to get the rotation number users want to implement.. 
def getEncryptRotation():
    encryptNum = 0
    while encryptNum < 1 or encryptNum > 26:
        encryptInput = input("Enter the nunmber of shifting to cipher [between 1 to 26]:")
        while encryptInput.isnumeric() == False:
            print("PLease enter the integer between the range")
            encryptInput = input("Enter the nunmber of shifting to cipher [between 1 to 26]:")
        encryptNum = int(encryptInput)
    return encryptNum

# Define the function to get the file name which users would like to encrypt.
def getEncryptFileName():
    return input("Enter the filename to encrypt: ")

# Define the function to show the original text from the specific file, then store it as a list.
def showOriginalMessageThenGetOriginalList(fileName):
    print("Original message is:")
    file = open(fileName, 'r')
    orgMsg = file.read()
    orgMsgList = orgMsg.split("\n")[:-1]
    print(orgMsg)
    file.close()
    return orgMsgList

# Define the function to get the decrypt rotation from the user.
def getDecryptRotation():
    encryptNum = 0
    while encryptNum < 1 or encryptNum > 26:
        encryptInput = input("Enter the nunmber of shifting that was done to cipher [between 1 to 26]:")
        while encryptInput.isnumeric() == False:
            print("Please enter the integer between the range")
            encryptInput = input("Enter the nunmber of shifting to cipher [between 1 to 26]:")
        encryptNum = int(encryptInput)
    return encryptNum

# Define the function to get the file name which users would like to decrypt.
def getDecryptFileName():
    return input("Enter the filename to decrypt: ")

# Define the functon to encrypt the text and display it.
def encryptMsgThenDisplay(orgMsgList, encryptRotation):
    encryptedMsgList = []
    for line in orgMsgList:
        newLine = ""
        for char in line:
            ascii_num = ord(char)
            if ascii_num >= 97 and ascii_num <=122:
                new_ascii = ascii_num + encryptRotation
                if new_ascii > 122:
                    new_ascii = new_ascii - 26
                newLine = newLine + chr(new_ascii)
            else:
                newLine = newLine + chr(ascii_num)
        encryptedMsgList.append(newLine)
    print("Encrypted message is:")
    for line in encryptedMsgList:
        print(line)
    return encryptedMsgList

# Define the function to decrypt the texts.
def decryptMsgThenDisplay(encryptedMsgList, decryptRotation):
    decryptedMsgList = []
    for line in encryptedMsgList:                                   
        newLine = ""
        for char in line:
            ascii_num = ord(char)                                             
            if ascii_num >= 97 and ascii_num <= (122+decryptRotation-26):
                new_ascii = ascii_num + 26 - decryptRotation
            elif ascii_num == 32:
                new_ascii = ascii_num
            else:
                new_ascii = ascii_num - decryptRotation
            newLine = newLine + chr(new_ascii)
        decryptedMsgList.append(newLine)
    print("Decrypted message is:")
    for line in decryptedMsgList:
        print(line)                
    return decryptedMsgList

# Define the function to output the message as a txt file.
def outputMsg(msgList):
    file = open("CaesarCypher_Output.txt", 'w')
    for line in msgList:
        file.writelines(line + "\n")
    file.close()

# Define the function to get content of the file which useres want to decrypt, then display the texts.
def inputEncryptedMsgThenDisplay(fileName):
    print("Original message is:")
    file = open(fileName, 'r')
    encryptedMsg = file.read()
    encryptedMsgList = encryptedMsg.split("\n")[:-1]
    print(encryptedMsg)
    file.close()
    return encryptedMsgList

# Define the function to implement all functions.
def implemente():
    showHeader()
    userOption = chooseOption()
    if userOption == "1":
        encryptRotation = getEncryptRotation()
        fileName = getEncryptFileName()
        print()
        orgMsgList = showOriginalMessageThenGetOriginalList(fileName)
        encryptedMsgList = encryptMsgThenDisplay(orgMsgList, encryptRotation)
        outputMsg(encryptedMsgList)
    else:
        decryptRotation = getDecryptRotation()
        fileName = getDecryptFileName()
        print()
        encryptedMsgList = inputEncryptedMsgThenDisplay(fileName)
        decryptedMsgList = decryptMsgThenDisplay(encryptedMsgList, decryptRotation)
        outputMsg(decryptedMsgList)

implemente()

