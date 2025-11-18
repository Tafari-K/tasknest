# TaskNest
## Contents
- [Project Overview](#project-overview)
- [User Stories](#user-stories)
- [Planning](#planning)
- [Wireframes](#wireframes)
- [Data Model (ERD)](#data-model-erd)
- [Project Development Board](#project-development-board)
- [Features](#features)
- [Summary](#summary)

## Project Overview
TaskNest is a full-stack web platform that connects customers with local tradesmen. 
Customers can book services, leave reviews, and find trusted professionals. 
Tradesmen can create profiles showcasing their skills and qualifications.

## User Stories
*(Add your user stories here)*

## Planning
- Wireframes
## Wireframes

Below are the initial wireframes created for TaskNest.

### Home Page
![Home Page Wireframe](static/wireframes/home-page.png)

### Tradesman Profile Page
![Profile Page Wireframe](static/wireframes/tradesman-profile.png)

### Booking Page
![Booking Page Wireframe](static/wireframes/bookings-page.png)

### Login and Register Page
![Login and Register Page Wireframe](static/wireframes/login-register-page.png)

### Dashboard Page
![Dashboard Page Wireframe](static/wireframes/dashboard.png)

### Ad Listing Page
![Ad Listing Page Wireframe](static/wireframes/ad-listings-page.png)

### Review Page
![Review Page Wireframe](/static/wireframes/review-page.png)

- ERD (Data Model)

## Data Model (ERD)

The following diagram shows the relationships between the main entities in TaskNest.

![Entity Relationship Diagram](/staticfiles/planning/tasknest_ERD.png)

## Project Development Board

You can track the ongoing development, tasks, and progress for **TaskNest** on the official GitHub Project Board below:

[View TaskNest Project Board](https://github.com/<your-username>/<your-repo>/projects)

The board outlines all current tasks, upcoming features, and completed milestones.


## Features

TaskNest is designed to connect customers with skilled tradesmen for quick and reliable service bookings.  
Below are the main features planned for development, separated into **MVP (Minimum Viable Product)** and **Stretch Goals**.

## Features

- User authentication (register, login, logout)
- Tradesmen can create jobs and manage listings
- Customers can create job ads and leave feedback
- Responsive design using Bootstrap
- **Database:** SQLite (chosen for MVP simplicity and Django integration)

### preset profiles
Below are details of the preset profiles created for testing and demonstration purposes:
Username: james_sparks | Password: TestPass123!
Username: sarah_fixes | Password: TestPass123!
Username: mike_carpenter | Password: TestPass123!

Customers:

Username: emma_wilson | Password: TestPass123!
Username: david_brown | Password: TestPass123!
Username: lisa_jones | Password: TestPass123!

### Minimum Viable Product (MVP)

| **Feature** | **Description** | **User Type** |
|--------------|-----------------|----------------|
| **User Authentication** | Users can register, log in, and log out securely using Django’s built-in auth system. | All Users |
| **Profile Management** | Tradesmen can create and edit their profiles, including their skills, qualifications, and location. | Tradesmen |
| **Service Listings** | Tradesmen can create, update, and delete job/service advertisements. | Tradesmen |
| **Booking System** | Customers can view listings and book tradesmen directly. | Customers |
| **Review and Rating System** | Customers can leave feedback and ratings on completed jobs. | Customers |
| **Admin Dashboard** | Admin can manage users, listings, and reviews through Django’s admin panel. | Administrator |
| **Responsive Design** | The site is mobile-friendly and works across different screen sizes. | All Users |

---

### Stretch Goals (Future Enhancements)

| **Feature** | **Description** | **User Type** |
|--------------|-----------------|----------------|
| **Dashboard View** | Users can view all their active bookings, jobs, and reviews in one place. | All Users |
| **Messaging System** | Allow customers and tradesmen to communicate directly through private messages. | All Users |
| **Search and Filter Options** | Search for tradesmen by skill, price, or location. | Customers |
| **Profile Badges** | Highlight top-rated tradesmen with achievement badges. | Tradesmen |
| **Booking Notifications** | Email or in-site notifications when a booking is confirmed or reviewed. | All Users |

---

### Summary

The MVP focuses on delivering a functional platform where customers can:
- Browse available tradesmen  
- Book jobs easily  
- Leave verified reviews  

Tradesmen can:
- Advertise their services  
- Manage bookings and reviews  

Future development will focus on improving communication, personalisation, and user experience.


## Technologies Used
- Python (Django)
- HTML, CSS
- PostgreSQL
- GitHub, Heroku

## Known Issues & Fixes
| **Issue** | **Cause** | **Fix** | **Status** | **Commit Message** / Outcome|
|-----------|-----------|---------|------------|---------------------|
| `TemplateDoesNotExist: core/home.html` | Django couldn’t locate the template due to folder structure and missing template path in `settings.py` | Verified template location, added `core/templates` to `DIRS`, confirmed `INSTALLED_APPS` and `APP_DIRS` | Fixed | Fix: template loading issue, correct folder sturcture |
| CSS not loading (`404` on `home.css`) | Incorrect file name in template (`home.css` instead of `style.css`) | Updated `{% static %}` path to match actual file name | Fixed | Fix: update static link to style.css |
|PostgreSQL connection failure during database setup. Django could not establish a connection due to “System Error 1067: The process terminated unexpectedly.”| PostgreSQL service could not start due to Windows permission conflicts in the Program Files directory and uninitialized data folder.| Switched the project database from PostgreSQL to SQLite by updating settings.py to use Django’s built-in sqlite3 engine. This ensured smooth local development with no external dependencies.| Resolved — Database running successfully using SQLite. All migrations applied and server running as expected.|Fix: replace PostgreSQL config with SQLite setup|
| Page rendering blank despite correct template path | incorrect import syntax: from django.shortcuts import render was mistyped as 'from django.shortcuts import import render' |  Corrected the import statement in views.py to properly load the render function | fixed | Fix: amend render request|
| Page not rendering after logic for signup | corrected statement| fixed| refactor: update class, update appropriate py files|
| django.db.utils.OperationalError: no such column: main_profile.location | Model field (location) was added to the Profile model after the initial migrations | Created and applied new migration to add the location field to the Profile table | Fixed |fix: resolved profile model migration issue and implemented dashboard view |
| Dashboard page not rendering after login | The dashboard.html template wasn’t located in the correct folder or Django couldn’t find it | Ensured TEMPLATES['DIRS'] points to the correct path and the template exists | fixed | |
| Styling not displaying| CSS/Bootstrap not yet linked to the templates | Deferred Bootstrap integration to later phase for consistent project structure | Deferred | |
|Profile not updating after form submission | Missing instance=profile in form save logic | Added instance binding to form in view | Fixed | feat: implemented profile editing feature with user validation |
| Users could access edit page without login | Missing @login_required decorator | Added login protection to edit_profile view | Fixed | feat: finish authentication system, update login logic, update appropriate templates and files |
| Add/Remove Job pages initially not rendering | Missing templates and URL routes | Created add_job.html and updated URLs in main/urls.py | Fixed | feat: implemented add/remove job functionality |
| Profile section missing details on dashbaord | Profile model fields not displaced in dashboard template | Added avatar, username, role, location, skills, and job stats display | Fixed  | Added profile info section with avatar, role, and job stats to dashboard; verified dashboard renders correctly |
| Needed realistic test data for development and testing | Empty database made it difficult to test CRUD functionality and user dashboards | Created Django management command `seed_profiles` to populate database with 3 tradesman and 3 customer profiles with realistic data | Fixed | feat: add seed_profiles management command for test data |
| Missing URL routes for add_job, remove_job, and add_review | Template references didn't match URL patterns | Added URL aliases and placeholder view for review functionality | Fixed | feat: add seed_profiles management command for test data |
| No logout functionality visible to users | Logout route existed but no UI button in navigation | Added logout button to navbar with authentication check, updated logout redirect to home page | Fixed | feat: add logout button and active jobs preview page |
| Jobs page had minimal information display | Basic list view didn't show enough job details for users to make decisions | Redesigned jobs page with card layout, status badges, poster info, location, and interactive elements | Fixed | feat: add logout button and active jobs preview page |
| The jobs model was not showing in Django admin, even though it existed in the project. Attempted migrations showed "no changes detected". | There were two separate Django apps in the project core and main. Some model/admin files were accidentally left in core, while the actual logic used main. || Fixed | Verified that all important models, views, and admin registrations were in main. Removed the unused core app folder. Cleaned up INSTALLED_APPS in settings.py. Restarted the server and confirmed Jobs, Profiles, and Reviews now appear in Django admin.| 
|Images uploaded through Django admin were not displaying on the jobs page. A 404 error appeared when accessing image URLs. | MEDIA_ROOT and media URL routing were not properly configured. Images were uploaded via admin, but not served correctly due to missing URL patterns and folders.| |fixed | - Configured `MEDIA_ROOT` and `MEDIA_URL` in `settings.py`. Updated `urls.py` to serve media files during development using `static()`. Ensured `media/job_images/` directory exists and images are uploaded there.Re-uploaded images via Django admin. | Logout returned 405 error | Django’s `LogoutView` only allows POST requests, but navbar link used GET. | Replaced `<a>` link with a secure POST form including CSRF token. | ✅ Fixed | **Commit:** `fix: resolved logout 405 error and improved dashboard grid layout responsiveness`<br>Outcome: Logout now functions correctly and securely. |
| Avatar section stretched layout | Sidebar lacked width constraints and proper alignment on different screen sizes. | Wrapped avatar area in `.avatar-section`, added flexbox layout, centered elements, and improved styling for file input and upload button. | ✅ Fixed | Outcome: Avatar section now consistent and visually balanced across devices. |
| Job thumbnails misaligned on mobile | Dashboard cards didn’t have a defined grid structure, causing overlap or poor spacing. | Implemented `.thumb-grid` using `grid-template-columns` and added responsive media queries for mobile/tablet screens. | ✅ Fixed | Outcome: Dashboard layout now responsive, with properly aligned job cards. |




## Testing
*(To be added later)*

## Deployment
in order to deploy this project to Heroku, the following steps were taken:
1. Created a `Procfile` and .python-version in the root directory with the following content:
   ```
   web: gunicorn tasknest_project.wsgi
   ```
   ```
    3.12
    ```
2. Added `gunicorn` , `whitenoise` and 'dj-database-url' to `requirements.txt`
   ```
3. git bash heroku ps:scale web=1
   ```
4. heroku run python manage.py migrate

5. create heroku app

the site can be found on heroku via the following link:
https://tasknest-eu-1d1de4a401f0.herokuapp.com/

## Project Development Board
project board link:
https://github.com/users/Tafari-K/projects/6/views/1
## Credits
### images
Tasknest hero image
https://www.freepik.com/free-photo/full-shot-people-working-as-engineers_41695771.htm#fromView=search&page=1&position=39&uuid=bee739a0-7d39-473c-979f-439ff39629d8&query=tradesman+and+woman
