from django.shortcuts import render,redirect
from django.contrib import messages
from .models import contact
from django.core.mail import EmailMessage
from django.conf import settings
# Create your views here.
def index(request):
    return render(request, "index.html")
def about(request):
    return render(request, "about_us.html")
def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        comment = request.POST.get('comment')
        c = contact(name=name, email=email, phone=phone, comment=comment)
        c.save()
  # Send email
        subject = "New Contact Form Submission"
        message = f"""
        You have received a new contact form submission:
        
        Name: {name}
        Email: {email}
        Phone: {phone}
        Comment: {comment}
        """
        recipient_email = "jainharshit2546@gmail.com"  # Replace with the recipient's email address
        sender_email = settings.EMAIL_HOST_USER  # Replace with your email address
        
        try:
            email_message = EmailMessage(subject, message, sender_email, [recipient_email])
            email_message.send()
            messages.success(request, "Your message has been sent successfully.")
            return redirect('contact_us')  # Redirect to the contact page or any other page
        except Exception as e:
            messages.error(request, f"Failed to send email: {str(e)}")
            print(f"Email sending failed: {str(e)}")  # Debugging log
            return redirect('contact_us')  # Redirect to the contact page or any other page
    return render(request, 'contact.html', {'success': True})
def product(request):
    return render(request, "product.html")
def parabolic(request):
    return render(request, "parabolic.html")
def conventional_leaf_spring(request):
    return render(request, "conventional_leaf_spring.html")
def trialer_leaf_spring(request):
    return render(request, "trialer_leaf_spring.html")
def erickshaw_leaf_spring(request):
    return render(request, "erickshaw_leaf_spring.html")
def truck_leaf_spring(request):
    return render(request, "truck_leaf_spring.html")