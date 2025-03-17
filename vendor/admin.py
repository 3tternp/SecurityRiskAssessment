from django.contrib import admin
from .models import Vendor, UserVendor, UserTypeVendor

# Customize the Vendor admin view
class VendorAdmin(admin.ModelAdmin):
    list_display = ('name', 'website', 'exstContract', 'slug')  # Displayed columns in the list view
    search_fields = ('name', 'website', 'address')  # Searchable fields
    list_filter = ('exstContract',)  # Filter options in the sidebar

class UserVendorAdmin(admin.ModelAdmin):
    list_display = ('user', 'vendor', 'userType', 'phone')  # Displayed columns in the list view
    search_fields = ('user__fname', 'user__lname', 'phone')  # Searchable fields, including user's first/last name
    list_filter = ('userType',)  # Filter options in the sidebar
    raw_id_fields = ('user',)  # Improves performance when selecting a user (especially with large databases)

class UserTypeVendorAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Displayed columns in the list view
    search_fields = ('name',)  # Searchable fields

# Register the models with their respective custom admin views
admin.site.register(Vendor, VendorAdmin)
admin.site.register(UserVendor, UserVendorAdmin)
admin.site.register(UserTypeVendor, UserTypeVendorAdmin)
