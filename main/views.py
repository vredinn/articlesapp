from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render, redirect
from .models import Article, Category, Comment
from django.db.models import Q
import re


def index(request):
    query = request.GET.get("q", "")
    selected_categories = request.GET.getlist("category")

    if query:
        query = re.escape(query)

    # Фильтрация по категории
    articles = Article.objects.order_by("-public_date")
    categories = Category.objects.all()

    if selected_categories and not query:
        articles = articles.filter(category_id__in=selected_categories)
    if query and not selected_categories:
        articles = articles.filter(title__iregex=query)

    if query and selected_categories:
        articles = articles.filter(
            title__iregex=query, category_id__in=selected_categories
        )

    # Пагинация
    paginator = Paginator(articles, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "main/index.html",
        {
            "page_obj": page_obj,
            "query": query,
            "categories": categories,
            "selected_category": selected_categories,
        },
    )


def article_detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    categories = request.GET.getlist("category")
    if request.method == "POST":
        username = request.POST.get("username")
        comment_text = request.POST.get("comment_text")

        if username and comment_text:
            Comment.objects.create(
                article=article, username=username, comment_text=comment_text
            )
            query_params = request.GET.urlencode()
            return redirect(f"{request.path}?{query_params}")

    return render(
        request,
        "main/article_detail.html",
        {
            "article": article,
            "categories": categories,
        },
    )
