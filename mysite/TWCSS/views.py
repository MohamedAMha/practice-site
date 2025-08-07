from django.shortcuts import render
def tailwindcss(request):
    template = "case.html"
    return render(request, template)  # apparently I can just ommit the context, since I'm not passing variables