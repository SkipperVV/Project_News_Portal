from django import template

register = template.Library()

bad_word = {
    "редиска": "р******",
    "редиски": "р******",
    "какашка": "к******",
    "какашки": "к******",
}


@register.filter()
def censor(value: str) -> str:

    for i in bad_word.keys():
        value = value.lower().replace(i, bad_word[i])
    return f"{value}"