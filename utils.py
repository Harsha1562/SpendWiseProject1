import re


def check_date(date):
    pattern = r"^\d{4}-\d{2}-\d{2}$"

    if re.match(pattern, date):
        return True
    else:
        return False


def create_id(number):
    return "EXP-" + str(number).zfill(3)


def make_tags(text):
    tags = set()

    words = text.split(",")

    for word in words:
        word = word.strip().lower()

        if word != "":
            tags.add(word)

    return tags
