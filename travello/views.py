from django.shortcuts import render

# Create your views here.
from .models import Destination


def index(request):

    '''dest1 = Destination()
    dest1.name = 'Ahmedabad'
    dest1.desc = 'The City That Never Sleeps'
    dest1.img = 'destination_1.jpg'
    dest1.price = 700
    dest1.offer = True

    dest2 = Destination()
    dest2.name = 'Mehsana'
    dest2.desc = 'For Farming You Can Come'
    dest2.img = 'destination_2.jpg'
    dest2.price = 650
    dest2.offer = False

    dest3 = Destination()
    dest3.name = 'Surat'
    dest3.desc = 'Moj-Sokh ne khani pini surti lala sahelani'
    dest3.img = 'destination_3.jpg'
    dest3.price = 670
    dest3.offer = True

    dest4 = Destination()
    dest4.name = 'Baroda'
    dest4.desc = 'Your Vadodara'
    dest4.img = 'destination_4.jpg'
    dest4.price = 660
    dest4.offer = True

    dest5 = Destination()
    dest5.name = 'Kutch'
    dest5.desc = 'Salty Desert'
    dest5.img = 'destination_5.jpg'
    dest5.price = 698
    dest5.offer = True

    dest6 = Destination()
    dest6.name = 'Junagadh'
    dest6.desc = 'The Girnar Mountain'
    dest6.img = 'destination_6.jpg'
    dest6.price = 630
    dest6.offer = False

    dests = [dest1, dest2, dest3, dest4, dest5, dest6]'''

    dests = Destination.objects.all()

    return render(request, 'index.html', {'dests': dests})
