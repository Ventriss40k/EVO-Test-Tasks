from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Name
from .forms import *

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = Your_name(request.POST)
        if form.is_valid():
            name = (request.POST["name"]) # that how to get atribute from request
            if Name.objects.filter(name = name ).exists():
                content = f"Good to see you again, {name}!"

                return render(request,'greet_app/hello.html', {'title':'Hello!','content':content} )
            else:
                
                content = f"Greetings, {name}!"
                new_record = Name(name = name)
                new_record.save()
                return render(request,'greet_app/hello.html', {'title':'Hello!','content':content} )
            #  print(form.cleaned_data['start_date'])
            # period_start = form.cleaned_data['start_date']
            # period_end = form.cleaned_data['end_date']
            # period = [period_start,period_end]
            # result_incomes = Income.objects.all().filter(date__range =period ).aggregate(sum = Sum('amount')).get('sum')
            # if result_incomes == None:
            #     result_incomes = 0
            # result_expences = Expense.objects.all().filter(date__range =period ).aggregate(sum = Sum('amount')).get('sum')
            # if result_expences == None:
            #     result_expences = 0
            # result_balance = result_incomes - result_expences            
            # return render(request,'f_app/stats_for_period.html',{'title':'Stats for period','form': form, 'result_title': f" For period {period_start} to {period_end}", 
            # 'result_incomes':f"Incomes: {result_incomes} UAH",'result_expences': f'Expences: {result_expences} UAH','result_balance':f'Balance: {result_balance} UAH' })
            

    form = Your_name()
    return render(request, 'greet_app/index.html', {'title':"What's your name?", 'form': form, 'name':''})


def show_all(request):
    # return HttpResponse("Show_all test")
    all_names = Name.objects.all()
    template = loader.get_template('greet_app/show_all.html')
    context = {
        'all_names': all_names
    }
    return HttpResponse(template.render(context, request))
