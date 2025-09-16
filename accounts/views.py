from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import datetime
from django.db.models import Q
import matplotlib
from travello.models import Client
from travello.models import Hotel
from travello.models import Destination
from travello.models import Tour
from travello.models import Transaction
from travello.models import Promo
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
import requests
import matplotlib.pyplot as plt
import base64
from io import BytesIO
from django.shortcuts import render
matplotlib.use('Agg')  # <-- важно!


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Invalid credentials.')
            return redirect('login')

    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name', '').strip()
        last_name = request.POST.get('last_name', '').strip()
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username is already taken.")
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered.")
            return redirect('register')

        user = User.objects.create_user(
            username=username,
            password=password1,
            email=email,
            first_name=first_name,
            last_name=last_name
        )
        user.save()

        Client.objects.create(
            user=user,
            patronymic='',
            address='',
            phone=''
        )

        messages.success(request, "User successfully created. Please log in.")
        return redirect('login')

    return render(request, 'register.html')



def logout(request):
    auth.logout(request)
    return redirect('/')


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


def news(request):
    return render(request, 'news.html')


def destinations(request):
    return render(request, 'destinations.html')

@login_required
def destination_detail(request, pk):
    destination = get_object_or_404(Destination, pk=pk)
    hotels = destination.hotel_set.all()

    weather_data = None
    exchange_rate = None

    # Получение данных о погоде
    try:
        weather_api_key = 'b1ca3822e5a24817bf1172711252605'
        city_name = destination.name
        weather_url = f'http://api.weatherapi.com/v1/current.json?key={weather_api_key}&q={city_name}&lang=ru'
        weather_response = requests.get(weather_url)
        if weather_response.status_code == 200:
            weather_data = weather_response.json()
    except Exception:
        weather_data = None

    # Получение курса валюты EUR -> USD
    try:
        exchange_url = 'https://api.exchangerate.host/latest?base=EUR&symbols=USD'
        exchange_response = requests.get(exchange_url)
        if exchange_response.status_code == 200:
            exchange_data = exchange_response.json()
            exchange_rate = exchange_data.get('rates', {}).get('USD')
    except Exception:
        exchange_rate = None

    if request.method == "POST":
        try:
            client = Client.objects.get(user=request.user)

            selected_hotels = request.POST.getlist('hotels[]')
            if not selected_hotels:
                messages.error(request, "Пожалуйста, выберите хотя бы один отель.")
                return redirect(request.path)

            hotel = get_object_or_404(Hotel, pk=selected_hotels[0])

            duration_weeks = int(request.POST.get('duration'))
            start_date_str = request.POST.get('start_date')

            try:
                start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
            except (ValueError, TypeError):
                messages.error(request, "Некорректный формат даты начала тура.")
                return redirect(request.path)

            promo_code = request.POST.get('promo_code', '').strip()
            promo = Promo.objects.filter(code=promo_code, active=True).first() if promo_code else None

            tour = Tour(
                client=client,
                destination=destination,
                hotel=hotel,
                start_date=start_date,
                duration_weeks=duration_weeks,
                promo=promo
            )
            tour.save()

            transaction = Transaction(
                client=client,
                tour=tour,
                amount=tour.total_price
            )
            transaction.save()

            messages.success(request, 'Tour successfully booked and transaction recorded!')
            return redirect('destination_detail', pk=pk)

        except Client.DoesNotExist:
            messages.error(request, "Клиент не найден.")
        except Exception as e:
            print(f"Ошибка при бронировании тура: {e}")
            messages.error(request, f"Ошибка при бронировании тура: {e}")

    return render(request, 'destination_detail.html', {
        'dest': destination,
        'hotels': hotels,
        'weather': weather_data,
        'exchange_rate': exchange_rate,
    })



def travel_news(request):
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": "travel",
        "language": "en",
        "apiKey": "ВАШ_API_КЛЮЧ"
    }
    try:
        response = requests.get(url, params=params)
        data = response.json()
        articles = data.get("articles", [])[:5]  # Возьмем только 5 новостей
    except Exception as e:
        articles = []
    return render(request, "news.html", {"articles": articles})

def news(request):
    url = 'https://newsapi.org/v2/everything'
    params = {
        'q': 'travel OR tourism',  # ищем любые новости про туризм
        'language': 'en',          # можно заменить на 'ru' при желании
        'sortBy': 'publishedAt',
        'apiKey': 'aff4ee7a196245428da2a4d5b4be6943'
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()
        articles = data.get('articles', [])[:10]  # максимум 10 свежих новостей
    except Exception as e:
        print(f"[ERROR] Failed to load travel news: {e}")
        articles = []

    return render(request, 'news.html', {'articles': articles})

@login_required
def stats_page(request):
    return render(request, 'stats.html')

@login_required
def stats_image(request):
    transactions = Transaction.objects.all().order_by('purchase_date')

    data = {}
    for t in transactions:
        # Группировка по часу
        date_hour_str = t.purchase_date.strftime('%Y-%m-%d %H:00')
        data[date_hour_str] = data.get(date_hour_str, 0) + float(t.amount)

    # Сортировка по времени
    sorted_items = sorted(data.items())
    dates = [item[0] for item in sorted_items]
    amounts = [item[1] for item in sorted_items]

    # Построение графика
    plt.figure(figsize=(12, 6))
    plt.plot(dates, amounts, marker='o')
    plt.title('Сумма покупок по часам')
    plt.xlabel('Дата и час')
    plt.ylabel('Сумма ($)')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()
    buffer.seek(0)

    return HttpResponse(buffer.getvalue(), content_type='image/png')

def search_destinations(request):
    query = request.GET.get('city', '').strip()
    results = []

    if query:
        results = Destination.objects.filter(name__icontains=query)

    return render(request, 'search_destinations.html', {'results': results, 'query': query})
