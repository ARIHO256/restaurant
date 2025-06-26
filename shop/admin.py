from django.contrib import admin
from .models import Product, Contact, Orders, OrderUpdate, About

class OrderUpdateAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'update_desc', 'timestamp')
    list_filter = ['timestamp']

    def has_delete_permission(self, request, obj=None):
        return False

class OrdersAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'userId', 'name', 'email', 'timestamp')
    list_filter = ['timestamp']

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'category', 'price')
    list_filter = ['category']
    search_fields = ['product_name']

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'desc', 'email', 'timestamp')
    list_filter = ['timestamp']

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_module_permission(self, request):
        return False

class AboutAdmin(admin.ModelAdmin):
    # Add any customization for an About model here or leave empty
    pass

admin.site.register(Product, ProductAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Orders, OrdersAdmin)
admin.site.register(OrderUpdate, OrderUpdateAdmin)
admin.site.register(About, AboutAdmin)

admin.site.site_header = "The Achiever Restaurant"
admin.site.index_title = "The Achiever Restaurant Administration"
admin.site.site_title = "The Achiever Restaurant Admin"
