from django.views.generic import ListView
from pure_pagination.mixins import PaginationMixin
from . import models

class PrevNextPaginatorView(ListView):
    model = models.Article
    template_name = 'myapp/prev_next.html'
    paginate_by = 1
    
class PrevNextPaginatorByDescView(ListView):
    model = models.Article
    template_name = 'myapp/prev_next_desc.html'
    paginate_by = 1
    ordering = '-pk'
    
class AllPaginatorView(ListView):
    model = models.Article
    template_name = 'myapp/all.html'
    paginate_by = 1
    
    
class PurePaginatorView(PaginationMixin, ListView):
    model = models.Article
    template_name = 'myapp/pure.html'
    paginate_by = 1