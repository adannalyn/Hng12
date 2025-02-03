from django.http import JsonResponse
import pytz
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def get_info(request):
    if request.method == 'GET':
        email = "ezeadannalyn@gmail.com"
        now_utc = timezone.now()
        current_time = now_utc.strftime("%Y-%m-%dT%H:%M:%SZ")
        github_url = "https://github.com/adannalyn/Hng12.git"

        data = {
            "email": email,
            "datetime": current_time,
            "github_url": github_url,
        }
        return JsonResponse(data)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=405)
