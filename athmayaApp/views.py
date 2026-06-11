from django.shortcuts import render
from .models import Category,PackageItinerary,PackageDetail,TourHighlight,PackageDetailsTwo,PackageItineraryTwo,PackageDetailsTwo, PackageItineraryTwo, TourHighlight
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Category,Package
from django.core.paginator import Paginator
from django.urls import reverse
from django.db import IntegrityError


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



def spiritual_packages(request, category_id):

    category = Category.objects.get(id=category_id)

    packages = Package.objects.filter(
        category_id=category_id,
        status='Active'
    )

    context = {
        'packages': packages,
        'category': category 
    }

    return render(request, 'spiritual_packages.html', context)


def books(request):
    return render(request, 'books.html')



def wellness_packages(request):
    pass



def publications(request):
    pass

def contact(request):



    pass




def view_packages(request):
    package_list = Package.objects.all().order_by('-id')
    paginator = Paginator(package_list, 4)
    page = request.GET.get('page')
    packages = paginator.get_page(page)

    categories = Category.objects.filter(status='Active')

    return render(request, 'useradmin/add_packages.html', {
        'packages': packages,
        'categories': categories,
    })




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

    packages = Package.objects.all().order_by('-id')

    context = {
        'categories': categories,
        'packages': packages
    }

    return render(request, 'useradmin/add_packages.html', context)



def edit_package(request, id):

    package = get_object_or_404(Package, id=id)

    categories = Category.objects.filter(status='Active')

    packages = Package.objects.all().order_by('-id')

    page_number = request.GET.get('page', 1)

    package_list = Package.objects.all().order_by('-id')
    paginator = Paginator(package_list, 4)
    packages = paginator.get_page(page_number)

    context = {
            'package': package,
            'categories': categories,
            'packages': packages
    }

    return render(request, 'useradmin/add_packages.html', context)




def update_package(request, id):

    package = get_object_or_404(Package, id=id)

    if request.method == "POST":

        package.name = request.POST.get('name')

        category_id = request.POST.get('category')

        package.category = Category.objects.get(id=category_id)

        package.duration = request.POST.get('duration')

        package.amount = request.POST.get('amount')

        package.status = request.POST.get('status')
        image = request.FILES.get('image')

        # Update image only if new image uploaded
        if image:
            package.image = image

        package.save()

        return redirect('add_packages')

    return redirect('edit_package', id=id)



def delete_package(request, id):

    package = get_object_or_404(Package, id=id)

    package.delete()

    return redirect('add_packages')







def add_category(request):

    edit_category = None

    edit_id = request.GET.get('edit')

    if edit_id:
        edit_category = get_object_or_404(Category, id=edit_id)

    if request.method == 'POST':

        categoryname = request.POST.get('categoryname', '').strip()

        short_description = request.POST.get(
            'short_description',
            ''
        ).strip()

        status = request.POST.get('status', '').strip()

        image = request.FILES.get('image')

        edit_id = request.POST.get('edit_id')

        # Validation
        if not categoryname:

            messages.error(
                request,
                'Category name is required.'
            )

        elif not status:

            messages.error(
                request,
                'Please select a status.'
            )

        else:

            if edit_id:

                # UPDATE
                category = get_object_or_404(
                    Category,
                    id=edit_id
                )

                category.categoryname = categoryname

                category.short_description = short_description

                category.status = status

                # Update image only if uploaded
                if image:
                    category.image = image

                category.save()

                messages.success(
                    request,
                    'Category updated successfully!'
                )

            else:

                # CREATE
                Category.objects.create(
                    categoryname=categoryname,
                    short_description=short_description,
                    image=image,
                    status=status
                )

                messages.success(
                    request,
                    'Category added successfully!'
                )

            # return redirect('add_category')
            page_number = request.POST.get('page_number', 1)
            if edit_id:
                return redirect(f"{reverse('add_category')}?edit={edit_id}&page={page_number}")
            else:
                return redirect(f"{reverse('add_category')}?page={page_number}")

    categories = Category.objects.all().order_by('-created_at')

    paginator = Paginator(categories, 4)

    page = request.GET.get('page')

    categories = paginator.get_page(page)

    return render(request, 'useradmin/add_category.html', {
        'categories': categories,
        'edit_category': edit_category,
    })




 
 
def delete_category(request, pk):
    category = get_object_or_404(Category, id=pk)
    category.delete()
    messages.success(request, 'Category deleted successfully!')
    return redirect('add_category')





# # package detail page
def kailash_detail(request, id):
    package = Package.objects.get(id=id)
    
    try:
        details = package.details_two
    except:
        details = None

    itineraries = PackageItineraryTwo.objects.filter(
        package=package, 
        status='active'
    ).order_by('id')

    highlights = TourHighlight.objects.none()
    if details:
        highlights = details.tour_highlights.filter(status='Active')

    context = {
        'package': package,
        'details': details,
        'itineraries': itineraries,
        'highlights': highlights,
    }
   
    return render(request, 'kailash_detail_new.html')




def kailash_detail(request, id):
    package = Package.objects.get(id=id)
    
    try:
        details = package.details_two
    except:
        details = None

    itineraries = PackageItineraryTwo.objects.filter(
        package=package, 
        status='active'
    ).order_by('id')

    highlights = TourHighlight.objects.none()
    if details:
        highlights = details.tour_highlights.filter(status='Active')

    context = {
        'package': package,
        'details': details,
        'itineraries': itineraries,
        'highlights': highlights,
    }
   
    return render(request, 'kailash_detail_new.html', context)




# new add pacakagedetail function with error handling 

def add_package_details(request, edit_id=None):
    packages = Package.objects.all()
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
            'map_name': request.POST.get('map_name'),
            'map_details': request.POST.get('map_details'),
            'included': request.POST.get('included'),
            'not_included': request.POST.get('not_included'),
            'eligible': request.POST.get('eligible'),
            'tibet_visa': request.POST.get('tibet_visa'),
            'payment_terms': request.POST.get('payment_terms'),
            'regular_clothing': request.POST.get('regular_clothing'),
            'trekking_gear': request.POST.get('trekking_gear'),
            'bath_kit': request.POST.get('bath_kit'),
            'health_essentials': request.POST.get('health_essentials'),
            'travel_utility': request.POST.get('travel_utility'),
            'documents_money': request.POST.get('documents_money'),
        }

        main_image = request.FILES.get('main_image')
        map_image = request.FILES.get('map_image')

        if edit_id:
            for key, value in data.items():
                setattr(edit_detail, key, value)
            if main_image:
                edit_detail.main_image = main_image
            if map_image:
                edit_detail.map_image = map_image
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
                    if map_image:
                        detail.map_image = map_image
                    detail.save()
                    detail.tour_highlights.set(highlight_ids)
                    return redirect(f"{reverse('add_package_details')}?page={page_number}")
                except IntegrityError:
                    error_message = f'Package details already exist for "{package.name}". Please edit the existing record instead.'

    # Pagination
    detail_list = PackageDetailsTwo.objects.all().order_by('-id')
    paginator = Paginator(detail_list, 1)
    package_details = paginator.get_page(page_number)

    return render(request, "useradmin/add_package_details.html", {
        'packages': packages,
        'highlights': highlights,
        'edit_detail': edit_detail,
        'package_details': package_details,
        'error_message': error_message,
    })



def delete_package_detail(request, id):
    detail = PackageDetailsTwo.objects.get(id=id)
    detail.delete()
    return redirect('add_package_details')



def package_highlights(request):
    packages = Package.objects.all()
    highlights = TourHighlight.objects.all()
    return render(request, "useradmin/add_tour_highlights_new.html",{
        'packages': packages,
        'highlights': highlights,
    })




def add_package_highlights(request, edit_id=None):
    packages = Package.objects.all()
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





def add_package_itinerary(request, edit_id=None):
    packages = Package.objects.all()
    edit_itinerary = None
    page_number = request.POST.get('page_number') or request.GET.get('page', 1)

    if edit_id:
        edit_itinerary = get_object_or_404(PackageItineraryTwo, id=edit_id)

    if request.method == 'POST':
        package_id = request.POST.get('package')
        package = get_object_or_404(Package, id=package_id)
        itinerary = request.POST.get('itinerary')
        status = request.POST.get('status')
        images = request.FILES.get('images')

        if edit_id:
            edit_itinerary.package = package
            edit_itinerary.itinerary = itinerary
            edit_itinerary.status = status
            if images:
                edit_itinerary.images = images
            edit_itinerary.save()
        else:
            PackageItineraryTwo.objects.create(
                package=package,
                itinerary=itinerary,
                status=status,
                images=images,
            )

        return redirect(f"{reverse('add_package_itinerary')}?page={page_number}")

    itinerary_list = PackageItineraryTwo.objects.select_related('package').order_by('-id')
    paginator = Paginator(itinerary_list, 1)  # changed from 1 to 5
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