# Hosptital-Management-System

Hospital Management System and Web App.
This is a hospital management system and web application that allows patients to book available slots in the hospital through an online portal. The system provides a convenient way for patients to schedule appointments with various doctors and manage their medical information.

Features
The hospital management system and web app offer the following features:

1.User Authentication:
Patients can log in using their Google accounts.
Staff members can log in and log out using the built-in Django login and logout system.

2.User Profiles:
Each user has a profile containing personal details such as name, gender, and email.
Patients can view their medical history, including illness records and prescriptions.
Users can update their profile information.

3.Appointment Booking:
Patients can book available slots for different types of doctors, including ENT, Cardiologist, Neurologist, Oncologist, Ortho, etc.
The system allows patients to write down complaints and problems while seeking an appointment.

4.Accounts Section:
Patients can view their bills and the status of each bill, such as paid or pending.

5.Staff-Patient Communication:
Staff members can chat with patients using a messaging system.
The chat system displays the number of unread messages for each chat.
Real-time updates are implemented to retrieve new messages without refreshing the page.

6.Profile Search:
Users can search for other people's profiles by their names.
Fuzzy search functionality is implemented for flexible and accurate search results.

7.Django-tables Integration:
Staff members have access to a table view for viewing profiles and other relevant data.
Django-tables library is utilized to display data in a tabular format.

8.Additional Features:
Websockets are implemented to facilitate real-time updates in the chat system.
Signals are used for sending emails when necessary, such as appointment reminders.
The web application can be hosted on PythonAnywhere or a similar hosting service.

Installation
To set up the hospital management system and web app locally, follow these steps:

Clone the repository from <https://github.com/xFBIx/Hosptital-Management-System.git>.
Install the required dependencies by running pip install -r requirements.txt.
Run the application using the command python manage.py runserver.
Access the web app through your browser at <http://localhost:8000> or the appropriate URL.
