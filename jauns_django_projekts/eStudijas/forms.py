from django.forms import (
    Form,
    CharField,
)


class CreateStudentForm(Form):

    name = CharField()
    grades = CharField()