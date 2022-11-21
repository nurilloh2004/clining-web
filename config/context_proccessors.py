from clining.models import Settings

def all_category(request):
    return {
        "phone":Settings.objects.get(key='phone').value,
        "openhour":Settings.objects.get(key='openhour').value,
        "location":Settings.objects.get(key='location').value,
        "extra_phone1":Settings.objects.get(key='extra_phone1').value,
        "extra_phone2":Settings.objects.get(key='extra_phone2').value,
        "facebook":Settings.objects.get(key='facebook').value,
        "telegram":Settings.objects.get(key='telegram').value,
        "instagram":Settings.objects.get(key='instagram').value,
        "youtube":Settings.objects.get(key='youtube').value,
    }