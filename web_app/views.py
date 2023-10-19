from django.shortcuts import render, redirect
from .models import User

def character_selection(request):
    if request.method == 'POST':
        selected_character = request.POST.get('selected_character')
        user = User.objects.get(user_id=333142671)
        user.character = selected_character
        user.save()
        return redirect('character_selection')
    else:
        return render(request, 'character_selector.html')
