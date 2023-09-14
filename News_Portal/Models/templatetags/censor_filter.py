from django import template

register = template.Library()

bad_word = {
    "редиска": "р******",
    "редиски": "р******",
    "редиску": "р******",
    "какашка": "к******",
    "какашки": "к******",
    "какашку": "к******",
    "гадкий ": "г******",
    "гадкие ": "г******",
    "гадкая ": "г******",
    "гадкое ": "г******",
}


@register.filter()
def censor(value: str) -> str:
    for i in bad_word.keys():
        if i in value:
            value = value.lower().replace(i, bad_word[i])
    return f"{value}"
