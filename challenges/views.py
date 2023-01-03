from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
monthly_challenges = {
    "january": "Work out at least 3x a week",
    "february": "Prepare Goldie's room for her",
    "march": "Be vigilant for your wife and baby",
    "april": "Be vigilant for your wife and baby",
    "may": "Be vigilant for your wife and baby",
    "june": "Be vigilant for your wife and baby",
    "july": "Be vigilant for your wife and baby",
    "august": "Be vigilant for your wife and baby",
    "september": "Be vigilant for your wife and baby",
    "october": "Be vigilant for your wife and baby",
    "november": "Be vigilant for your wife and baby",
    "december": "Be vigilant for your wife and baby"
}


def index(request):
    list_items = ""

    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    response_data = f"<ul>{list_items}</ul>"

    return HttpResponse(response_data)


def monthly_challenge_num(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("This month is not supported")
    else:
        forward_month = months[month - 1]
        forward_path = reverse("month-challenge", args=[forward_month])
        return HttpResponseRedirect(forward_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("This month is not supported")
