from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm, MyPasswordResetForm, MypasswordChangeForm,MySetPasswordForm

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('category/<slug:val>/', views.CategoryView.as_view(), name='category'),
    path('product-detail/<int:pk>/', views.ProductDetail.as_view(), name='product-detail'),
    # Login redirect path
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('category-title/<val>/', views.CategoryTitle.as_view(), name='category-title'),

    # Update address
    path('updateAddress/<int:pk>/', views.updateAddress.as_view(), name='updateAddress'),

    # Registration
    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),

    # Login process
    path('accounts/login/', auth_views.LoginView.as_view(template_name='app/login.html', authentication_form=LoginForm), name='login'),

    # Password reset & forgetpassword
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='app/passwordreset.html',form_class=MyPasswordResetForm),name='password_reset'),

    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='app/passwordresetdone.html'),name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='app/passwordresetconfirm.html',form_class=MySetPasswordForm),name='password_reset_confirm'),

    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='app/passwordresetcomplete.html'),name='password_reset_complete'),
 
    #add to cart
    #path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    #path('cart/', views.show_cart, name='showcart'),



    #logout
   path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    # Password change
     path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name='app/changepassword.html',form_class=MypasswordChangeForm,success_url='/passwordchangedone/'), name='passwordchange'),
    path('passwordchangedone/', auth_views.PasswordChangeDoneView.as_view(template_name='app/passwordchangedone.html'), name='passwordchangedone'),






] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
