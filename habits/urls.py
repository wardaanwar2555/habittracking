from django.contrib import admin
from django.urls import path
from appname.views import home, contact, base, login, signin, summer,add,edits,delete ,dashboard,settings,insertuser,insert_habit,habit_list,edit_habit,delete_habit

urlpatterns = [
    # Home page - accessible at /

    path('', home, name="home"),
    
    # Alternative route to home page at /index/
    path('index.html', home, name="home"),
    
    # Signup page at /signup/
    path('signup.html/', contact, name="contact"),
    
    # Login page at /login/
    path('login', login, name="login"),
    
    # Signin page at /signin/
    
    
    # Base template page at /base/
    path('base.html', base, name="base"),

    path('add.html', add , name="add"),
    # Summer page at /login.html/
    path('login.html/', summer, name="summer"),
      path('edits.html', edits , name="edits"),
      path('delete.html', delete , name="delete"),
     path('dashboard.html/', dashboard , name="dashboard"),
      path('settings.html/', settings , name="settings"),
    path('signin', signin, name="signin"),
    # Django admin interface at /admin/
    path('insertuser', insertuser , name="insertuser"),
    path('insert_habit',insert_habit , name="insert_habit"),
  path('edit_habit', edit_habit, name="edit_habit"),
  path('delete_habit', delete_habit, name="delete_habit"),
    path('habit_list',habit_list, name="habit_list"),
    path('admin/', admin.site.urls),
]
