from django.views.generic import TemplateView

# Static Pages
class DashboardView(TemplateView):
    template_name = "website/pages/dashboard.html"