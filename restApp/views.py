from django.shortcuts import render

from snippets.models import Snippet


def home(request):
	return render(request, "index.html", {
		"Snippets": Snippet.objects.all()[:10]
	})
