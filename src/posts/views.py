from django.shortcuts import render

# Create your views here.
def home_view(request):
    ##---- Carreguem el template amb els paràmetres ----##
    
    # Param 2: Carraguem el template#
    # Param 3: Enviem dades al template.
    
    return render(request, 'posts/main.html', {'pepe':'Hello World'}) 