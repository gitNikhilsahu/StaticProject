from django.shortcuts import render
from datetime import datetime

def TimeInfo(request):
    date_now = datetime.now()
    name = 'NareshIT-HYDERABAD'
    th = int(date_now.strftime('%H'))
    if th < 12:
        wish = "Good Morning Buddy"
    elif th > 16:
        wish = "Good Afternoon Dude"
    else:
        wish = "Good Night Guys-Sleep Well"
    Py_Dict = {'date_now': date_now, 'name': name, 'wish': wish}
    return render(request, 'MyApp/Welcome.html', context=Py_Dict)
