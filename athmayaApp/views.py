from django.shortcuts import render
from .models import Category,PackageItinerary,PackageDetail,TourHighlight,PackageDetailsTwo,PackageItineraryTwo,PackageDetailsTwo, PackageItineraryTwo, TourHighlight
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Category,Package
from django.core.paginator import Paginator
from django.urls import reverse
from django.db import IntegrityError

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.contrib.auth import logout

# dhjhdhj



# Create your views here.
def home(request):
    categories = Category.objects.filter(
        status='Active'
    ).order_by('-id')

    context = {
        'categories': categories
    }

    return render(request, 'index.html', context)
    # return render(request, 'index.html')


def contact(request):
  
    return render(request, 'contact.html')




def spiritual_packages(request, category_id):

    category = Category.objects.get(id=category_id)

    packages = Package.objects.filter(
        category_id=category_id,
        status='Active'
    )

    # packages = Package.objects.select_related('category').filter(
    # category_id=category_id, status='Active'
    # )

    context = {
        'packages': packages,
        'category': category 
    }

    return render(request, 'spiritual_packages.html', context)


def books(request):
    return render(request, 'books.html')



def wellness_packages(request):
    pass

def about(request):
    return render(request, 'about.html')





def publications(request):
    pass

# def contact(request):



#     pass













@login_required(login_url='backoffice')
def add_packages(request):

    if request.method == "POST":
        name = request.POST.get('name')
        category_id = request.POST.get('category')
        duration = request.POST.get('duration')
        amount = request.POST.get('amount')
        status = request.POST.get('status')
        image = request.FILES.get('image')

        category = Category.objects.get(id=category_id)

        Package.objects.create(
            name=name,
            category=category,
            duration=duration,
            amount=amount,
            status=status,
            image=image,
        )

        return redirect('add_packages')

    categories = Category.objects.filter(status='Active')
    package_list = Package.objects.select_related('category').order_by('-id')

    # ✅ Added pagination here
    paginator = Paginator(package_list, 4)
    page = request.GET.get('page')
    packages = paginator.get_page(page)

    context = {
        'categories': categories,
        'packages': packages      # now a Page object, not a QuerySet
    }

    return render(request, 'useradmin/add_packages.html', context)


@login_required(login_url='backoffice')
def edit_package(request, id):

    package = get_object_or_404(Package, id=id)
    categories = Category.objects.filter(status='Active')

    package_list = Package.objects.select_related('category').order_by('-id')

    # ✅ Reads ?page= from URL (passed via edit link)
    page_number = request.GET.get('page', 1)
    paginator = Paginator(package_list, 4)
    packages = paginator.get_page(page_number)

    context = {
        'package': package,
        'categories': categories,
        'packages': packages
    }

    return render(request, 'useradmin/add_packages.html', context)





@login_required(login_url='backoffice')
def edit_package(request, id):

    package = get_object_or_404(Package, id=id)

    categories = Category.objects.filter(status='Active')

    # packages = Package.objects.all().order_by('-id')

    page_number = request.GET.get('page', 1)

    # package_list = Package.objects.all().order_by('-id')
    package_list = Package.objects.select_related('category').order_by('-id')

    paginator = Paginator(package_list, 4)
    packages = paginator.get_page(page_number)

    context = {
            'package': package,
            'categories': categories,
            'packages': packages
    }

    return render(request, 'useradmin/add_packages.html', context)



# @login_required(login_url='backoffice')
# def update_package(request, id):

#     package = get_object_or_404(Package, id=id)

#     if request.method == "POST":

#         package.name = request.POST.get('name')

#         category_id = request.POST.get('category')

#         package.category = Category.objects.get(id=category_id)

#         package.duration = request.POST.get('duration')

#         package.amount = request.POST.get('amount')

#         package.status = request.POST.get('status')
#         image = request.FILES.get('image')

#         # Update image only if new image uploaded
#         if image:
#             package.image = image

#         package.save()

#         return redirect('add_packages')

#     return redirect('edit_package', id=id)


def update_package(request, id):
    package = get_object_or_404(Package, id=id)

    if request.method == "POST":
        name = request.POST.get('name')
        category_id = request.POST.get('category')
        duration = request.POST.get('duration')
        amount = request.POST.get('amount')
        status = request.POST.get('status')
        image = request.FILES.get('image')

        page_number = request.POST.get('page_number', 1)  # ✅ read page from form

        package.name = name
        package.category = Category.objects.get(id=category_id)
        package.duration = duration
        package.amount = amount
        package.status = status

        if image:
            package.image = image

        package.save()

        return redirect(f"/add-packages/?page={page_number}")  # ✅ back to same pagedef update_package(request, id):
    package = get_object_or_404(Package, id=id)

    if request.method == "POST":
        name = request.POST.get('name')
        category_id = request.POST.get('category')
        duration = request.POST.get('duration')
        amount = request.POST.get('amount')
        status = request.POST.get('status')
        image = request.FILES.get('image')

        page_number = request.POST.get('page_number', 1)  # ✅ read page from form

        package.name = name
        package.category = Category.objects.get(id=category_id)
        package.duration = duration
        package.amount = amount
        package.status = status

        if image:
            package.image = image

        package.save()

        return redirect(f"/add-packages/?page={page_number}")  # ✅ back to same page


@login_required(login_url='backoffice')
def delete_package(request, id):

    package = get_object_or_404(Package, id=id)

    package.delete()

    return redirect('add_packages')






# @login_required(login_url='backoffice')
# def add_category(request):

#     edit_category = None

#     edit_id = request.GET.get('edit')

#     if edit_id:
#         edit_category = get_object_or_404(Category, id=edit_id)

#     if request.method == 'POST':

#         categoryname = request.POST.get('categoryname', '').strip()

#         short_description = request.POST.get(
#             'short_description',
#             ''
#         ).strip()

#         status = request.POST.get('status', '').strip()

#         image = request.FILES.get('image')

#         edit_id = request.POST.get('edit_id')

#         # Validation
#         if not categoryname:

#             messages.error(
#                 request,
#                 'Category name is required.'
#             )

#         elif not status:

#             messages.error(
#                 request,
#                 'Please select a status.'
#             )

#         else:

#             if edit_id:

#                 # UPDATE
#                 category = get_object_or_404(
#                     Category,
#                     id=edit_id
#                 )

#                 category.categoryname = categoryname

#                 category.short_description = short_description

#                 category.status = status

#                 # Update image only if uploaded
#                 if image:
#                     category.image = image

#                 category.save()

#                 messages.success(
#                     request,
#                     'Category updated successfully!'
#                 )

#             else:

#                 # CREATE
#                 Category.objects.create(
#                     categoryname=categoryname,
#                     short_description=short_description,
#                     image=image,
#                     status=status
#                 )

#                 messages.success(
#                     request,
#                     'Category added successfully!'
#                 )

#             # return redirect('add_category')
#             page_number = request.POST.get('page_number', 1)
#             if edit_id:
#                 return redirect(f"{reverse('add_category')}?edit={edit_id}&page={page_number}")
#             else:
#                 return redirect(f"{reverse('add_category')}?page={page_number}")

#     categories = Category.objects.all().order_by('-created_at')

#     paginator = Paginator(categories, 1)

#     page = request.GET.get('page')

#     categories = paginator.get_page(page)

#     return render(request, 'useradmin/add_category.html', {
#         'categories': categories,
#         'edit_category': edit_category,
#     })




@login_required(login_url='backoffice')
def add_category(request):

    edit_category = None
    edit_id = request.GET.get('edit')

    if edit_id:
        edit_category = get_object_or_404(Category, id=edit_id)

    if request.method == 'POST':

        categoryname = request.POST.get('categoryname', '').strip()
        short_description = request.POST.get('short_description', '').strip()
        status = request.POST.get('status', '').strip()
        image = request.FILES.get('image')
        edit_id = request.POST.get('edit_id')

        # Validation
        if not categoryname:
            messages.error(request, 'Category name is required.')

        elif not status:
            messages.error(request, 'Please select a status.')

        else:

            if edit_id:
                # ✅ Check duplicate on UPDATE — exclude current category
                duplicate = Category.objects.filter(
                    categoryname__iexact=categoryname
                ).exclude(id=edit_id).exists()

                if duplicate:
                    messages.error(request, f'Category "{categoryname}" already exists.')

                else:
                    category = get_object_or_404(Category, id=edit_id)
                    category.categoryname = categoryname
                    category.short_description = short_description
                    category.status = status

                    if image:
                        category.image = image

                    category.save()
                    messages.success(request, 'package updated successfully!')

                    page_number = request.POST.get('page_number', 1)
                    # return redirect(f"{reverse('add_category')}?edit={edit_id}&page={page_number}")
                    return redirect(f"{reverse('add_category')}?page={page_number}")

            else:
                # ✅ Check duplicate on CREATE
                duplicate = Category.objects.filter(
                    categoryname__iexact=categoryname
                ).exists()

                if duplicate:
                    messages.error(request, f'pacakage "{categoryname}" already exists.')

                else:
                    Category.objects.create(
                        categoryname=categoryname,
                        short_description=short_description,
                        image=image,
                        status=status
                    )
                    messages.success(request, 'package added successfully!')

                    page_number = request.POST.get('page_number', 1)
                    return redirect(f"{reverse('add_category')}?page={page_number}")

    categories = Category.objects.all().order_by('-created_at')
    paginator = Paginator(categories, 4)
    page = request.GET.get('page')
    categories = paginator.get_page(page)

    return render(request, 'useradmin/add_category.html', {
        'categories': categories,
        'edit_category': edit_category,
    })



 
@login_required(login_url='backoffice')
def delete_category(request, pk):
    category = get_object_or_404(Category, id=pk)
    category.delete()
    messages.success(request, 'package deleted successfully!')
    return redirect('add_category')




def kailash_detail(request, id=None):
    if id:
        package = get_object_or_404(Package.objects.select_related('category', 'details_two'), id=id)
    else:
        package = Package.objects.select_related('category', 'details_two').first()

    details = None
    itineraries = []
    highlights = []

    if package:
        try:
            details = package.details_two
        except Exception:
            details = None

        itineraries = list(package.itineraries_two.filter(status='active').order_by('day'))
        if details:
            highlights = list(details.tour_highlights.filter(status='Active'))
        else:
            highlights = []

    context = {
        'package': package,
        'details': details,
        'itineraries': itineraries,
        'highlights': highlights,
    }

    return render(request, 'kailash_detail_new3.html', context)




# new add pacakagedetail function with error handling 
@login_required(login_url='backoffice')
def add_package_details(request, edit_id=None):
    # packages = Package.objects.all()
    packages = Package.objects.select_related('category').all()
    highlights = TourHighlight.objects.all()
    edit_detail = None
    error_message = None
    page_number = request.POST.get('page_number') or request.GET.get('page', 1)

    if edit_id:
        edit_detail = get_object_or_404(PackageDetailsTwo, id=edit_id)

    if request.method == 'POST':
        package_id = request.POST.get('package')
        package = get_object_or_404(Package, id=package_id)
        highlight_ids = request.POST.getlist('tour_highlights')

        data = {
            'about_package': request.POST.get('about_package'),
            'included': request.POST.get('included'),
            'not_included': request.POST.get('not_included'),
            'who_can_participate': request.POST.get('who_can_participate'),
            'who_should_avoid': request.POST.get('who_should_avoid'),
            'medical_fitness': request.POST.get('medical_fitness'),
            'documents_required': request.POST.get('documents_required'),
            'travel_advisory': request.POST.get('travel_advisory'),
            'payment_schedule': request.POST.get('payment_schedule'),
            'travel_tips': request.POST.get('travel_tips'),
            'additional_place_heading': request.POST.get('additional_place_heading'),
            'additional_place_content': request.POST.get('additional_place_content'),
            'additional_permission_details': request.POST.get('additional_permission_details'),
            'packing_checklist': request.POST.get('packing_checklist'),
            'packing_note': request.POST.get('packing_note'),
        }

        main_image = request.FILES.get('main_image')

        if edit_id:
            for key, value in data.items():
                setattr(edit_detail, key, value)
            if main_image:
                edit_detail.main_image = main_image
            edit_detail.package = package
            edit_detail.save()
            edit_detail.tour_highlights.set(highlight_ids)
            return redirect(f"{reverse('add_package_details')}?page={page_number}")

        else:
            # Check if details already exist for this package
            if PackageDetailsTwo.objects.filter(package=package).exists():
                error_message = f'Package details already exist for "{package.name}". Please edit the existing record instead.'
            else:
                try:
                    detail = PackageDetailsTwo(package=package, **data)
                    if main_image:
                        detail.main_image = main_image
                    detail.save()
                    detail.tour_highlights.set(highlight_ids)
                    return redirect(f"{reverse('add_package_details')}?page={page_number}")
                except IntegrityError:
                    error_message = f'Package details already exist for "{package.name}". Please edit the existing record instead.'

    # Pagination
    # detail_list = PackageDetailsTwo.objects.all().order_by('-id')
    detail_list = PackageDetailsTwo.objects.select_related('package').prefetch_related(
        'tour_highlights'
        ).order_by('-id')
    paginator = Paginator(detail_list, 4)
    package_details = paginator.get_page(page_number)

    return render(request, "useradmin/add_package_details.html", {
        'packages': packages,
        'highlights': highlights,
        'edit_detail': edit_detail,
        'package_details': package_details,
        'error_message': error_message,
    })


@login_required(login_url='backoffice')

def delete_package_detail(request, id):
    detail = PackageDetailsTwo.objects.get(id=id)
    detail.delete()
    return redirect('add_package_details')


@login_required(login_url='backoffice')
def package_highlights(request):
    packages = Package.objects.all()
    highlights = TourHighlight.objects.all()
    return render(request, "useradmin/add_tour_highlights_new.html",{
        'packages': packages,
        'highlights': highlights,
    })



@login_required(login_url='backoffice')
def add_package_highlights(request, edit_id=None):
    # packages = Package.objects.all()
    packages = Package.objects.select_related('category').all()
    edit_highlight = None
    page_number = request.POST.get('page_number') or request.GET.get('page', 1)

    if edit_id:
        edit_highlight = get_object_or_404(TourHighlight, id=edit_id)

    if request.method == 'POST' and not edit_id:
        name = request.POST.get('name')
        icon = request.FILES.get('icon')
        status = request.POST.get('status')

        TourHighlight.objects.create(
            name=name,
            icon=icon,
            status=status,
        )
        return redirect(f"{reverse('add_package_highlights')}?page={page_number}")

    if request.method == 'POST' and edit_id:
        highlight = get_object_or_404(TourHighlight, id=edit_id)
        highlight.name = request.POST.get('name')
        highlight.status = request.POST.get('status')
        icon = request.FILES.get('icon')
        if icon:
            highlight.icon = icon
        highlight.save()
        return redirect(f"{reverse('add_package_highlights')}?page={page_number}")

    highlight_list = TourHighlight.objects.all().order_by('-id')
    paginator = Paginator(highlight_list, 4)
    highlights = paginator.get_page(page_number)

    return render(request, "useradmin/add_tour_highlights_new.html", {
        'packages': packages,
        'highlights': highlights,
        'edit_highlight': edit_highlight,
    })





def delete_highlight(request, id):
    highlight = TourHighlight.objects.get(id=id)
    highlight.delete()
    return redirect('add_package_highlights')




# @login_required(login_url='backoffice')
# def add_package_itinerary(request, edit_id=None):
#     # packages = Package.objects.all()
#     packages = Package.objects.select_related('category').all()
#     edit_itinerary = None
#     page_number = request.POST.get('page_number') or request.GET.get('page', 1)

#     if edit_id:
#         edit_itinerary = get_object_or_404(PackageItineraryTwo, id=edit_id)

#     if request.method == 'POST':
#         package_id = request.POST.get('package')
#         package = get_object_or_404(Package, id=package_id)
#         itinerary = request.POST.get('itinerary')
#         status = request.POST.get('status')
#         images = request.FILES.get('images')

#         if edit_id:
#             edit_itinerary.package = package
#             edit_itinerary.itinerary = itinerary
#             edit_itinerary.status = status
#             if images:
#                 edit_itinerary.images = images
#             edit_itinerary.save()
#         else:
#             PackageItineraryTwo.objects.create(
#                 package=package,
#                 itinerary=itinerary,
#                 status=status,
#                 images=images,
#             )

#         return redirect(f"{reverse('add_package_itinerary')}?page={page_number}")

#     itinerary_list = PackageItineraryTwo.objects.select_related('package').order_by('-id')
#     paginator = Paginator(itinerary_list, 1)  # changed from 1 to 5
#     itineraries = paginator.get_page(page_number)

#     return render(request, 'useradmin/add_package_itneraries.html', {
#         'packages': packages,
#         'itineraries': itineraries,
#         'edit_itinerary': edit_itinerary,
#     })




# new itneray with day added
# @login_required(login_url='backoffice')
# def add_package_itinerary(request, edit_id=None):
#     packages = Package.objects.select_related('category').all()
#     edit_itinerary = None
#     page_number = request.POST.get('page_number') or request.GET.get('page', 1)

#     if edit_id:
#         edit_itinerary = get_object_or_404(PackageItineraryTwo, id=edit_id)

#     if request.method == 'POST':
#         package_id = request.POST.get('package')
#         package = get_object_or_404(Package, id=package_id)
#         itinerary = request.POST.get('itinerary')
#         status = request.POST.get('status')
#         images = request.FILES.get('images')
#         day = request.POST.get('day')  # ✅ get day from POST data

#         if edit_id:
#             edit_itinerary.package = package
#             edit_itinerary.day = day          # ✅ update day
#             edit_itinerary.itinerary = itinerary
#             edit_itinerary.status = status
#             if images:
#                 edit_itinerary.images = images
#             edit_itinerary.save()
#         else:
#             PackageItineraryTwo.objects.create(
#                 package=package,
#                 day=day,                      # ✅ save day on create
#                 itinerary=itinerary,
#                 status=status,
#                 images=images,
#             )

#         return redirect(f"{reverse('add_package_itinerary')}?page={page_number}")

#     itinerary_list = PackageItineraryTwo.objects.select_related('package').order_by('day')  # ✅ order by day
#     paginator = Paginator(itinerary_list, 1)
#     itineraries = paginator.get_page(page_number)

#     return render(request, 'useradmin/add_package_itneraries.html', {
#         'packages': packages,
#         'itineraries': itineraries,
#         'edit_itinerary': edit_itinerary,
#     })



# new view function with heading added
@login_required(login_url='backoffice')
def add_package_itinerary(request, edit_id=None):
    packages = Package.objects.select_related('category').all()
    edit_itinerary = None
    page_number = request.POST.get('page_number') or request.GET.get('page', 1)

    if edit_id:
        edit_itinerary = get_object_or_404(PackageItineraryTwo, id=edit_id)

    if request.method == 'POST':
        package_id = request.POST.get('package')
        package = get_object_or_404(Package, id=package_id)
        itinerary = request.POST.get('itinerary')
        eyebrow = request.POST.get('eyebrow')
        heading = request.POST.get('heading')
        location_pin = request.POST.get('location_pin')
        distance = request.POST.get('distance')
        driving_time = request.POST.get('driving_time')
        distance_duration = request.POST.get('distance_duration')
        altitude = request.POST.get('altitude')
        highlights_list = request.POST.getlist('day_highlights')
        if highlights_list:
            day_highlights = "\n".join([h.strip() for h in highlights_list if h.strip()])
        else:
            day_highlights = (request.POST.get('day_highlights') or '').strip()
        accommodation = request.POST.get('accommodation')
        meals = request.POST.get('meals')
        status = request.POST.get('status')
        images = request.FILES.get('images')
        day = request.POST.get('day')

        if edit_id:
            edit_itinerary.package = package
            edit_itinerary.day = day
            edit_itinerary.eyebrow = eyebrow
            edit_itinerary.heading = heading
            edit_itinerary.location_pin = location_pin
            edit_itinerary.itinerary = itinerary
            edit_itinerary.distance = distance
            edit_itinerary.driving_time = driving_time
            edit_itinerary.distance_duration = distance_duration
            edit_itinerary.altitude = altitude
            edit_itinerary.day_highlights = day_highlights
            edit_itinerary.accommodation = accommodation
            edit_itinerary.meals = meals
            edit_itinerary.status = status
            if images:
                edit_itinerary.images = images
            try:
                edit_itinerary.save()
            except IntegrityError:
                itinerary_list = PackageItineraryTwo.objects.select_related('package').order_by('day')
                paginator = Paginator(itinerary_list, 1)
                itineraries = paginator.get_page(page_number)
                return render(request, 'useradmin/add_package_itneraries.html', {
                    'packages': packages,
                    'itineraries': itineraries,
                    'edit_itinerary': edit_itinerary,
                    'error': 'Day already exists for this package.'
                })
        else:
            try:
                PackageItineraryTwo.objects.create(
                    package=package,
                    day=day,
                    eyebrow=eyebrow,
                    heading=heading,
                    location_pin=location_pin,
                    itinerary=itinerary,
                    distance=distance,
                    driving_time=driving_time,
                    distance_duration=distance_duration,
                    altitude=altitude,
                    day_highlights=day_highlights,
                    accommodation=accommodation,
                    meals=meals,
                    status=status,
                    images=images,
                )
            except IntegrityError:
                itinerary_list = PackageItineraryTwo.objects.select_related('package').order_by('day')
                paginator = Paginator(itinerary_list, 1)
                itineraries = paginator.get_page(page_number)
                return render(request, 'useradmin/add_package_itneraries.html', {
                    'packages': packages,
                    'itineraries': itineraries,
                    'edit_itinerary': edit_itinerary,
                    'error': 'Day already exists for this package.'
                })

        return redirect(f"{reverse('add_package_itinerary')}?page={page_number}")

    itinerary_list = PackageItineraryTwo.objects.select_related('package').order_by('day')
    paginator = Paginator(itinerary_list, 4)
    itineraries = paginator.get_page(page_number)

    return render(request, 'useradmin/add_package_itneraries.html', {
        'packages': packages,
        'itineraries': itineraries,
        'edit_itinerary': edit_itinerary,
    })






def delete_package_itinerary(request, id):
    itinerary = PackageItineraryTwo.objects.get(id=id)
    itinerary.delete()
    return redirect('add_package_itinerary')




def backoffice(request):
    # if request.user.is_authenticated:
    #     return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_staff:
            login(request, user)
            return redirect('add_category')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, "useradmin/adminlogin.html")


def admin_logout(request):
    logout(request)
    return redirect('backoffice')


def kailash_detail_new3(request, id=None):
    package = None
    details = None
    itineraries = []
    highlights = []

    if id:
        package = get_object_or_404(Package.objects.select_related('category', 'details_two'), id=id)
    else:
        package = Package.objects.select_related('category', 'details_two').first()

    if package:
        try:
            details = package.details_two
        except Exception:
            details = None

        itineraries = list(package.itineraries_two.filter(status='active').order_by('day'))
        if details:
            highlights = list(details.tour_highlights.filter(status='Active'))
        else:
            highlights = []

    return render(request, 'kailash_detail_new3.html', {
        'package': package,
        'details': details,
        'itineraries': itineraries,
        'highlights': highlights,
    })