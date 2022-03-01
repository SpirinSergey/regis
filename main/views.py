from django.shortcuts import render
from django.db.models import Q
from main.models import Gallery
from main.models import Listing


def index(request):
    return render(request, 'main/pages/index.html')


def about(request):
    return render(request, 'main/pages/about.html')


def developers(request):
    return render(request, 'main/pages/developers.html')


def amenities(request):
    return render(request, 'main/pages/amenities.html')


def gallery(request):
    gal_img = Gallery.objects.all()
    return render(request, 'main/pages/gallery.html', context={'gal_img': gal_img})


def listings(request):
    unit_type = request.GET.get('unit_type')
    view = request.GET.get('view')
    if unit_type or view:
        listing_object = Listing.objects.filter(Q(UNIT_TYPE__icontains=unit_type) & Q(BATHROOMS__icontains=view))
    else:
        listing_object = Listing.objects.all()
    return render(request, 'main/pages/listings.html', context={'listing_object': listing_object})


def contact(request):
    return render(request, 'main/pages/contacts.html')


def privacy(request):
    return render(request, 'main/privacy-policy.html')


def disclaimer(request):
    return render(request, 'main/disclaimer.html')
