from django.urls import path
from . import views

urlpatterns = [
    path('', views.sudoku, name='sudoku-home'),
    path('about/', views.about, name='sudoku-about'),
    path('puzzlify/', views.puzzlify, name='sudoku-puzzler'),
    path('solution/', views.solution, name='sudoku-solution'),
    path('puzzle/', views.showPuzzle, name='sudoku-puzzle'),
]