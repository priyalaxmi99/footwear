from django.shortcuts import render,redirect
from .models import Bond

# Create your views here.
def home(request):
	return render(request,'index.html')

def about(request):
	return render(request,'about.html')

def contact(request):
	if request.method == "POST":
		name=request.POST["username"]
		mail=request.POST["usermail"]
		job=request.POST["userjob"]
		msg=request.POST["message"]
		print(name)
		print(mail)
		print(job)
		print(msg)

		object_user = Bond(
			u_name = name,
			u_mail = mail,
			u_job = job,
			u_msg = msg
			)
		object_user.save()
	return render(request,'contact.html')

def read(request):
	obj=Bond.objects.all()
	print(obj)
	return render(request,"read.html",locals())

def readfile(request):
	if request.method =="POST":
		mails=request.POST["usermail"]
		print(mails)

		obj_file=Bond.objects.get(u_mail=mails)
		print(obj_file)
	return render(request,"readfile.html",locals())

def update(request):
	if request.method=="POST":
		if request.POST["form_name"]== "form1":
			mails=request.POST["usermail"]
			print(mails)

			obj_form=Bond.objects.get(u_mail=mails)
		if request.POST["form_name"]=="form2":
			user_name=request.POST["username"]
			user_mail=request.POST["usermail"]
			user_job=request.POST["userjob"]
			user_msg=request.POST["message"]
			print(user_mail)

			obj_form2=Bond.objects.get(u_mail=user_mail)
			obj_form2.u_name=user_name
			obj_form2.u_mail=user_mail
			obj_form2.u_job=user_job
			obj_form2.u_msg=user_msg

			obj_form2.save()
	return render(request,"update.html",locals())

def delete(request):
	if request.method=="POST":
		get_mail=request.POST["usermail"]
		print(get_mail)

		obj_del=Bond.objects.filter(u_mail=get_mail)
		obj_del.delete()
		return redirect("read")
	return render(request,"delete.html")

def pathvalue(request,mynum):
	return render(request,"pathvalue.html",locals())
	