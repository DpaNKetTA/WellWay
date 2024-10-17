from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Review, Review3, Review5, Review2, Review4
from users.models import User
from .forms import ReviewForm, ReviewForm2, ReviewForm3, ReviewForm4, ReviewForm5

# Create your views here.

def main(request):
    return render(request, 'pages/MainPage.html')

def Route_1(request):
    reviews = Review.objects.all()  # Получаем все отзывы

    stars_range = range(1, 6)  # Диапазон от 1 до 5
    return render(request, 'pages/Route_1.html', {'reviews': reviews, 'stars_range': stars_range})

def Route_2(request):
    reviews = Review2.objects.all()  # Получаем все отзывы

    stars_range = range(1, 6)  # Диапазон от 1 до 5
    return render(request, 'pages/Route_2.html', {'reviews': reviews, 'stars_range': stars_range})
def Route_3(request):
    reviews = Review3.objects.all()  # Получаем все отзывы

    stars_range = range(1, 6)  # Диапазон от 1 до 5
    return render(request, 'pages/Route_3.html', {'reviews': reviews, 'stars_range': stars_range})
def Route_4(request):
    reviews = Review4.objects.all()  # Получаем все отзывы

    stars_range = range(1, 6)  # Диапазон от 1 до 5
    return render(request, 'pages/Route_4.html', {'reviews': reviews, 'stars_range': stars_range})
def Route_5(request):
    reviews = Review5.objects.all()  # Получаем все отзывы

    stars_range = range(1, 6)  # Диапазон от 1 до 5
    return render(request, 'pages/Route_5.html', {'reviews': reviews, 'stars_range': stars_range})
#def AddReview(request):
#    return render(request, 'pages/html3.html')

@login_required
def add_review(request):
    if request.method == 'POST':
        selected_route = request.POST.get('route')

        if selected_route == 'Маршрут 1':
            form = ReviewForm(data=request.POST)
            print (form.is_valid())
            print (form.errors)
            if form.is_valid():
                review = form.save(commit=False)
                review.user = request.user
                review.save()
                return redirect('Route_1')

        elif selected_route == 'Маршрут 2':
            form = ReviewForm2(data=request.POST)
            print(form.is_valid())
            print(form.errors)
            if form.is_valid():
                review = form.save(commit=False)
                review.user = request.user
                review.save()
                return redirect('Route_2')

        elif selected_route == 'Маршрут 3':
            form = ReviewForm3(data=request.POST)
            print(form.is_valid())
            print(form.errors)
            if form.is_valid():
                review = form.save(commit=False)
                review.user = request.user
                review.save()
                print('qwerty')
                return redirect('Route_3')

        elif selected_route == 'Маршрут 4':
            form = ReviewForm4(data=request.POST)
            print(form.is_valid())
            print(form.errors)
            if form.is_valid():
                review = form.save(commit=False)
                review.user = request.user
                review.save()
                print('qwerty')
                return redirect('Route_4')

        elif selected_route == 'Маршрут 5':
            form = ReviewForm5(data=request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.user = request.user
                review.save()
                print('qwerty')
                return redirect('Route_5')

    else:
        form = ReviewForm()

    return render(request, 'pages/html3.html', {'form': form})

