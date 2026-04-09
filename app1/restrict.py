from django.shortcuts import redirect, render


def redirect_if_logged_in(view_func):
    def get_id(request):
        if request.session.get('user_id'):
            return redirect('landing')   
        return view_func(request)
    return get_id



def noentry_order(view_func):
    def get_id(request):
        if request.session.get('user_id'):
            username = request.session.get('user_username')
            return render(request,'app1/order.html',{'username':username})
        return redirect('login')
    return get_id

