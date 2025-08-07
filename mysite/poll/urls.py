from django.urls import path, include
from . import views

# at end of django part 3, I skipped the part about re-writing hard-coded urls

app_name = "poll"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path("poll/CSS_practice", views.CSS_practice, name="practice"),
    path("TWCSS/", include('TWCSS.urls')),
]