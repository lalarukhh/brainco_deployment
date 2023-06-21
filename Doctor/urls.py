from django.contrib import admin

# Create your views here.
from django.urls import path
from django.urls import path
from Doctor.views import export_to_pdf_patient, export_to_pdf_prescription
from MyProject import settings
#now import the views.py file into this code
from . import views
urlpatterns=[
     path('admin/', admin.site.urls),
     path('home',views.Home,name="Homepage"),

     path('home/prescription/',views.INDEX,name="main_prescription"),
     path('prescription/',views.INDEX,name="main_prescription"),
     path('addprescription/',views.ADD,name="addprescription"),
     path('editprescription',views.Edit,name="editprescription"),
     path('updateprescription/<int:id>',views.Update,name="updateprescription"),
     path('deleteperscription/<int:id>',views.Delete,name="deleteperscription"),

     path('patientrecord/',views.Record_fun,name="Record_of_Patient"),
     path('addrecord',views.ADD_Record,name="addrecord"),
     path('updateprecord/<int:id>',views.Update_Precord,name="updateprecord"),
     path('deletepatient/<int:id>',views.Delete_Precord,name="deletepatient"),
     path('search', views.search_record, name='search_record'),

     path('contact_patient',views.contact_With_patient,name='contact_patient'),
     path('export_pres/', export_to_pdf_prescription, name='export_to_pdf_prescription'),
     path('export_patient_record/', export_to_pdf_patient, name='export_to_pdf_patient'),

     path('contact_patient_search/',views.Contact_Patient,name="contact_patient_search"),
     path('contact_patient_by_search/',views.search_record_for_contact,name="contact_patient_by_search"),
     path('contact_patient_by_search2/',views.search_record_for_contact2,name="contact_patient_by_search2"),


     path('doc_login' , views.doc_login , name='doc_login'),
      path('signup/', views.signup, name='signup'),
     
   

]

