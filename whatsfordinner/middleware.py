from .utils import set_current_user, remove_current_user

class CurrentUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):

        set_current_user(getattr(request, 'user', None))

        response = self.get_response(request)
  
        remove_current_user()

        return response
