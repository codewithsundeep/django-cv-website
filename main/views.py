from django.shortcuts import render
from main.models import personal_info, Skills, Languages, Current_Work, Work_Experience, Education, Social_Links, contact
from django.contrib import messages

# Create your views here.


def read(request):

    try:
        pi = personal_info.objects.all()[0]

    except:
        pi = ""

    try:
        sk = Skills.objects.all
    except:
        sk = ""
    try:
        lg = Languages.objects.all

    except:
        lg = ""

    try:
        cw = Current_Work.objects.all()[0]
    except:
        cw = ""
    try:
        we = Work_Experience.objects.all
    except:
        we = ""
    try:
        edu = Education.objects.all
    except:
        edu = ""

    try:
        scl = Social_Links.objects.all()[0]
    except:
        scl = ""

    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        Ctk = contact(Name=name, Email=email, Subject=subject, Message=message)
        Ctk.save()
        messages.success(request, """
                    <div class="w3-panel                        w3-teal">
            
                    <h2>Message has been sent                       succesfully
            
                    </h2>
            
                    <p>We will reply you soon as                        possible.</p>
                    <span onclick="this.                    parentElement.style.                display='none'"
             class="w3-button                       w3-display-topright">&times;</span>
                    </div>
                    """)


    context = {
    "my_info": pi,
    "skill": sk,
    "lang": lg,
    "cwork": cw,
    "wex": we,
    "ed": edu,
    "social": scl

}


    return render(request, "index.html", context)
