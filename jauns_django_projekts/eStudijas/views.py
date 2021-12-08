from django.shortcuts import render
from .forms import CreateStudentForm
from .models import StudentModels


def add_student(request):

    form = CreateStudentForm(request.POST or None)

    if request.method == 'POST':

        if form.is_valid():

            grades_string = form.grades
            grades_int_list = list(map(int, grades_string.split(',')))

            student = StudentModels(
                student=form.cleaned_data['student'],
                grades=grades_int_list,
                average_grade=sum(form.grades) / len(form.grades)
            )

            student.save()

            context = {
                'student': student,
            }

            return render(
                request,
                template_name='student.html',
                context=context,
            )

    context = {
        'form': form,
    }

    return render(
        request,
        template_name='add_student.html',
        context=context,
    )
