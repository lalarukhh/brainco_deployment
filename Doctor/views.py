from django.shortcuts import render , redirect
from Doctor.models import Doctors_Prescription, Patient_Record
from django.shortcuts import render, get_object_or_404
from .models import CustomUser, Patient_Record
from django.core.paginator import Paginator

from django.http import HttpResponse
from fpdf import FPDF

from .forms import ContactForm

from django.core.mail import send_mail
from django.template.loader import render_to_string


from django.contrib.auth import authenticate, login
from .models import CustomUser

def INDEX(request):           #Read values from prescription
   presc_obj=Doctors_Prescription.objects.order_by('-date')        #to add a for loop in html page to read all objects
   
   # code for pagination starts from there
   paginator=Paginator(presc_obj,4)       #ye line bata rahi hai k kitna data lana hai 
   page_number=request.GET.get('page')    # ye line page number get kar rahi hai
   presc_obj_final=paginator.get_page(page_number)
   totalpage=presc_obj_final.paginator.num_pages #this line is use to find the last page by finding total pages
   context={
      'presc_obj':presc_obj_final,
      'lastpage':totalpage,
      'totalpagelist':[n+1 for n in range(totalpage)]
   }
   return render(request,'index.html',context)

def ADD(request):          #Add values in presscription 
   
   if request.method == 'POST':
        doctor_Id=request.POST.get('doctor_Id')
        patient_Id=request.POST.get('patient_Id')
        doctor_Name=request.POST.get('doctor_Name')
        patient_Name=request.POST.get('patient_Name')
        medicine_Name=request.POST.get('medicine_Name')
        medicine_Dossage=request.POST.get('medicine_Dossage')
        date=request.POST.get('date')
        suggestions =request.POST.get('suggestions')
   

        doc_pres=Doctors_Prescription(
            patient_Id=patient_Id,
            doctor_Id=doctor_Id,
            doctor_Name=doctor_Name,
            patient_Name=patient_Name,
            medicine_Name=medicine_Name,
            medicine_Dossage=medicine_Dossage,
            date=date,
            suggestions=suggestions,
        )
   
       
        doc_pres.save()
        return redirect('main_prescription')
   return render(request,'index.html')
   
def Edit(request):
   if request.method == 'POST':
        doctor_Id=request.POST.get('doctor_Id')
        patient_Id=request.POST.get('patient_Id')
        doctor_Name=request.POST.get('doctor_Name')
        patient_Name=request.POST.get('patient_Name')
        medicine_Name=request.POST.get('medicine_Name')
        medicine_Dossage=request.POST.get('medicine_Dossage')
        date=request.POST.get('date')
        suggestions =request.POST.get('suggestions ')

        doc_pres=Doctors_Prescription(
            patient_Id=patient_Id,
            doctor_Id=doctor_Id,
            doctor_Name=doctor_Name,
            patient_Name=patient_Name,
            medicine_Name=medicine_Name,
            medicine_Dossage=medicine_Dossage,
            date=date,
            suggestions=suggestions,
        )
       
        doc_pres.save()
        return redirect('main_prescription')
   return redirect(request,'index.html')

def Update(request, id):
    if request.method == 'POST':
        dI = request.POST.get('doctor_Id')
        pI = request.POST.get('patient_Id')
        dN = request.POST.get('doctor_Name')
        pN= request.POST.get('patient_Name')
        mN = request.POST.get('medicine_Name')
        mD = request.POST.get('medicine_Dossage')
        d = request.POST.get('date')
        s = request.POST.get('suggestions')

        doc_pres = Doctors_Prescription(
         id=id,
         doctor_Id = dI,
         patient_Id=pI,
         doctor_Name = dN,
         patient_Name = pN,
         medicine_Name = mN,
         medicine_Dossage = mD,
         date = d,
         suggestions = s,
        )
        doc_pres.save()
        print(pN)
        
        return redirect('main_prescription')

    return redirect(request,'index.html')

def Delete(request, id):    
    pres_obj = Doctors_Prescription.objects.filter(id=id).delete()
    
    # Redirect to 'main_prescription' view
    return redirect('main_prescription')

def Home(request):
    return render(request,'home.html')
   

def Record_fun(request):           #Read values from prescription
    record_obj=Patient_Record.objects.order_by('-date')        #to add a for loop in html page to read all objects
   
    # code for pagination starts from there
    paginator=Paginator(record_obj,4)       #ye line bata rahi hai k kitna data lana hai 
    page_number=request.GET.get('page')    # ye line page number get kar rahi hai
    record_obj_final=paginator.get_page(page_number)
    totalpage1=record_obj_final.paginator.num_pages #this line is use to find the last page by finding total pages
    context={
      'record_obj':record_obj_final,
      'lastpage':totalpage1,
      'totalpagelist2':[n+1 for n in range(totalpage1)]
   }
    return render(request,'records_of_patient.html',context)


def ADD_Record(request):          #Add values in presscription 
   if request.method == 'POST':
        patient_Id=request.POST.get('patient_Id')
        patient_Name=request.POST.get('patient_Name')
        disease=request.POST.get('disease')
        city=request.POST.get('city')
        patient_Email=request.POST.get('patient_Email')
        date=request.POST.get('date')
        patient_Ph_No =request.POST.get('patient_Ph_No')

        record_obj=Patient_Record(
            patient_Id=patient_Id,  
            patient_Name=patient_Name,
            disease= disease,
            city=city,
            patient_Email=patient_Email,
            date=date,
            patient_Ph_No=patient_Ph_No,
        )
       
        record_obj.save()
        return redirect('Record_of_Patient')
   return render(request,'records_of_patient.html')



def Update_Precord(request, id):
    if request.method == 'POST':
       
        pI = request.POST.get('patient_Id')
        pN= request.POST.get('patient_Name')
        dis = request.POST.get('disease')
        d = request.POST.get('date')
        c = request.POST.get('city')
        e=request.POST.get('patient_Email')
        ph = request.POST.get('patient_Ph_No')

        pat_record = Patient_Record(
         id=id,
         patient_Id=pI,
         patient_Name = pN,
         disease = dis,
         city = c,
         patient_Email=e,
         date = d,
         patient_Ph_No=ph,
        )
        pat_record.save()
        print(pN)
        
        return redirect('Record_of_Patient')
    return render(request,'records_of_patient.html')


def Delete_Precord(request, id):    
    record_obj=Patient_Record.objects.filter(id=id).delete()
    
    # context={
    #     "record_obj":record_obj
    # }
    # Redirect to 'Patient Record' view
    return redirect('Record_of_Patient')




def search_record(request):
    if request.method == 'GET':
        search_id = request.GET.get('search')

        if search_id:
            try:
                record = get_object_or_404(Patient_Record, patient_Id=search_id)
                return render(request, 'search_record.html', {'record': record})
            except Patient_Record.DoesNotExist:
                return render(request, 'search_record.html', {'error_message': 'Record not found.'})

    return render(request, 'search_record.html')

def contact_With_patient(request):
    return render(request,'contact_patient.html')

def export_to_pdf_prescription(request):
    # Retrieve data from the database
    data = Doctors_Prescription.objects.all()  # Replace YourModel with your actual model name

    # Create a response object with PDF content type
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="doctor_prescription_data.pdf"'

    # Create a PDF object
    pdf = FPDF()

    # Add a page
    pdf.add_page()

    # Set font and size
    pdf.set_font("Arial", size=12)

    # Set table headers
    headers = ['Patient ID', 'Doctor ID', 'Patient Name', 'Doctor Name', 'Medicine Name', 'Medicine Dosage']
    pdf.cell(30, 10, headers[0], border=1)
    pdf.cell(30, 10, headers[1], border=1)
    pdf.cell(40, 10, headers[2], border=1)
    pdf.cell(40, 10, headers[3], border=1)
    pdf.cell(40, 10, headers[4], border=1)
    pdf.cell(40, 10, headers[5], border=1)
    pdf.ln()

    # Set table data
    for item in data:
        # Check if any field is empty
        if all([item.patient_Id, item.doctor_Id, item.patient_Name, item.doctor_Name, item.medicine_Name, item.medicine_Dossage]):
            pdf.cell(30, 10, str(item.patient_Id), border=1)
            pdf.cell(30, 10, str(item.doctor_Id), border=1)
            pdf.cell(40, 10, str(item.patient_Name), border=1)
            pdf.cell(40, 10, str(item.doctor_Name), border=1)
            pdf.cell(40, 10, str(item.medicine_Name), border=1)
            pdf.cell(40, 10, str(item.medicine_Dossage), border=1)
            pdf.ln()

    # Output the PDF content
    response.write(pdf.output(dest='S').encode('latin-1'))

    return response

def export_to_pdf_patient(request):
    # Retrieve data from the database
    data = Patient_Record.objects.all()  # Replace YourModel with your actual model name

    # Create a response object with PDF content type
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="patient_record_data.pdf"'

    # Create a PDF object
    pdf = FPDF()

    # Add a page
    pdf.add_page()

    # Set font and size
    pdf.set_font("Arial", size=12)

    # Set table headers
    pdf.cell(30, 10, 'Patient ID', border=1)
    pdf.cell(40, 10, 'Patient Name', border=1)
    pdf.cell(40, 10, 'Disease', border=1)
    pdf.cell(30, 10, 'Patient Age', border=1)
    pdf.cell(30, 10, 'Date', border=1)
    pdf.ln()

    # Set table data
    for item in data:
        # Check if any field is empty
        if all([item.patient_Id, item.patient_Name, item.disease, item.patient_Age, item.date]):
            pdf.cell(30, 10, str(item.patient_Id), border=1)
            pdf.cell(40, 10, str(item.patient_Name), border=1)
            pdf.cell(40, 10, str(item.disease), border=1)
            pdf.cell(30, 10, str(item.patient_Age), border=1)
            pdf.cell(30, 10, str(item.date), border=1)
            pdf.ln()

    # Output the PDF content
    response.write(pdf.output(dest='S').encode('latin-1'))

    return response

def Contact_Patient(request):
    return render(request,'contact_patient.html')

def search_record_for_contact(request):
    if request.method == 'GET':
        search_id = request.GET.get('search')
        if search_id:
            try:
                record = get_object_or_404(Patient_Record, patient_Id=search_id)
                context={'record': record }

                return render(request, 'search_patient_for_contact.html',context )
            except Patient_Record.DoesNotExist:
                return render(request, 'search_patient_for_contact.html', {'error_message': 'Record not found.'})
            

def search_record_for_contact2(request):
    if request.method == 'POST':
                form=ContactForm(request.POST)
                if form.is_valid():

                    name=form.cleaned_data['name']
                    title=form.cleaned_data['title']
                    email=form.cleaned_data['email']
                    content=form.cleaned_data['content']

                    html = render_to_string('contact/email/contactform.html',{
                        'name':name,
                        'title':title,
                        'email':email,
                        'content':content
                    })
                    print("The form was valid ")

                    send_mail('The contact from Subject', 'This is the Message','lalaarukhhh@gmail.com',['aamnazahid151@gmail.com'],html_message=html)

                    return redirect('contact_patient_by_search2')
                
                
    else:
                form=ContactForm()

    return render(request, 'search_and_email.html',{'form':form} )
   
    



def doc_login(request):

    return render(request , 'doc_login.html')


def signup(request):
    if request.method == 'POST':
        # Retrieve form data
        name = request.POST['name']
        phone_number = request.POST['phone_number']
        specialization = request.POST['specialization']
        country = request.POST['country']
        email = request.POST['email']
        license_number = request.POST['license_number']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        # Create a new user
        user = CustomUser.objects.create_user(username=username, password=password1)
        
        # Set additional fields
        user.name = name
        user.phone_number = phone_number
        user.specialization = specialization
        user.country = country
        user.email = email
        user.license_number = license_number
        
        # Save the user object
        user.save()
        
        # Authenticate and login the user
        user = authenticate(username=username, password=password1)
        if user is not None:
            login(request, user)
            
            # Set cookies
            response = HttpResponse("Signup successful!")
            response.set_cookie('username', username)
            response.set_cookie('email', email)
            
            return response

    return render(request, 'signup.html')

