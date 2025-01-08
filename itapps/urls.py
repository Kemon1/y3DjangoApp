from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from users import views as user_views
from courses import views as courses_views
from django.conf import settings
from django.conf.urls.static import static
from modules.views import ModuleListView, ModuleDetailView, enroll_in_module

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('itreporting.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile', user_views.profile, name = 'profile'),
    path('register', user_views.register, name = 'register'), 
    path('course', courses_views.my_course, name='my_course'),
    path('modules/', ModuleListView.as_view(template_name='modules/module_list.html'), name = 'modules'),
    path('module/<int:pk>/', ModuleDetailView.as_view(template_name='modules/module_detail.html'), name = 'module-detail'),
    path('enroll/<int:module_id>/', enroll_in_module, name = 'enroll-in-module'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name = 'users/password_reset.html'), name ='password_reset'),
    path('password_reset/done', auth_views.PasswordChangeDoneView.as_view(template_name = 'users/password_reset_done.html'), name ='password_reset_done'),
    path('reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="users/password_reset_confirm.html"),  name = "password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="users/password_reset_complete.html"), name = "password_reset_complete"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)