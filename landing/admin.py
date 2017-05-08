from django.contrib import admin
from mezzanine.pages.admin import  PageAdmin

from landing.models import SiteInformation,AboutUs,Visualization,Data,Data_template,Visualization_template,Candidate
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


class CandidateAdmin(admin.ModelAdmin):
    list_display = ('Name','Party','Position','picture_inline','symbol_inline','Short_Bio','Age','Education','Experience','Promises','Contributor_Name','Contributor_PhoneNumber','Status',)
    search_fields = ('Name','Party','Position','picture_inline','symbol_inline','Short_Bio','Age','Education','Experience','Promises','Contributor_Name','Contributor_PhoneNumber','Status',)
    list_filter = ('Status',)

admin.site.register(Candidate, CandidateAdmin)

admin.site.register(Data_template,PageAdmin)
admin.site.register(Visualization_template,PageAdmin)

admin.site.register(AboutUs)
admin.site.register(Data)
admin.site.register(Visualization)