from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Review
from users.models import User
from .forms import ReviewForm

# Create your views here.

def main(request):
    return render(request, 'pages/MainPage.html')

def Route_1(request):
    reviews = Review.objects.all()  # Получаем все отзывы

    stars_range = range(1, 6)  # Диапазон от 1 до 5
    return render(request, 'pages/Route_1.html', {'reviews': reviews, 'stars_range': stars_range})

def Route_2(request):
    return render(request, 'pages/Route_2.html')

def Route_3(request):
    return render(request, 'pages/Route_3.html')

def Route_4(request):
    return render(request, 'pages/Route_4.html')

def Route_5(request):
    return render(request, 'pages/Route_5.html')

#def AddReview(request):
#    return render(request, 'pages/html3.html')

@login_required
def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('Route_1')
    else:
        form = ReviewForm()

    return render(request, 'pages/html3.html', {'form': form})

