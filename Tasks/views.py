from django.shortcuts import render

# Create your views here.  # in the book it lists it AS INDEX.PY

#view for index page




def connection(request):

    return render(request, 'en/public/connection.html')

def page(request):
        my_variable = "Hello World !"
        years_old = 15
        array_city_capitale = [ "Paris", "London", "Washington" ]
        return render(request, 'en/public/index.html', { "my_var":my_ variable, "years":years_old, "array_city":array_city_capitale })