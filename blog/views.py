from django.views.generic import TemplateView
from blog.models import Post

class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.all()[:5]
        print(context)
        return context
