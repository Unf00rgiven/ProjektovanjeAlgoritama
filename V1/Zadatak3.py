def func(string1,string2):
    returnString=""
    returnString+=string1[:3]+string1[:3]+string2[len(string2)-3:]+string2[len(string2)-3:]
    return returnString