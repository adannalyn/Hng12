##
from django.http import JsonResponse
from math import isqrt
from django.views.decorators.csrf import csrf_exempt
import requests

# Create your views here.

@csrf_exempt
def get_number(request):
    if request.method != 'GET':
        return JsonResponse({"error": "Invalid request method"}, status=405)
    
    number_str = request.GET.get('number')

    if number_str is None:
        return JsonResponse({
            "error": "Number parameter is required"}, status=400)

    try:
        number = int(number_str)
    except ValueError:
        return JsonResponse({
            "number": "alphabet",
            "error": True
            }, status=400)
    
    def check_prime(n):
        if n < 2:
            return False
        for i in range(2, isqrt(n) + 1):
            if n % i == 0:
                return False
        return True
        
    def check_perfect(n):
        if n <= 0:
            return False
        sums = 1
        for i in range(2, isqrt(n) + 1):
            if n % i == 0:
                sums += i + (n // i)
        return sums == n

    def check_armstrong(n):
        if n < 0:
            return False
        s = str(n)
        b = len(s)
        sums = sum(int(digit)**b for digit in s)
        return sums == n
 
    def check_parity(n):
        if n % 2 == 0:
            return "even"
        else:
            return "odd"

    def add_number(n):
        sums = 0
        for i in str(abs(n)):
            sums += int(i)
        return sums

    prime = check_prime(number)
    perfect = check_perfect(number)
    armstrong = check_armstrong(number)
    parity = check_parity(number)
    adds = add_number(number)

    properties = []
    if armstrong:
        properties.append("Armstrong")
    if parity == "odd":
        properties.append("odd")
    if parity == "even":
        properties.append("even")

    try:
        abs_number = abs(number)
        fun_fact_response = requests.get(f"http://numbersapi.com/{abs_number}/math?json")
        fun_fact_response.raise_for_status()
        fun_fact_data = fun_fact_response.json()
        fun_fact = fun_fact_data.get("text", f"Fun fact about {number} not found")
    except requests.exceptions.RequestException as e:
        fun_fact = f"Could not retrieve fun fact about {number}. Error: {e}"

        data = {
            "number": number,
            "is_prime": prime,
            "is_perfect": perfect,
            "properties": properties,
            "digit_sum": adds,
            "fun_fact": fun_fact
        }
        
        return JsonResponse(data)
