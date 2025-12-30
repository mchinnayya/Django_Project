from django.shortcuts import render, redirect
from .forms import EnquiryForm

def home(request):
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # or success page
    else:
        form = EnquiryForm()
    return render(request, 'core/home.html', {'enquiry_form': form, 'show_happy_clients': True})

def jobs(request):
    return render(request, 'core/jobs.html', {'show_happy_clients': False})
