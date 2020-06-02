from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from django.urls import reverse_lazy
from .models import Post


class LatestPostsFeed(Feed):
    # The title, link, and description attributes correspond to the <title>, <link>,
    # and <description> RSS elements, respectively.
    title = 'My blog'
    link = reverse_lazy('blog:post_list')  # Allows to use a URL reversal before the project's URL configuration
    # is loaded.
    description = 'New posts of my blog.'

    @staticmethod
    def items():
        return Post.published.all()[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.body, 30)
