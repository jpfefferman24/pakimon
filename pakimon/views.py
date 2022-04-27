from django.shortcuts import redirect

def redirectBlank(request):
    response = redirect('/play/')
    return response
