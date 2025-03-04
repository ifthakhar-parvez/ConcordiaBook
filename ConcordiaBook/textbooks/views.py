from django.shortcuts import render
from .models import Textbook

# Home page view
def home(request):
    return render(request, 'home.html')

def textbooks_for_course(request, course_code):
    # Filter textbooks by course code and availability
    textbooks = Textbook.objects.filter(course_code=course_code, availability=True)
    
    # If no textbooks are found, render no_results.html
    if not textbooks:
        return render(request, 'textbooks/no_results.html', {'course_code': course_code})

    # If textbooks found, render textbooks_list.html
    return render(request, 'textbooks/textbooks_list.html', {'textbooks': textbooks, 'course_code': course_code})
