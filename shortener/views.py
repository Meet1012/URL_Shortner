from django.shortcuts import render
from django.http import HttpResponse
from .models import url_schema
from datetime import datetime, timezone
from shortener.forms import Create_form, Edit_from, Fetch_form, Delete_form
import hashlib


def initial(request):
    current_time = datetime.now(timezone.utc)
    formatted_time = current_time.strftime('%Y-%m-%dT%H:%M:%SZ')
    form = Create_form()
    shorturl = None
    if request.method == "POST":
        form = Create_form(request.POST)
        if form.is_valid():
            print("Form Is Valid")
            url = form.cleaned_data['url']
            print(f"URL: {url}")
            shorturl = hashlib.sha256(url.encode()).hexdigest()[-6:]
            try:
                print("Trial")
                response = url_schema.objects.get(shortCode = shorturl)
                response.url = url
                print(shorturl)
            except:
                url_schema.objects.create(
                    url=str(url),
                    shortCode=str(shorturl),
                    createdAt=formatted_time,
                    updatedAt=formatted_time
                )
    return render(request, "index.html", {"create_form": form, "short_url": shorturl})


def get_all(request):
    form = Fetch_form()
    original_url = None
    count = None
    status = None
    if request.method == "POST":
        form = Fetch_form(request.POST)
        if form.is_valid():
            shorten_url = form.cleaned_data["shorten_url"]
            try:
                response = url_schema.objects.get(shortCode=shorten_url)
                original_url = response.url
                count = response.count + 1
                response.count = count
                response.save()
            except:
                status = 404
    return render(request, "fetch.html", {"fetch_form": form, "original_url": original_url, "count": count, "status": status})


def delete(request):
    form = Delete_form()
    status = 100
    if request.method == "POST":
        form = Fetch_form(request.POST)
        if form.is_valid():
            shorten_url = form.cleaned_data["shorten_url"]
            try:
                response = url_schema.objects.get(shortCode = shorten_url)
                response.delete()
                status = 200
            except:
                status = 404
    return render(request, "delete.html", {"delete_form": form, "status": status})


def update(request):
    current_time = datetime.now(timezone.utc)
    formatted_time = current_time.strftime('%Y-%m-%dT%H:%M:%SZ')
    form = Edit_from()
    status_code = 0
    if request.method == "POST":
        form = Edit_from(request.POST)
        if form.is_valid():
            shorten_url = form.cleaned_data["shorten_url"]
            url = form.cleaned_data["url"]
            try:
                response = url_schema.objects.get(shortCode=shorten_url)
                response.url = url
                response.updatedAt = formatted_time
                status_code = 201
                response.save()
            except:
                status_code = 404
    return render(request, "update.html", {"edit_form": form, "status_code": status_code})
