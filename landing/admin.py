from django.contrib import admin
from mezzanine.pages.admin import  PageAdmin

from landing.models import SiteInformation,AboutUs,Visualization,Data,Data_template,Visualization_template
# Register your models here.

admin.site.register(SiteInformation)


class SiteInformationAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        base_add_permission = super(SiteInformationAdmin, self).has_add_permission(request)
        if base_add_permission:
            count = SiteInformation.objects.all().count()
            if count == 0:
                return True
        return False


admin.site.register(Data_template,PageAdmin)
admin.site.register(Visualization_template,PageAdmin)

admin.site.register(AboutUs)
admin.site.register(Data)
admin.site.register(Visualization)