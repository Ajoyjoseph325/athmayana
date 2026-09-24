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


    included = models.TextField(null=True, blank=True)

    not_included = models.TextField(null=True, blank=True)

    eligible = models.TextField(null=True, blank=True)

    tibet_visa = models.TextField(null=True, blank=True)

    payment_terms = models.TextField(null=True, blank=True)

    payment_schedule = models.TextField(null=True, blank=True)

    # Health & Pilgrimage Readiness fields
    who_can_participate = models.TextField(
        null=True, blank=True,
        help_text="One point per line (e.g., 'Participants above 10 years of age')"
    )

    who_should_avoid = models.TextField(
        null=True, blank=True,
        help_text="One point per line (e.g., 'Asthma or chronic respiratory illnesses')"
    )

    medical_fitness = models.TextField(
        null=True, blank=True,
        help_text="One point per line (e.g., 'Undergo a complete medical examination before departure')"
    )

    # Documents Required card
    documents_required = models.TextField(
        null=True, blank=True,
        help_text="One document per line (e.g., 'Aadhaar Card')"
    )

    # Important Travel Advisory (Rich Text)
    travel_advisory = models.TextField(
        null=True, blank=True,
        help_text="Rich text / HTML content for Important Travel Advisory"
    )

    # Useful Travel Tips (Rich Text)
    travel_tips = models.TextField(
        null=True, blank=True,
        help_text="Rich text / HTML content for Useful Travel Tips"
    )

    # Packing Checklist (Rich Text)
    packing_checklist = models.TextField(
        null=True, blank=True,
        help_text="Rich text / HTML content for Packing Checklist"
    )

    # Additional Place Visit (Optional)
    additional_place_heading = models.CharField(
        max_length=255, null=True, blank=True,
        help_text="Heading for additional place visit (e.g. 'Lipulekh Pass Visit')"
    )

    additional_place_content = models.TextField(
        null=True, blank=True,
        help_text="Content details and conditions for additional place visit"
    )

    additional_permission_details = models.TextField(
        null=True, blank=True,
        help_text="Additional permission / cancellation disclaimer details"
    )

    # Packing Caution / Note
    packing_note = models.TextField(
        null=True, blank=True,
        help_text="Important note / caution at bottom of Packing Checklist"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.package.name

    def _to_list(self, field_value):
        """Helper to split a newline-delimited or HTML text field into a clean list."""
        if not field_value:
            return []
        import html, re
        text = str(field_value)
        if '<' in text and '>' in text:
            text = re.sub(r'<\s*/?\s*(?:br|p|li|div|tr|h\d)[^>]*>', '\n', text, flags=re.IGNORECASE)
            text = re.sub(r'<[^>]+>', '', text)
        text = html.unescape(text).replace('\xa0', ' ').replace('&nbsp;', ' ')
        lines = []
        for line in text.splitlines():
            cleaned = re.sub(r'\s+', ' ', line).strip()
            if cleaned:
                lines.append(cleaned)
        return lines

    def get_included_list(self):
        return self._to_list(self.included)

    def get_not_included_list(self):
        return self._to_list(self.not_included)

    def get_who_can_participate_list(self):
        return self._to_list(self.who_can_participate)

    def get_who_should_avoid_list(self):
        return self._to_list(self.who_should_avoid)

    def get_medical_fitness_list(self):
        return self._to_list(self.medical_fitness)

    def get_documents_required_list(self):
        return self._to_list(self.documents_required)

    def get_travel_tips_list(self):
        return self._to_list(self.travel_tips)

    def get_travel_advisory_list(self):
        return self._to_list(self.travel_advisory)

    def get_travel_advisory_groups(self):
        """Parse travel_advisory into list of {'heading': '...', 'items': [...]}."""
        if not self.travel_advisory:
            return []
        import html, re
        text = str(self.travel_advisory)
        if '<' in text and '>' in text:
            text = re.sub(r'<\s*/?\s*(?:br|p|li|div|tr|h\d)[^>]*>', '\n', text, flags=re.IGNORECASE)
            text = re.sub(r'<[^>]+>', '', text)
        text = html.unescape(text).replace('\xa0', ' ').replace('&nbsp;', ' ')
        groups = []
        current_heading = None
        current_items = []
        for line in text.splitlines():
            stripped = re.sub(r'\s+', ' ', line).strip()
            if not stripped:
                if current_heading and current_items:
                    groups.append({'heading': current_heading, 'items': current_items})
                    current_heading = None
                    current_items = []
                continue
            if stripped.isupper() or (stripped == stripped.upper() and len(stripped) > 2):
                if current_heading and current_items:
                    groups.append({'heading': current_heading, 'items': current_items})
                current_heading = stripped
                current_items = []
            else:
                if not current_heading:
                    current_heading = stripped
                else:
                    current_items.append(stripped)
        if current_heading and current_items:
            groups.append({'heading': current_heading, 'items': current_items})
        return groups

    






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

    day = models.PositiveIntegerField(
        help_text="Day number of the itinerary (e.g., 1 for Day 1, 2 for Day 2)"
    )

    eyebrow = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text="Tagline above title (e.g., 'ANCIENT STONE TEMPLES & SACRED PEAKS')"
    )

    heading = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text="Main route title (e.g., 'Jageshwar → Kasar Devi → Katarmal → Pithoragarh')"
    )

    location_pin = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text="Location tag on image (e.g., 'Jageshwar Dham • 124 Stone Temples')"
    )

    images = models.ImageField(
        upload_to='itineraries_two/',
        null=True,
        blank=True
    )

    itinerary = models.TextField(
        null=True,
        blank=True,
        help_text="Detailed day description"
    )

    distance = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        help_text="e.g., '~140 Kms'"
    )

    driving_time = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        help_text="e.g., '6 - 7 Hours'"
    )

    altitude = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text="e.g., 'Kasar Devi: 2,116 M • Katarmal: 2,114 M • Pithoragarh: 1,627 M'"
    )

    day_highlights = models.TextField(
        null=True,
        blank=True,
        help_text="Enter each highlight on a new line"
    )

    distance_duration = models.CharField(max_length=255, null=True, blank=True)

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
        return f"{self.package.name} - Day {self.day}: {self.heading or ''}"

    def get_highlights_list(self):
        """Helper to return day_highlights as a clean list for templates"""
        if not self.day_highlights:
            return []
        import html, re
        text = str(self.day_highlights)
        if '<' in text and '>' in text:
            text = re.sub(r'<\s*/?\s*(?:br|p|li|div|tr|h\d)[^>]*>', '\n', text, flags=re.IGNORECASE)
            text = re.sub(r'<[^>]+>', '', text)
        text = html.unescape(text).replace('\xa0', ' ').replace('&nbsp;', ' ')
        lines = []
        for line in text.splitlines():
            cleaned = re.sub(r'\s+', ' ', line).strip()
            if cleaned:
                lines.append(cleaned)
        return lines