from django.db.models import Q
from django.views.generic import ListView

from concept.models import Concept


class SearchView(ListView):
    model = Concept
    context_object_name = 'concepts'
    paginate_by = 10
    template_name = 'search/index.html'

    def get_queryset(self):
        queryset = super(SearchView, self).get_queryset()

        q = self.request.GET.get('q')
        if q:
            return queryset.filter(
                Q(description__icontains=q) | Q(title__icontains=q) |
                

        return queryset
