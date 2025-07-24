from django.urls import path
from . import views

# at end of django part 3, I skipped the part about re-writing hard-coded urls

app_name = "poll"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/result", views.result, name="result"),
    path("<int:question_id>/vote", views.vote, name="vote"),
]