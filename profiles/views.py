from django.shortcuts import render
from .models import PensionersDetails
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned


# Create your views here.

def index(request):
    try:
        id = request.GET.get('id', 'system')
        print(id)

        if id == 'system':
            return render(request, 'empty.html')
        else:
            int(id)

        print(id)

        pensioner = PensionersDetails.objects.get(id=id)
        print(pensioner.name)


        return render(request, 'index.html', {'pensioner': pensioner})

    except ObjectDoesNotExist:
        return render(request, '404.html')


