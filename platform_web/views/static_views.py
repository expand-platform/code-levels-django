from django.views.generic import TemplateView

# Static Pages
class HomeView(TemplateView):
    template_name = "website/pages/home.html"

# class AboutView(TemplateView):
#     template_name = "website/pages/about.html"

# class ContactView(TemplateView):
#     template_name = "website/pages/contact.html"

# class ProfileView(TemplateView):
#     template_name = "website/account/profile.html"

# class GoogleSignupView(TemplateView):
#     template_name = "website/account/socialaccount/signup.html"