3) Challenge #3
We have a nested object, we would like a function that you pass in the object and a key and get back the value. How this is implemented is up to you.
 
Example Inputs
object = {“a”:{“b”:{“c”:”d”}}}
key = a/b/c
 
object = {“x”:{“y”:{“z”:”a”}}}
key = x/y/z
value = a
 
Hints
We would like to see some tests. A quick read to help you along the way
 
We would expect it in any other language apart from elixir.

						

Solution Approach:
Used python to code this 

Used links : https://stackoverflow.com/questions/9807634/find-all-occurrences-of-a-key-in-nested-dictionaries-and-lists
https://stackoverflow.com/questions/1305532/how-to-convert-a-nested-python-dict-to-object

The example is :

>>> d = {'a': 1, 'b': {'c': 2}, 'd': ["hi", {'foo': "bar"}]}
Should be accessible in this way:
>>> x = dict2obj(d)
>>> x.a
1
>>> x.b.c
2
>>> x.d[1].foo
bar

This is a nested python dict to object .

Uploaded the code to https://github.com/pattanaiksrimani/Challanges_UK/blob/main/Challange-3.py
Testing :

Copy the code to any instance where python is installed :

Output/testing of the script :

[ec2-user@ip-172-31-22-154 ~]$ cat challange3.py
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
[ec2-user@ip-172-31-22-154 ~]$ python3 challange3.py
d d d
[ec2-user@ip-172-31-22-154 ~]$
