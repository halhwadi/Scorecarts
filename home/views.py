from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from . forms import LoginForm, TicketForm
from . models import TicketModel
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required, user_passes_test

from django.views.generic.edit import CreateView, DeleteView, UpdateView

# Create your views here.


def login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        username = form['username'].value()
        password = form['password'].value()
        user = auth.authenticate(username=username, password=password)
        if form.is_valid():
            if user is not None:
                auth.login(request, user)
                return redirect('tickets_list')
            else:
                messages.error(request, "Invalid credentials")
                return render(request, "login.html", context={"form": form})
        else:
            errors = form.errors
            messages.error(request, "Invalid credentials")
            return render(request, "login.html", context={"form": form, 'errors': errors})
    else:
        return render(request, "login.html", context={"form": form})

@login_required
def logout(request):
    auth.logout(request)
    return redirect('/')


@login_required
def create_ticket(request):
    form = TicketForm()
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            try:
                createdby = request.user
            except:
                messages.error(request, "Profile issue")
                return redirect('login')
            else:
                instance.createdby = createdby
                instance.save()
                messages.success(request, "Your ticket has been created successfully")
                return redirect('tickets_list')
        else:
            errors = form.errors
            messages.error(request, "Check the error")
            return render(request, 'create_ticket.html', context={'errors': errors})
    else:
        return render(request, 'create_ticket.html', context={'form': form})


@login_required
def tickets_list(request):
    try:
        createdby = request.user
    except:
        messages.error(request, "Profile issue")
        return redirect('login')
    else:
        tickets = createdby.ticket.all().order_by('-date')

        date = request.GET.get('date')
        status = request.GET.get('status')
        priority = request.GET.get('priority')

        status_list = []
        for ticket in tickets:
            status_list += [status for status in ticket.status if status not in status_list]

        priority_list = []
        for ticket in tickets:
            priority_list += [priority for priority in ticket.priority if priority not in priority_list]

        if (date is not None) and (date != ""):
            tickets = tickets.order_by(date)

        if (status is not None) and (status != ""):
            tickets = tickets.filter(status=status)

        if (priority is not None) and (priority != ""):
            tickets = tickets.filter(priority=priority)

        return render(request, "tickets_list.html", context={'tickets': tickets, 'priority_list':priority_list,'status_list':status_list })

@login_required
def view_ticket(request, id):
    try:
        ticket = get_object_or_404(TicketModel, id=id)
    except:
        messages.error(request, "No available ticket with this number")
        return redirect('tickets_list')
    else:
        return render(request,'view_ticket.html', context={'ticket': ticket})


@login_required
def update_ticket(request, id):
    try:
        ticket = get_object_or_404(TicketModel, id=id)
    except:
        messages.error(request, "No available ticket with this number")
        return redirect('tickets_list')
    else:
        if request.user == ticket.createdby:
            form = TicketForm(instance=ticket)

            if request.method == "POST":
                form = TicketForm(request.POST, instance=ticket)

                if form.is_valid():
                    form.save()
                    messages.success(request, "Ticket has been updated successfully")
                    return redirect('view_ticket', id)
                else:
                    errors = form.errors
                    return render(request, "update_ticket.html", context={'form': form, 'errors': errors})

            else:
                return render(request, "update_ticket.html", context={'form': form})

        else:
            messages.error(request, "Authorization restriction")
            return redirect('tickets_list')

@login_required
def delete_ticket(request,id):
    try:
        ticket = get_object_or_404(TicketModel, id=id)
    except:
        messages.error(request, "No available ticket with this number")
        return redirect('tickets_list')
    else:
        if request.user == ticket.createdby:
            ticket.delete()
            messages.success(request, "Ticket has been deleted successfully")
            return redirect('tickets_list')
        else:
            messages.error(request, "Authorization restriction")
            return redirect('tickets_list')


