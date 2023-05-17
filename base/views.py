from django.shortcuts import render

import re

def landing(request):

    MOBILE_AGENT_RE=re.compile(r".*(iphone|mobile|androidtouch)",re.IGNORECASE)

    if MOBILE_AGENT_RE.match(request.META['HTTP_USER_AGENT']):
        return render(request, 'landing_mobile.html')
    else:
        return render(request, 'landing_desktop.html')
        

def qa(request):
    return render(request, 'q&a.html')

def why_us(request):
    return render(request, 'why_us.html')