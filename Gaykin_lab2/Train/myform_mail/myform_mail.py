import re


def match_mail(mail):
    if re.match(r"^[a-zA-Z-_.0-9]+@[a-zA-Z-_.0-9]+\.(?=.{2,3}$)[a-z]+", mail):
        return True
    else:
        return False

