from django.shortcuts import render
from rest_framework import viewsets
from concept.models import Concept
from concept.serializers import ConceptSerializer
from django.views.generic import ListView, DetailView

def concepts_gallery(request):
    context = {}
    return render(request, 'concepts/index.html', context)

class ConceptViewSet(viewsets.ModelViewSet):
    queryset = Concept.objects.all()
    serializer_class = ConceptSerializer
    paginate_by = 10
    paginate_by_param = 'page_size'


class ConceptListView(ListView):
	model = Concept
	queryset = Concept.objects.all()
	context_object_name = "concepts"
	template_name = 'concept/list.html'


class ConceptDetailView(DetailView):

    model = Concept
    template_name = 'concept/contact.html'

    def get_context_data(self, **kwargs):
        context = super(ContactDetailView, self).get_context_data(**kwargs)
        return context	
