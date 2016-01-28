from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect


# Create your views here.
from .forms import PostForm
from .models import Post

def post_create(request):
	form = PostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Succesfully Created")
		return HttpResponseRedirect(instance.get_absolute_url())

	#if request.method == "POST":
	#	print request.POST.get("content")
	#	print request.POST.get("title")
	context = {
		"form": form,
	}
	return render(request, "post_form.html", context)

def post_detail(request, slug=None):
	instance = get_object_or_404(Post, slug=slug)
	context = {
		"title": instance.title,
		"instance": instance,
	}
	return render(request, "post_detail.html", context)

# produkty views - poczatek

def wedliny_list(request, slug=None):
	wedliny_query = Post.objects.filter(kategoria=Post.WEDLINY)
	context = {
		"wedliny_q": wedliny_query,
	}
	return render(request, "wedliny.html", context)

def garmazeria_list(request, slug=None):
	garmazeria_query = Post.objects.filter(kategoria=Post.GARMAZERIA)
	context = {
		"garmazeria_q": garmazeria_query,
	}
	return render(request, "garmazeria.html", context)

def art_spozywcze_list(request, slug=None):
	art_spozywcze_query = Post.objects.filter(kategoria=Post.ART_SPOZYWCZE)
	context = {
		"art_spozywcze_q": art_spozywcze_query,
	}
	return render(request, "post_detail.html", context)


def napoje_list(request, slug=None):
	napoje_query = Post.objects.filter(kategoria=Post.NAPOJE)
	context = {
		"napoje_q": napoje_query,
	}
	return render(request, "post_detail.html", context)

# produkty views -  koniec

def post_list(request):
	queryset_list = Post.objects.filter(kategoria=Post.POST).order_by("-timestamp")
	paginator = Paginator(queryset_list, 4) # Show 10 contacts per page

	page = request.GET.get('post')
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)

	context = {
		"object_list": queryset,
		"title": "List"
	}	
	return render(request, "post_list.html", context)


def post_update(request, slug=None):
	instance = get_object_or_404(Post, slug=slug)
	form = PostForm(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		#messege success
		messages.success(request, "Item Saved")
		return HttpResponseRedirect(instance.get_absolute_url())
		
	context = {
		"title": instance.title,
		"instance": instance,
		"form": form,
	}
	return render(request, "post_form.html", context)

def post_delete(request, slug=None):
	instance = get_object_or_404(Post, slug=slug)
	instance.delete()
	messages.success(request, "Succesfully Deleted")
	return redirect("posts:list")