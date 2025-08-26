# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib import messages
# from .models import Trip
# from .form import TripForm
# from django.db.models import Sum, Count
# from datetime import datetime, timedelta
#
#
# def dashboard(request):
#     total_trips = Trip.objects.count()
#     pending_payments = Trip.objects.filter(payment_status='Pending').count()
#     total_profit = Trip.objects.aggregate(Sum('profit'))['profit__sum'] or 0
#     total_receivable = Trip.objects.aggregate(Sum('receivable'))['receivable__sum'] or 0
#     recent_trips = Trip.objects.order_by('-date')[:5]
#
#     context = {
#         'total_trips': total_trips,
#         'pending_payments': pending_payments,
#         'total_profit': total_profit,
#         'total_receivable': total_receivable,
#         'recent_trips': recent_trips,
#     }
#     return render(request, 'dashboard.html', context)
#
#
# def add_trip(request):
#     if request.method == 'POST':
#         form = TripForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Trip added successfully!')
#             return redirect('add_trip')
#     else:
#         form = TripForm()
#     return render(request, 'add_trip.html', {'form': form})
#
#
# def trip_list(request):
#     trips = Trip.objects.all().order_by('-date')
#     search = request.GET.get('search')
#     if search:
#         trips = trips.filter(bilty_number__icontains=search) | \
#                 trips.filter(vehicle_number__icontains=search) | \
#                 trips.filter(driver_name__icontains=search)
#
#     payment_filter = request.GET.get('payment_status')
#     if payment_filter:
#         trips = trips.filter(payment_status=payment_filter)
#
#     context = {
#         'trips': trips,
#         'total_count': trips.count(),
#     }
#     return render(request, 'trip_list.html', context)
#
#
# def edit_trip(request, pk):
#     trip = get_object_or_404(Trip, pk=pk)
#     if request.method == 'POST':
#         form = TripForm(request.POST, instance=trip)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Trip updated successfully!')
#             return redirect('trip_list')
#     else:
#         form = TripForm(instance=trip)
#     return render(request, 'edit_trip.html', {'form': form, 'trip': trip})
#
#
# def delete_trip(request, pk):
#     trip = get_object_or_404(Trip, pk=pk)
#     if request.method == 'POST':
#         trip.delete()
#         messages.success(request, 'Trip deleted successfully!')
#         return redirect('trip_list')
#     return render(request, 'delete_trip.html', {'trip': trip})

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.db.models import Sum
from .models import Trip
from .form import TripForm

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('user_login')

@login_required(login_url='user_login')
def dashboard(request):
    total_trips = Trip.objects.count()
    pending_payments = Trip.objects.filter(payment_status='Pending').count()
    total_profit = Trip.objects.aggregate(Sum('profit')).get('profit__sum') or 0
    total_receivable = Trip.objects.aggregate(Sum('receivable')).get('receivable__sum') or 0
    recent_trips = Trip.objects.order_by('-date')[:5]

    context = {
        'total_trips': total_trips,
        'pending_payments': pending_payments,
        'total_profit': total_profit,
        'total_receivable': total_receivable,
        'recent_trips': recent_trips,
        'is_admin': request.user.is_staff,
    }
    return render(request, 'dashboard.html', context)

@login_required(login_url='user_login')
def add_trip(request):
    if request.method == 'POST':
        form = TripForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Trip added successfully!')
            return redirect('add_trip')
    else:
        form = TripForm()
    return render(request, 'add_trip.html', {'form': form})

@login_required(login_url='user_login')
def trip_list(request):
    if not request.user.is_staff:
        messages.error(request, 'Access denied')
        return redirect('dashboard')

    trips = Trip.objects.all().order_by('-date')
    context = {
        'trips': trips,
        'total_count': trips.count(),
    }
    return render(request, 'trip_list.html', context)

@login_required(login_url='user_login')
def edit_trip(request, pk):
    if not request.user.is_staff:
        messages.error(request, 'Access denied')
        return redirect('dashboard')

    trip = get_object_or_404(Trip, pk=pk)
    if request.method == 'POST':
        form = TripForm(request.POST, instance=trip)
        if form.is_valid():
            form.save()
            messages.success(request, 'Trip updated successfully!')
            return redirect('trip_list')
    else:
        form = TripForm(instance=trip)
    return render(request, 'edit_trip.html', {'form': form, 'trip': trip})

@login_required(login_url='user_login')
def delete_trip(request, pk):
    if not request.user.is_staff:
        messages.error(request, 'Access denied')
        return redirect('dashboard')

    trip = get_object_or_404(Trip, pk=pk)
    if request.method == 'POST':
        trip.delete()
        messages.success(request, 'Trip deleted successfully!')
        return redirect('trip_list')
    return render(request, 'delete_trip.html', {'trip': trip})
