from django.shortcuts import render

# Cadastro de médico

def cadastro_medico(request):
  if request.method == "GET":
    return render(request, 'cadastro_medico.html')