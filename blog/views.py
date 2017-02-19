from django.views.generic import TemplateView
from blog.models import Post

class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        posts = []
        for p in Post.objects.all()[:5]:
            post = dict()
            post['title'] = p.title
            post['preview'] = p.body[:100] + '[...]'
            post['created'] = p.created
            posts.append(post)

        context['posts'] = posts
        return context

class PostView(TemplateView):
    template_name = 'post.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        
