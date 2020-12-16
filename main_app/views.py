from django.shortcuts import render

from django.http import HttpResponse

# Add the Finch class & list and view function below the imports
class Finch:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, description, age):
    self.name = name
    self.description = description
    self.age = age

finches = [
  Finch('Lolo', 'foul little demon', 3),
  Finch('Sachi','diluted tortoise shell', 0),
  Finch('Raven', '3 legged bird', 4)
]

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
  return render(request, 'about.html')

def finches_index(request):
  return render(request, 'finches/index.html', { 'finches': finches })
