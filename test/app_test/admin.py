from django.contrib import admin
from .models import Test

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price', 'action', 'created_date', 'updated_date']
    list_filter = ['action', 'created_at']
    actions = ['make_auction_ass_false', 'make_auction_ass_true']
    @admin.action(description='торг не уместен')
    def make_auction_ass_false(self, request, queryset):
        queryset.update(action=False)
    @admin.action(description='торг уместен')
    def make_auction_ass_true(self, request, queryset):
        queryset.update(action=True)
    fieldsets = (('Общее', {'fields': ('title', 'description')}),('Финансы', {'fields': ('price', 'action'), 'classes': ['collapse']}))

admin.site.register(Test, AdvertisementAdmin)


