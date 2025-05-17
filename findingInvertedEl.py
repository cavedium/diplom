def NSD(a, b):
	while b:
		temp = a % b
		a = b
		b = temp
	return a

def invertedElement(a, b):
    fTemp = 0
    sTemp = 1
    if a < 0:
        a = a % b
    if NSD(a, b) == 1:
        while(True):
            intNumber = b // a
            remainder = b - (a* intNumber)
            invertedEl = fTemp - (sTemp * intNumber)
            if remainder == 1:
                return invertedEl
            b = a
            a = remainder
            fTemp = sTemp
            sTemp = invertedEl
        return invertedEl
    else:
         return False

number= int(input("Enter your number: "))
module = int(input("Enter your module: "))

if invertedElement(number, module) == False:
    print(f"{number} is not have inverted element!")
else:
    print(f"{number} inverted element is ", invertedElement(number, module))