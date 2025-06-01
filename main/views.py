from django.shortcuts import render
from .models import About, Award, Advantage, Contact, Tour
from requests import post

BOT_TOKEN = '7419830226:AAGIyVjLFm8AA_eo6D25Bf9ht7CD6iiw5pk'
CHAT_ID = '-1002164984527'


def send_telegram_message(name, phone):
    text = f"📥 Yangi so'rov:\n👤 Ism: {name}\n📞 Telefon: {phone}"
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    payload = {
        'chat_id': CHAT_ID,
        'text': text,
        'parse_mode': 'HTML'
    }
    try:
        response = post(url, data=payload)
        response.raise_for_status()
    except Exception as e:
        print(f"Telegram xabari yuborishda xatolik: {e}")


def index(request):
    contact = Contact.objects.first()
    awards = Award.objects.all()
    tours = Tour.objects.all()
    advantages = Advantage.objects.all()
    about = About.objects.first()
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        send_telegram_message(name, phone)
    return render(request, 'index.html',
                  {'contact': contact, 'awards': awards, 'tours': tours, 'advantages': advantages, 'about': about})
