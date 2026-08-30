from django.shortcuts import get_object_or_404, render
from . models import Case
from .forms import CaseForm
from django.views.generic import ListView, DetailView

def home(request):
  return render(request, 'detective/home.html')

def case_list(request):
  cases = Case.objects.all()
  return render(request, 'detective/cases.html', {'cases': cases})

def case_detail(request, case_id):
  case = get_object_or_404(Case, id=case_id)

  return render(
      request,
      'detective/case_detail.html',
      {'case': case}
  )

def case_update(request, case_id):
  case = Case.objects.get(id=case_id)

  if request.method == 'POST':
      form = CaseForm(request.POST, instance=case)

      if form.is_valid():
          form.save()
          return render(
              request,
              'detective/case_detail.html',
              {'case': case}
          )

  else:
      form = CaseForm(instance=case)

  return render(
      request,
      'detective/case_form.html',
      {'form': form}
  )

def case_delete(request, case_id):
    case = Case.objects.get(id=case_id)

    if request.method == 'POST':
        case.delete()
        return render(request, 'detective/cases.html', {
            'cases': Case.objects.all()
        })

    return render(
        request,
        'detective/case_delete.html',
        {'case': case}
    )

def case_create(request):

    if request.method == 'POST':
        form = CaseForm(request.POST)

        if form.is_valid():
            form.save()
            return render(
                request,
                'detective/cases.html',
                {'cases': Case.objects.all()}
            )

    else:
        form = CaseForm()

    return render(
        request,
        'detective/case_form.html',
        {'form': form}
    )

class CaseListView(ListView):
  model = Case
  template_name = 'detective/cases.html'
  context_object_name = 'cases'

class CaseDetailView(DetailView):
  model = Case
  template_name = 'detective/case_detail.html'
  context_object_name = 'case'