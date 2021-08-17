import os
import platform
import time

def clear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def checkluhn(cardnumber):
    nDigits = len(cardnumber)
    nSum = 0
    isSecond = False
    for i in range(nDigits - 1, -1, -1):
        d = ord(cardnumber[i]) - ord('0')
        if (isSecond == True):
            d = d * 2
        nSum += d // 10
        nSum += d % 10
        isSecond = not isSecond
    if (nSum % 10 == 0):
        return True
    else:
        return False
if __name__=="__main__":
    clear()
    time.sleep(1)
    cardnumber = input("\nIngresa la tarjeta de credito >>> ")
    if (checkluhn(cardnumber)):
        time.sleep(1)
        print("\nLa tarjeta es valida")
    else:
        time.sleep(1)
        print("\nLa tarjeta no es valida")