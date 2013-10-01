from django.shortcuts import render_to_response
from django.core.paginator import Paginator
from usercrud.usertracker.models import User
from django.template import RequestContext


def render_response(req, *args, **kwargs):
    kwargs['context_instance'] = RequestContext(req)
    return render_to_response(*args, **kwargs)


def list(request, page = 1, message = ""):
    page = int(page)
    user_list = Paginator(User.objects.all(), 5)
    has_previous = user_list.page(page).has_previous()
    has_next = user_list.page(page).has_next()


    return render_response(
        request,
        'Users/list.html',
        {'user_list': user_list.page(page),
         'has_previous': has_previous,
         'previous_page': page - 1,
         'has_next': has_next,
         'next_page': page + 1,
         'message': message}
    )

def new(request):
    return render_response(
        request,
        'users/form.html',
        {'action': 'add', 'button': 'Add'}
    )


def edit(request, id):
    user = User.objects.get(id=id)
    return render_response(
        request,
        'users/form.html',
        {'user': user,
         'action': 'update/' + id,
         'button': 'Update'}
    )


def add(request):
    user_firstname = request.POST['user_firstname']
    user_lastname = request.POST['user_lastname']
    user_email = request.POST['user_email']
    user = User(
        user_firstname = user_firstname,
        user_lastname = user_lastname,
        user_email = user_email
    )
    user.save()
    return list(request, message='User born!')


def update(request, id):
    user = User.objects.get(id=id)
    user.user_firstname = request.POST['user_firstname']
    user.user_lastname = request.POST['user_lastname']
    user.user_email = request.POST['user_email']
    user.save()
    return list(request, message='User perfected!')


def delete(request, id):
    User.objects.get(id=id).delete()
    return list(request, message='User vanquished!')

