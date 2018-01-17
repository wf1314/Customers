from django.views.generic import View
from django.contrib.auth.decorators import login_required


class MyRequired(object):

    @classmethod
    def as_view(cls,**initkwargs):
        view = super(MyRequired, cls).as_view(**initkwargs)
        return  login_required(view)


class MyViewRequired(View):

    @classmethod
    def as_view(cls, **initkwargs):
        view = super(MyViewRequired, cls).as_view(**initkwargs)
        return login_required(view)
