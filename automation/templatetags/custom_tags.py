from django import template

register = template.Library()


# @register.filter(name="return_item")
def return_item(l, i):
    # print(l,i)
    try:
        return l[i]
    except:
        return None


register.filter("return_item", return_item)


def arange(value):
    return range(value)


register.filter("arange", arange)


def hasIndex(l, i):
    if i < len(l):
        return True
    else:
        return False


register.filter("hasIndex", hasIndex)


def getIndex(l, i):
    if hasIndex(l, i):
        return l[i]


register.filter("getIndex", getIndex)


def readIndex(l, i):
    if type(l) is not type(list()):
        l = list(l)
    if i in l:
        return l.index(i)
    else:
        return -1


register.filter("readIndex", readIndex)


def getType(obj):
    return type(obj)


register.filter("getType", getType)


def isDict(obj):
    # print(">>>> ", obj, True if type(obj) is type(dict()) else False)
    return True if type(obj) is type(dict()) else False


register.filter("isDict", isDict)


def containsDict(obj):
    return True if True in [True if type(item) is type(dict()) else False for item in list(obj.values())] else False
    # print(">>>> ", obj, True if type(obj) is type(dict()) else False)
    # return True if type(obj) is type(dict()) else False


register.filter("containsDict", containsDict)


def getValueOfKey(obj, key):
    return {key: obj[key]}


register.filter("getValueOfKey", getValueOfKey)


def getItemsOfDict(obj):
    return obj.items()


register.filter("getItemsOfDict", getItemsOfDict)


data = {
    "A": {
        "a": [1]*10,
        "aa": [11]*10,
        "aaa": [111]*10,
        "aaaa": [1111]*10,
    },
    "B": {
        "b": [2]*10,
        "bb": [22]*10,
        "bbb": [222]*10,
        "bbbb": [2222]*10,
    },
    "C": {
        "c": [3]*10,
        "cc": [33]*10,
        "ccc": [333]*10,
        "cccc": [3333]*10,
    },
    "D": {
        "d": [4]*10,
        "dd": [44]*10,
        "ddd": [444]*10,
        "dddd": [4444]*10,
    },
    "E": {
        "e": [5]*10,
        "ee": [55]*10,
        "eee": [555]*10,
        "eeee": [5555]*10,
    },
}