from django.contrib import admin
from booking_app.models import  Booking
from django.contrib.auth.models import User, Group
import csv
from django.http import HttpResponse

class TicketDisplay(admin.ModelAdmin):
    list_display = (
        'user',
        'source' ,
        'destination',
        'flight_name'
    )

    actions = ['generate_csv_report']
    
    def generate_csv_report(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="booking_report.csv"'
        
        writer = csv.writer(response)
        writer.writerow(['id','user', 'source','destination', 'flight_name'])
        
        for student in queryset:
            writer.writerow([f'BK-00{student.id}', student.user, student.source, student.destination, student.flight_name])  # Replace with your model fields
        
        return response

    generate_csv_report.short_description = "Generate CSV Report"

admin.site.register(Booking, TicketDisplay)
