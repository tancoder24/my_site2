from django.shortcuts import render

# Create your views here.
def example_view(request):
    return render(request, 'my_app/example.html')

def variable_view(request):

    my_var = {
        "first_name": "Tanmay",
        "last_name": "Gupta",
        "some_list": [1,2,4],
        "some_dict": {
                "some_key": "some_value"
            }
    }

    return render(request, 'my_app/variable.html',context=my_var)