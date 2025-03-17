from django.test import TestCase
from django.urls import reverse

class VendorViewsTestCase(TestCase):
    
    def test_create_vendor_view(self):
        """Test the create_vendor view."""
        response = self.client.get(reverse('create_vendor'))  # Use 'reverse' to get the URL for the view
        self.assertEqual(response.status_code, 200)  # Ensure the response status is 200 (OK)
        self.assertTemplateUsed(response, 'vendor/createVendor.html')  # Check that the correct template is used

    def test_vendor_role_error_view(self):
        """Test the vendor_role_error view."""
        response = self.client.get(reverse('vendor_role_error'))  # Similarly, reverse to get the URL
        self.assertEqual(response.status_code, 200)  # Ensure the response status is 200 (OK)
        self.assertTemplateUsed(response, 'vendor/VendorRoleError.html')  # Check correct template is used
        self.assertContains(response, 'val')  # Verify that 'val' is in the context (which should render in the template)
