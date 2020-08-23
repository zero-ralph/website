from ..base_imports import *


class LoginRequiredMixin(View):

    def dispatch(self, request, *args, **kwargs):
        route = redirect(reverse("login"))
        if request.user.is_authenticated:
            route = super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)
        return route
    