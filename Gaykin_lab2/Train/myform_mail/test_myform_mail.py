from unittest import TestCase

from myform_mail import match_mail


class Test(TestCase):
    def test_match_mail_true(self):
        emails = ["gajkin.kirill@yandex.ru", "kirill.new@gmail.com", "yuriy@mail.com", "sasha@gmail.com", "alexandra.haskova@yandex.ru",
                  "kirill.gaykin@gmail.com", "ricardrajonhart@gmail.com", "vovapupkin@mail.com", "genius877@yandex.ru", "vasilievskiy.central@yandex.ru"];
        for i in emails:
            self.assertTrue(match_mail(i), f"{i} mail is not valid")

    def test_match_mail_false(self):
        emails = ["1", "kirill", "@", "@gmail", "kiriLL@gmail", "kirill.gmail.com", "kirill.ru", "kirill@.ru",
                  "kirill@gmailcom", "kirill@gmail.r", "kirill@gmail.comma", "123456789"];
        for i in emails:
            self.assertFalse(match_mail(i), f"{i} mail is valid")
