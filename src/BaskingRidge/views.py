from django.contrib import messages
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import redirect, render


# from TwinBrooks.settings import FRONT_END_CONTACTFORM_EMAIL, FRONTEND_PRO_EMAIL
from BaskingRidgeFiles.models import menu_entry, gallery_image

'''
Static Views that serve as the frontend content.
'''
def home_static(request):
    return render(request,
                  './b_ridge/pages/index.html',
                  {'home_active': True})


def menus_static(request):
    menus = menu_entry.objects.all()
    return render(request,
                  './b_ridge/pages/menus.html',
                  {'history_active': True, 'menus': menus})

def gallery_static(request):
    gallery_items = gallery_image.objects.all()
    return render(request,
                  './b_ridge/pages/gallery.html',
                  {'home_active': True, 'gallery_items': gallery_items})


def vendors_static(request):
    return render(request,
                  './b_ridge/pages/vendors.html',
                  {'home_active': True})

def wedding_promo_static(request):
    return render(request,
                  './b_ridge/pages/wedding_promo.html',
                  {'home_active': True})

def contact_static(request):
    return render(request,
                  './b_ridge/pages/contact.html',
                  {'home_active': True})

def events_static(request):
    form = ContactForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            data = form.cleaned_data
            name = data['name']
            email = data['email']
            phone_number = data['phone_number']
            handicap = data['handicap']
            message = data['body']
            plain_message = (
                'Hello, \n  \n There was a new member inquiry on the site.: \n \n')
            # Include a html template:
            text_content = plain_message + name + '\n Phonenumber: ' + \
                phone_number + '\n Email: ' + email + '\n Handicap: ' + \
                handicap + '\n Message: ' + message + '\n - WVGC Mail Bot'
            msg = EmailMultiAlternatives(
                subject="WCGC Membership Inquiry",
                body=text_content,
                from_email="WVGC Admin <no-reply@watchungvalleygc.com>",
                to=[FRONT_END_CONTACTFORM_EMAIL],

            )
            # Optional Anymail extensions:
            msg.track_clicks = True
            msg.tags = ["Member Inquiry"]
            # Send it:d
            msg.send()
            messages.success(request, 'Request successfully sent.')
            return redirect("thankyou_static")
    return render(request,
                  './front-end/pages/events.html',
                  {'events_active': True, 'form': form})

