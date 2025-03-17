from django.shortcuts import render

# Create your views here.

def create_vendor(request):
    """Render the page for creating a new vendor."""
    return render(request, 'vendor/createVendor.html')

def vendor_role_error(request):
    """Render an error page for vendor role issues."""
    context = {'val': True}
    return render(request, 'vendor/VendorRoleError.html', context)
