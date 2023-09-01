from django.shortcuts import render, get_object_or_404
from .models import *
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
from blog.forms import MessageForm
from blog.models import *


def home(request):
    logo = Logo.objects.all()
    about = About.objects.all()
    service = Service.objects.all()
    fact = Facts.objects.all()
    portfolio = Portfolio.objects.all()
    articles = Article.objects.all()[:3]
    tags = HomePageTags.objects.all()
    form = MessageForm()
    if request.method == 'POST':
        form = MessageForm(data=request.POST)

        if form.is_valid():
            # Extract the email field value from the form
            email = form.cleaned_data['Email']

            # Create an EmailValidator instance
            email_validator = EmailValidator()

            try:
                # Validate the email using the EmailValidator
                email_validator(email)

                form.save()

            except ValidationError:
                # If validation fails, handle the error (e.g., show an error message)
                # You can customize this part to handle the validation error as you prefer
                # For example, you could add an error message to the form
                form.add_error('Email', 'Invalid email address!')
        else:
            # Form is not valid, you can handle this as needed
            # For example, you could display an error message to the user
            form.add_error('Name', 'Invalid form!')
    context = {
        'logo': logo,
        'about': about,
        'service': service,
        'fact': fact,
        'portfolio': portfolio,
        'form': form,
        'articles': articles,
        'tags': tags,
    }
    return render(request, 'home_app/Home.html', context)
