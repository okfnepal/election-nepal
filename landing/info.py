from django.shortcuts import get_object_or_404
from .models import SiteInformation


def siteinfo(request):
    try:
        siteinfo = SiteInformation.objects.get(pk=1)
    except:
        siteinfo = "not found "

    return {'siteinfo': siteinfo}
