##
# Example Inputs
# object = {“a”:{“b”:{“c”:”d”}}}
# key = a/b/c
##
# object = {“x”:{“y”:{“z”:”a”}}}
# key = x/y/z
# value = a

def getKeys(obj: dict):
    keys = list(obj)
    if len(keys) != 1:
        raise Exception('Multiple or Empty Doctionary found ')
    else:
        return keys[0]


def getNestedObjValue(obj: dict, key: str, isFound = False):
    # print(obj, key, isFound)
    if type(obj) is not dict and not isFound:
        #return None
         print('Not a nested Object')
    if (isFound or (key in obj.keys())) :
        if type(obj[key]) is dict:
            return getNestedObjValue(obj[key], getKeys(obj[key]), True)
        else:

            return obj[getKeys(obj)]
    else:
        nestedKey = getKeys(obj)
        return getNestedObjValue(obj[nestedKey], key, False)

if __name__ == '__main__':
    obj = {'a': {'b': {'c': 'd'}}}
    value = getNestedObjValue(obj, 'a')
    value1 = getNestedObjValue(obj, 'b')
    value2 = getNestedObjValue(obj, 'c')

    print(value,value1,value2)
