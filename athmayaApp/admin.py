
from django.contrib import admin
from .models import Category,Package,PackageItinerary,PackageDetail,TourHighlight,PackageDetailsTwo,PackageItineraryTwo

admin.site.register(Category)
admin.site.register(Package)
admin.site.register(PackageItineraryTwo)
admin.site.register(PackageDetail)
admin.site.register(TourHighlight)
admin.site.register(PackageDetailsTwo)

# Register your models here.
