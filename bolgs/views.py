from django.shortcuts import render
from .form import SignUpForm, ContactForm
from django.conf import settings
from .models import SignUP
from django.core.mail import send_mail


# Create your views here.

def home(request):
    # title = "Welcome you are new user"
    # if request.user.is_authenticated:
    #    title ="Welcome %s" %(request.user)
    print("=========================================")
    form = SignUpForm(request.POST or None)
    title = "Sign Up now"
    context = {
        "title": title,
        "form": form,
    }

    # if request.method == "POST":
    #     print(request.POST)
    # form = SignUpForm(request.POST or None)

    if form.is_valid():
        print(request.POST['email'])
        instance = form.save(commit=True)
        full_name = form.cleaned_data.get('full_name')
        if not full_name:
            instance.full_name = 'sara'
            # if not instance.full_name:
            #     instance.full_name = 'sara'
            instance.save(commit=False)
        print(instance.email)
        print(instance.timestamp)
        print(instance.full_name)
        context = {
            "title": " Thanks for registration",
        }

    if request.user.is_authenticated and request.user.is_staff:
        queryset = SignUP.objects.all().order_by('-timestamp')
        print(SignUP.objects.all().order_by('-timestamp').count())
        # queryset = SignUP.objects.all().order_by('-timestamp').filter(full_name__icontains="kati")
        # queryset = SignUP.objects.all().order_by('-timestamp').filter(full_name__iexact="kati")
        print(SignUP.objects.all())
        i=1
        for instance in SignUP.objects.all():
            print(i)
            print(instance)
            print(instance.full_name)
            i +=1
        context = {
                "queryset": queryset,
            }

    return render(request, "home.html", context)


def contact(request):
    title = 'Contact Us'
    text_center = True
    emailForm = ContactForm(request.POST or None)
    if emailForm.is_valid():
        print(emailForm.cleaned_data)
        form_email = emailForm.cleaned_data.get('email')
        form_message = emailForm.cleaned_data.get('message')
        form_full_name = emailForm.cleaned_data.get('full_name')

        Subject = "MAil from django"
        from_mail = settings.EMAIL_HOST_USER
        to_mail = [form_email, 'baddikata@gmail.com']
        contact_message = "%s : %s via %s".format(form_full_name, form_message, from_mail)
        # send_mail(Subject,contact_message, from_mail, to_mail, fail_silently=True)
    context = {
        "form": emailForm,
        "title": title,
        "text_center": text_center,

    }
    return render(request, "emailForm.html", context)
