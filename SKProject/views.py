from django.http import HttpResponse 
from django.shortcuts import render 

def homepage(request) :
    # data={
    #     'title' : 'home new' ,
    #     'bdata' : 'welcome to wscubetech' ,
    #     'cdata' : ['php' , 'java' , 'django'] ,
    #     'numbers' : [10,20,30,40,50] ,
    #     'student_Details' :[
    #         {'name':'pradip' , 'mobile' : 7854845648} ,
    #         {'name' :'rohit' , 'mobile' : 9965742810}
    #     ]
    # }
    # return render(request ,"index.html" , data)
    return render(request ,"index.html")

def aboutus(request) :
    return render(request ,"about.html")

def services(request) :
    return render(request ,"services.html")

def contect(request) :
    return render(request ,"contect.html")

def courseDetails(request , courseid) :
    return render(request ,"index.html")