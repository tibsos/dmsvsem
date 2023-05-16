from django.shortcuts import render

from datetime import datetime as dt

def landing(request):

    # analytics

    datetime = dt.now()

    user_agent = request.META.get('HTTP_USER_AGENT') or request.headers['User-Agent']

    ip = request.META.get('REMOTE_ADDR')

        # get country and city

    cookies = request.COOKIES

    # create an analytics model

    print(datetime)
    print(user_agent)
    print(ip)
    print(cookies)

    return render(request, 'landing.html')