from django.views.generic import TemplateView


class HomeTemplateView(TemplateView):
    template_name = 'home/homepage.html'


class TeamTemplateView(TemplateView):
    template_name = 'home/team.html'


class LocationTemplateView(TemplateView):
    template_name = 'home/location.html'


class PrivacyTemplateView(TemplateView):
    template_name = 'home/privacy.html'


class ResourceTemplateView(TemplateView):
    template_name = 'home/resource.html'


class CvTemplateView(TemplateView):
    template_name = 'home/cv.html'


class StuffTemplateView(TemplateView):
    template_name = 'home/stuff.html'
