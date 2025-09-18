from django.shortcuts import render

def home(request):
    ctx = {
        'course': 'IT373 - Web Systems and Technologies 2',
        'week': 1,
    }
    return render(request, 'pages/home.html', ctx)

def about(request):
    ctx = {
        'name': 'Mark Lawrence P. Lacdao',
        'student_id': '2023-02427',
    }
    return render(request, 'pages/about.html', ctx) 

