from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response
from .serializers import AboutSerializer, AwardSerializer, AdvantageSerializer, ContactSerializer, TourSerializer, \
    LeadSerializer
from .models import About, Award, Advantage, Contact, Tour
from requests import post


class AboutList(ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer

    def get(self, request, *args, **kwargs):
        return Response(AboutSerializer(About.objects.first()).data)


class AdvantageList(ListAPIView):
    queryset = Advantage.objects.all()
    serializer_class = AdvantageSerializer


class AwardList(ListAPIView):
    queryset = Award.objects.all()
    serializer_class = AwardSerializer


class ContactList(ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def get(self, request, *args, **kwargs):
        return Response(ContactSerializer(Contact.objects.first()).data)


class TourList(ListAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer


class LeadCreate(CreateAPIView):
    serializer_class = LeadSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        name = request.data.get("name")
        phone = request.data.get("phone")
        send_telegram_message(name, phone)
        return Response(serializer.data, status=201)


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
