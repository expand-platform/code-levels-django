from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "website/dashboard/dashboard.html"

class LevelView(LoginRequiredMixin, TemplateView):
    template_name = "website/dashboard/level.html"