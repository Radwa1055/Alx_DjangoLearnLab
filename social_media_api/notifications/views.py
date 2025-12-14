from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Notification


@api_view(['GET'])
def my_notifications(request):
    qs = Notification.objects.filter(recipient=request.user).order_by('-created_at')
    return Response([
        {
            'actor': n.actor.username,
            'verb': n.verb,
            'read': n.is_read
        } for n in qs
    ])


# Create your views here.
