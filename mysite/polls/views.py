# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic

from polls.models import Poll, Choice

# def index(request):
#     latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
#     context = {'latest_poll_list':latest_poll_list}
#     return render(request, 'polls/index.html', context)
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_poll_list'
    
    def get_queryset(self):
        return Poll.objects.order_by('-pub_date')[:5]

# def detail(request,poll_id):
#     poll = get_object_or_404(Poll, pk=poll_id)
#     return render(request, 'polls/details.html', {'poll':poll})

class DetailView(generic.DetailView):
    model = Poll
    template_name = 'polls/details.html'
    

# def result(request,poll_id):
#     poll = get_object_or_404(Poll,pk=poll_id)
#     return render(request, 'polls/results.html', {'poll':poll})

class ResultView(generic.DetailView):
    model = Poll
    template_name = 'polls/results.html'
    
    


def vote(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = poll.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'polls/details.html',{'poll':poll,'error_message':'You did not select a choice !'})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(poll.id,)))
        
        
        
    

