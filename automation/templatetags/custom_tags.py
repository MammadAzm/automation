from django import template

register = template.Library()


# @register.filter(name="return_item")
def return_item(l, i):
    try:
        return l[i]
    except:
        return None


register.filter("return_item", return_item)
