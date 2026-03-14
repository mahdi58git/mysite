from django.http import HttpResponse,JsonResponse
def httptest(request):
    return HttpResponse("hi")
def jsonteat(request):
    return JsonResponse({"hello":"hi mahdi your very vry good"})