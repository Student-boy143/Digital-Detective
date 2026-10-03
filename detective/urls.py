from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('cases/', views.CaseListView.as_view(), name='case_list'),

    path(
        'cases/<int:pk>/',
        views.CaseDetailView.as_view(),
        name='case_detail'
    ),

    path(
        'cases/<int:case_id>/update/',
        views.case_update,
        name='case_update'
    ),
    path(
        'cases/<int:case_id>/delete/',
        views.case_delete,
        name='case_delete'
    ),
    path('cases/create/', views.case_create, name='case_create'),
    path('jsx-demo/', views.jsx_demo, name='jsx_demo'),
    path('verbatim-demo/', views.verbatim_demo, name='verbatim_demo'),
]