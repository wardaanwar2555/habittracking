from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout
from django.http import HttpResponse
from django.contrib import messages
from .models import Ab



from django.shortcuts import render, redirect
from .models import User

  # Assuming Ab is your model for habits

def habit_list(request):
    habits = Ab.objects.all()
    
    # Debugging to check if habits has data
   # This will print in your terminal or console

    return render(request, 'base.html', {'habits': habits})

def insertuser(request):
    if request.method == "POST":
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')

        if email and password:  # Ensure both fields are provided
            try:
                user = User(uemail=email, upassword=password)
                user.save()
                print(f"✅ User {email} inserted successfully!")
             
                habits = Ab.objects.all()
                return render(request, 'base.html', {'habits': habits})  # Redirect after successful insertion
            except Exception as e:
                print(f"❌ Database Error: {e}")
        else:
            print("❌ Email or Password is missing")
       
    # Render base.html for GET requests or failed insertions
    habits = Ab.objects.all()
    habit_count = Ab.objects.count()
    print(f"Total habits in database: {habit_count}")
    # Debugging to check if habits have data
    print(habits)  # This will print to your terminal or console
    print(habits.query) 
    return render(request, 'base.html', {'habits': habits})
  # Assuming your model is named 'Habit' instead of 'Ab'

def insert_habit(request):
    if request.method == "POST":
        try:
            # Get form data
            habit_name = request.POST.get('habit_name', '').strip()
            frequency = request.POST.get('frequency', '').strip()
            reminder_time = request.POST.get('reminder_time', '').strip()
            notes = request.POST.get('notes', '').strip()

            # Validate required fields
            if not habit_name or not frequency:
                messages.error(request, "❌ Habit Name and Frequency are required.")
                return render(request, 'add.html')

            # Create new habit matching the model field names
            habit = Ab(
                habit_name=habit_name,  # Match the model field name
                frequency=frequency,
                reminder_time=reminder_time if reminder_time else None,
                notes=notes
            )
            habit.save()

            print(f"✅ Habit '{habit.habit_name}' inserted successfully!")
            messages.success(request, f"✅ Habit '{habit.habit_name}' inserted successfully!")
            return redirect('add.html')

        except Exception as e:
            print(f"❌ Error creating habit: {str(e)}")
            messages.error(request, "❌ An error occurred while creating the habit.")
            return render(request, 'add.html')

    return render(request, 'add.html')

def edit_habit(request):
    if request.method == "POST":
        try:
            habit_id = request.POST.get('habit_id')  # Will be None if adding new

            # Get form data
            habit_name = request.POST.get('habit_name', '').strip()
            frequency = request.POST.get('frequency', '').strip()
            reminder_time = request.POST.get('reminder_time', '').strip()
            notes = request.POST.get('notes', '').strip()

            # Validate required fields
            if not habit_name or not frequency:
                messages.error(request, "❌ Habit Name and Frequency are required.")
                return render(request, 'base.html')

            if habit_id:  # Edit existing habit
                habit = get_object_or_404(Ab, id=habit_id)
                habit.habit_name = habit_name
                habit.frequency = frequency
                habit.reminder_time = reminder_time if reminder_time else None
                habit.notes = notes
                habit.save()
                messages.success(request, f"✅ Habit '{habit.habit_name}' updated successfully!")
                print(f"✅ Habit '{habit.habit_name}' updated successfully!")
            else:  # Add new habit
                habit = Ab(
                    habit_name=habit_name,
                    frequency=frequency,
                    reminder_time=reminder_time if reminder_time else None,
                    notes=notes
                )
                habit.save()
                messages.success(request, f"✅ Habit '{habit.habit_name}' added successfully!")
                print(f"✅ Habit '{habit.habit_name}' added successfully!")

            return redirect('base.html')  # Adjust this if you want to redirect to a specific page

        except Exception as e:
            print(f"❌ Error: {str(e)}")
            messages.error(request, "❌ An error occurred while saving the habit.")
            return render(request, 'base.html')

    # GET request: Show form with all habits
    habits = Ab.objects.all()
    return render(request, 'base.html', {'habits': habits})
   
def signin(request):
     if request.method == "POST":
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')

        if email and password:  # Ensure both fields are provided
            try:
                user = User(uemail=email, upassword=password)
                user.save()
                print(f"✅ User {email} inserted successfully!")
             

                return redirect('/login.html')  # Redirect after successful insertion
            except Exception as e:
                print(f"❌ Database Error: {e}")
        else:
            print("❌ Email or Password is missing")
         
    # Render base.html for GET requests or failed insertions
        return render(request, 'login.html', {})

# Login view




def delete_habit(request):
    if request.method == 'POST':
        habit_id = request.POST.get('habit_id')
        if habit_id:
            try:
                habit = get_object_or_404(Ab, id=habit_id)
                habit_name = habit.habit_name
                habit.delete()
                messages.success(request, f"🗑️ Habit '{habit_name}' deleted successfully!")
                print(f"🗑️ Habit '{habit_name}' deleted successfully!")
            except Exception as e:
                messages.error(request, "❌ Error deleting habit.")
                print(f"❌ Error deleting habit: {str(e)}")
        else:
            messages.warning(request, "⚠️ No habit ID provided.")
    return redirect('base.html')

def login(request):
    if request.method == "POST":
        # Get username and password from the form
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)  # Log the user in
            messages.success(request, "Login successful!")
            return redirect('home')  # Redirect to home page after login
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')

    # Only fetch habits when rendering the page, not on POST requests
    habits = Ab.objects.all()
    habit_count = Ab.objects.count()
    print(f"Total habits in database: {habit_count}")
    # Debugging to check if habits have data
    print(habits)  # This will print to your terminal or console
    print(habits.query) 
    return render(request, 'addd.html', {'habits': habits})
# Home page view
def home(request):
    return render(request, "index.html")  # Render the home page

# Summer page view
def summer(request):
    return render(request, "login.html/")  # Render login.html for the summer page
def contact(request):
    return render(request, "signup.html")  # Render signup.html for the contact page

def add(request):
    return render (request,"add.html")
def edits(request):
    return render(request,"edits.html")
def delete(request):
    return render(request,'delete.html')
# Base template page view
def base(request):
    return render(request, "base.html")  # Render the base template
def dashboard(request):
    return render(request,"dashboard.html")
# Base template page view
def settings(request):
    return render(request, "settings.html")  # Render the base template
# Logout view
def logout_view(request):
    logout(request)  # Log the user out
    messages.success(request, "You have been logged out.")
    return redirect('login')  # Redirect to login page


