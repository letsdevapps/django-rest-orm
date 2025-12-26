from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User

@csrf_exempt  # Para simplificar no exemplo (não recomendado para produção)
def create_user(request):
    if request.method == 'POST':
        data = request.POST
        user = User.objects.create(name=data['name'], email=data['email'])
        return JsonResponse({'id': user.id, 'name': user.name, 'email': user.email})

def get_users(request):
    if 'name' in request.GET:
        name = request.GET['name']
        users = User.objects.filter(name__icontains=name)
    else:
        users = User.objects.all()
    user_list = [{'id': user.id, 'name': user.name, 'email': user.email} for user in users]
    return JsonResponse(user_list, safe=False)

