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


def equals(operand_01, operand_02):
    return operand_01 == operand_02


register.filter("equals", equals)


def hasContent(item):
    return True if item is not None else False


register.filter("hasContent", hasContent)

