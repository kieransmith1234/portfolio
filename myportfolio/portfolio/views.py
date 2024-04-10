from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'portfolio/index.html'

class TimelineView(TemplateView):
    template_name = 'portfolio/timeline.html'

class CodeView(TemplateView):
    template_name = 'portfolio/code.html'
