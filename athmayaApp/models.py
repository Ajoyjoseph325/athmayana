from django.db import models



class Category(models.Model):

    STATUS_CHOICES = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    )

    short_description = models.TextField(
        null=True,
        blank=True
    )

    image = models.ImageField(
        upload_to='categories/',
        null=True,
        blank=True
    )

    categoryname = models.CharField(max_length=200)

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='Active'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.categoryname

# Create your models here.


class Package(models.Model):

    STATUS_CHOICES = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    )

    name = models.CharField(max_length=255)

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='packages'
    )

    duration = models.CharField(max_length=100)

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='Active'
    )


    image = models.ImageField(
        upload_to='packages/',
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


#jdn

class PackageItinerary(models.Model):

    package = models.ForeignKey(
        Package,
        on_delete=models.CASCADE,
        related_name='itineraries'
    )

   



    heading = models.CharField(
        max_length=255
    )

    description = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.heading




class PackageDetail(models.Model):
    package = models.OneToOneField(
        Package,
        on_delete=models.CASCADE,
        related_name='detail'
    )
    maindescription = models.TextField(null=True, blank=True)
    main_image = models.ImageField(upload_to='packages/main/', null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.package.name





class TourHighlight(models.Model):

    STATUS_CHOICES = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    )



    name = models.CharField(max_length=255)

    icon = models.ImageField(
        upload_to='highlights/',
        null=True,
        blank=True
    )

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='Active'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    



class PackageDetailsTwo(models.Model):

    STATUS_CHOICES = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    )

   

    package = models.OneToOneField(
        Package,
        on_delete=models.CASCADE,
        related_name='details_two'
    )

    tour_highlights = models.ManyToManyField(
        TourHighlight,
        blank=True
    )

    about_package = models.TextField(null=True, blank=True)

    main_image = models.ImageField(
        upload_to='package_details/',
        null=True,
        blank=True
    )

    map_name = models.CharField(max_length=255, null=True, blank=True)

    map_details = models.TextField(null=True, blank=True)

    map_image = models.ImageField(
        upload_to='package_maps/',
        null=True,
        blank=True
    )

    included = models.TextField(null=True, blank=True)

    not_included = models.TextField(null=True, blank=True)

    eligible = models.TextField(null=True, blank=True)

    tibet_visa = models.TextField(null=True, blank=True)

    payment_terms = models.TextField(null=True, blank=True)

    regular_clothing = models.TextField(null=True, blank=True)

    trekking_gear = models.TextField(null=True, blank=True)

    bath_kit = models.TextField(null=True, blank=True)

    health_essentials = models.TextField(null=True, blank=True)

    travel_utility = models.TextField(null=True, blank=True)

    documents_money = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.package.name
    






class PackageItineraryTwo(models.Model):

    STATUS_CHOICES = (
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    )

    package = models.ForeignKey(
        Package,
        on_delete=models.CASCADE,
        related_name='itineraries_two'
    )

    heading = models.CharField(max_length=255, null=True, blank=True)

    day = models.PositiveIntegerField(
        help_text="Day number of the itinerary (e.g., 1 for Day 1, 2 for Day 2)"
    )

    images = models.ImageField(
        upload_to='itineraries_two/',
        null=True,
        blank=True
    )

    itinerary = models.TextField(null=True, blank=True)

    distance_duration = models.CharField(max_length=255, null=True, blank=True)

    altitude = models.CharField(max_length=255, null=True, blank=True)

    accommodation = models.CharField(max_length=255, null=True, blank=True)

    meals = models.CharField(max_length=255, null=True, blank=True)

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='active'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.package.name