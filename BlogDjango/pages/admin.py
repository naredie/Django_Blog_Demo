from django.contrib import admin
from .models import Page

#configuracion exta para el panel de administracion
class PageAdmin(admin.ModelAdmin):
    readonly_fields=('created_at','updated_at')
    search_fields=('title','content')
    list_filter=('visible',)
    list_display=('title','visible','created_at')
    ordering=('-created_at',)

# Register your models here.
admin.site.register(Page,PageAdmin)

panelTitle = "Blog con Django"
panelSubtitle = "Panel de gestión"

admin.site.site_header = panelTitle
admin.site.site_title = panelTitle
admin.site.index_title = panelSubtitle