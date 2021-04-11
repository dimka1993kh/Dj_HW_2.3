import datetime

from django.shortcuts import render

from .file import File, Directory

from django.conf import settings


def file_list(request, date=None):
    template_name = 'index.html'
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    files = Directory(settings.FILES_PATH).find_files()
    list_files = list(map(lambda file:
                                        {'name': file['file_name'],
                                        'ctime': file['file_object'].find_datetime_create(),
                                        'mtime': file['file_object'].find_datetime_change()}, 
                                        files))

    context = {
        'files': list_files,
        'date': date  # Этот параметр необязательный
    }

    return render(request, template_name, context)


def file_content(request, name):
    file_content = ''
    with open(request.path[1::], 'r', encoding='utf-8') as file:
        file_content = file.read()

    return render(
        request,
        'file_content.html',
        context={'file_name': name, 'file_content': file_content}
    )