from django.shortcuts import render
from apps.accounts.models import CustomUser
from django.db.models import Q

def users(request):

    query = request.GET.get('query')
    users_list = CustomUser.objects.all().order_by('id')

    if query:
        users_list = users_list.filter(Q(first_name__icontains=query) | Q(last_name__icontains=query))

    context = {
        'users': users_list,
        'query': query
    }

    return render(request, "accounts/users.html", context)