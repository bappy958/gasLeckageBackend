# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from django.core.mail import send_mail

# @api_view(["POST"])
# def send_alert(request):
#     message = request.data.get("message", "No Message")
#     send_mail(
#         subject="🚨 Gas Leakage Alert",
#         message=message,
#         from_email="dev.morsalin@gmail.com",
#         recipient_list=["weshallovercome335@gmail.com"],
#         fail_silently=False,
#     )
#     return Response({"status": "Email Sent", "message": message})



# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from django.core.mail import EmailMultiAlternatives
# from django.template.loader import render_to_string
# from django.utils.html import strip_tags
# from django.views.decorators.csrf import csrf_exempt


# @csrf_exempt
# @api_view(["POST"])
# def send_alert(request):
#     message = request.data.get("message", "No Message")
#     subject = "🚨 Gas Leakage Alert"

#     # Render HTML template (we’ll create it soon)
#     html_content = render_to_string("emails/alert.html", {"message": message})
#     text_content = strip_tags(html_content)  # fallback plain text

#     email = EmailMultiAlternatives(
#         subject,
#         text_content,
#         "dev.morsalin@gmail.com",  # sender
#         ["weshallovercome335@gmail.com", "bappyawal0@gmail.com"],  # recipient
#     )
#     email.attach_alternative(html_content, "text/html")
#     email.send()

    

#     return Response({"status": "Email Sent with HTML", "message": message})




from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@api_view(["POST"])
def send_alert(request):
    message = request.data.get("message", "No Message")
    subject = "🚨 Gas Leakage Alert"

    # Render the new HTML template
    html_content = render_to_string("emails/alert.html", {"message": message})
    text_content = strip_tags(html_content)  # fallback plain text

    email = EmailMultiAlternatives(
        subject,
        text_content,
        "dev.morsalin@gmail.com",  # sender
        ["weshallovercome335@gmail.com"],  # recipient
    )
    email.attach_alternative(html_content, "text/html")
    email.send()

    return Response({"status": "Email Sent", "message": message})
