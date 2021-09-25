
def get_full_name(request):

    if request.user.is_authenticated and (request.user.profile.first_name or request.user.profile.last_name):
        return {
            'full_name': request.user.profile.get_full_name()
        }
    else:
        return {}





