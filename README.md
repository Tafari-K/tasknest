# TaskNest

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
![Review Page Wireframe](static/wireframes/review-page.png)

- ERD (Data Model)

## Data Model (ERD)

The following diagram shows the relationships between the main entities in TaskNest.

![Entity Relationship Diagram](static/planning/tasknest-diagram.png)




## Features

TaskNest is designed to connect customers with skilled tradesmen for quick and reliable service bookings.  
Below are the main features planned for development, separated into **MVP (Minimum Viable Product)** and **Stretch Goals**.

---

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

## Known ISsuesn& Fixes
| **Issue** | **Cause** | **Fix** | **Status** | **Commit Message** |
|-----------|-----------|---------|------------|---------------------|
| `TemplateDoesNotExist: core/home.html` | Django couldn’t locate the template due to folder structure and missing template path in `settings.py` | Verified template location, added `core/templates` to `DIRS`, confirmed `INSTALLED_APPS` and `APP_DIRS` | Fixed | `fix: resolve template loading issue by correcting settings and folder structure` |

## Testing
*(To be added later)*

## Deployment
*(To be added later)*

## Credits
*(To be added later)*
