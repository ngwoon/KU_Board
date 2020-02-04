from django.views.generic.base import TemplateView

# 로그인 세션에 따라 template_name이 index.html 혹은 board_index.html로 이동


class HomeView(TemplateView):
    template_name = 'index.html'
