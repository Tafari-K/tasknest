"""
Django management command to seed the database with test profiles.
Usage: python manage.py seed_profiles
"""
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from main.models import Profile, Job


class Command(BaseCommand):
    help = 'Seeds the database with 3 tradesman and 3 customer profiles'

    def handle(self, *args, **kwargs):
        self.stdout.write('Starting database seeding...')

        # ===== TRADESMAN PROFILES =====
        tradesmen_data = [
            {
                'username': 'james_sparks',
                'email': 'james@sparkelectrical.co.uk',
                'password': 'TestPass123!',
                'first_name': 'James',
                'last_name': 'Sparks',
                'title': 'Mr',
                'current_occupation': 'Electrician',
                'location': 'Manchester, Greater Manchester',
                'skills': 'Electrical installations, Rewiring, Fault finding, Consumer unit upgrades, EV charger installation, PAT testing',
                'qualification': 'City & Guilds 2365 Level 3, 18th Edition Wiring Regulations, Part P Certified',
                'jobs_completed': 47
            },
            {
                'username': 'sarah_fixes',
                'email': 'sarah@fixitplumbing.co.uk',
                'password': 'TestPass123!',
                'first_name': 'Sarah',
                'last_name': 'Thompson',
                'title': 'Ms',
                'current_occupation': 'Plumber',
                'location': 'Birmingham, West Midlands',
                'skills': 'Boiler installation and repair, Bathroom fitting, Leak repairs, Drain unblocking, Central heating, Gas safety checks',
                'qualification': 'NVQ Level 3 Plumbing, Gas Safe Registered (Gas Safe No: 123456), Water Regulations Approved',
                'jobs_completed': 63
            },
            {
                'username': 'mike_carpenter',
                'email': 'mike@woodworkspro.co.uk',
                'password': 'TestPass123!',
                'first_name': 'Michael',
                'last_name': 'Carpenter',
                'title': 'Mr',
                'current_occupation': 'Carpenter & Joiner',
                'location': 'Leeds, West Yorkshire',
                'skills': 'Kitchen fitting, Custom furniture, Door hanging, Decking, Skirting and architrave, Built-in wardrobes, Flooring',
                'qualification': 'City & Guilds Level 3 Carpentry & Joinery, CSCS Card Holder, 15 years experience',
                'jobs_completed': 89
            }
        ]

        # ===== CUSTOMER PROFILES =====
        customers_data = [
            {
                'username': 'emma_wilson',
                'email': 'emma.wilson@email.com',
                'password': 'TestPass123!',
                'first_name': 'Emma',
                'last_name': 'Wilson',
                'title': 'Mrs',
                'current_occupation': 'Teacher',
                'location': 'London, Greater London',
            },
            {
                'username': 'david_brown',
                'email': 'david.brown@email.com',
                'password': 'TestPass123!',
                'first_name': 'David',
                'last_name': 'Brown',
                'title': 'Mr',
                'current_occupation': 'Software Developer',
                'location': 'Bristol, South West England',
            },
            {
                'username': 'lisa_jones',
                'email': 'lisa.jones@email.com',
                'password': 'TestPass123!',
                'first_name': 'Lisa',
                'last_name': 'Jones',
                'title': 'Ms',
                'current_occupation': 'Marketing Manager',
                'location': 'Liverpool, Merseyside',
            }
        ]

        # Create Tradesmen
        self.stdout.write(self.style.WARNING('Creating tradesman profiles...'))
        for data in tradesmen_data:
            user, created = User.objects.get_or_create(
                username=data['username'],
                defaults={
                    'email': data['email'],
                    'first_name': data['first_name'],
                    'last_name': data['last_name']
                }
            )
            if created:
                user.set_password(data['password'])
                user.save()
                self.stdout.write(self.style.SUCCESS(f'✓ Created user: {user.username}'))
            else:
                self.stdout.write(self.style.WARNING(f'○ User already exists: {user.username}'))

            profile, created = Profile.objects.get_or_create(
                user=user,
                defaults={
                    'title': data['title'],
                    'role': 'tradesman',
                    'current_occupation': data['current_occupation'],
                    'location': data['location'],
                    'skills': data['skills'],
                    'qualification': data['qualification'],
                    'jobs_completed': data['jobs_completed']
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'✓ Created tradesman profile: {profile}'))
            else:
                self.stdout.write(self.style.WARNING(f'○ Profile already exists: {profile}'))

        # Create Customers
        self.stdout.write(self.style.WARNING('\nCreating customer profiles...'))
        for data in customers_data:
            user, created = User.objects.get_or_create(
                username=data['username'],
                defaults={
                    'email': data['email'],
                    'first_name': data['first_name'],
                    'last_name': data['last_name']
                }
            )
            if created:
                user.set_password(data['password'])
                user.save()
                self.stdout.write(self.style.SUCCESS(f'✓ Created user: {user.username}'))
            else:
                self.stdout.write(self.style.WARNING(f'○ User already exists: {user.username}'))

            profile, created = Profile.objects.get_or_create(
                user=user,
                defaults={
                    'title': data['title'],
                    'role': 'customer',
                    'current_occupation': data['current_occupation'],
                    'location': data['location']
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'✓ Created customer profile: {profile}'))
            else:
                self.stdout.write(self.style.WARNING(f'○ Profile already exists: {profile}'))

        # Create sample jobs for customers
        self.stdout.write(self.style.WARNING('\nCreating sample jobs...'))
        sample_jobs = [
            {
                'profile': Profile.objects.get(user__username='emma_wilson'),
                'title': 'Kitchen Socket Installation',
                'description': 'Need 3 additional power sockets installed in kitchen for new appliances. Property is in Zone 2 postcode.',
                'is_completed': False
            },
            {
                'profile': Profile.objects.get(user__username='david_brown'),
                'title': 'Leaking Bathroom Tap Repair',
                'description': 'Bathroom sink tap has been dripping for a week. Needs urgent repair or replacement.',
                'is_completed': False
            },
            {
                'profile': Profile.objects.get(user__username='lisa_jones'),
                'title': 'Garden Decking Construction',
                'description': 'Looking for carpenter to build 4m x 3m decking area in back garden. Materials already purchased.',
                'is_completed': False
            }
        ]

        for job_data in sample_jobs:
            job, created = Job.objects.get_or_create(
                profile=job_data['profile'],
                title=job_data['title'],
                defaults={
                    'description': job_data['description'],
                    'is_completed': job_data['is_completed']
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'✓ Created job: {job.title}'))
            else:
                self.stdout.write(self.style.WARNING(f'○ Job already exists: {job.title}'))

        self.stdout.write(self.style.SUCCESS('\n=== Database seeding completed! ==='))
        self.stdout.write('\nYou can now log in with any of these accounts:')
        self.stdout.write(self.style.SUCCESS('\nTRADESMEN:'))
        self.stdout.write('  james_sparks / TestPass123!')
        self.stdout.write('  sarah_fixes / TestPass123!')
        self.stdout.write('  mike_carpenter / TestPass123!')
        self.stdout.write(self.style.SUCCESS('\nCUSTOMERS:'))
        self.stdout.write('  emma_wilson / TestPass123!')
        self.stdout.write('  david_brown / TestPass123!')
        self.stdout.write('  lisa_jones / TestPass123!')