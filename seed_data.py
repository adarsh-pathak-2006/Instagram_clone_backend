import os
import django
from django.core.files.uploadedfile import SimpleUploadedFile

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'clone.settings')
django.setup()

from django.contrib.auth.models import User
from authentication.models import Profile
from posts.models import Post

def seed():
    print("Creating users...")
    user1, _ = User.objects.get_or_create(username='alice', email='alice@example.com', first_name='Alice', last_name='Wonderland')
    if not user1.has_usable_password():
        user1.set_password('password123')
        user1.save()
        
    user2, _ = User.objects.get_or_create(username='bob', email='bob@example.com', first_name='Bob', last_name='Builder')
    if not user2.has_usable_password():
        user2.set_password('password123')
        user2.save()

    print("Fetching profiles...")
    profile1, _ = Profile.objects.get_or_create(user=user1)
    profile1.name = 'Alice'
    profile1.bio = 'Hello! I am Alice.'
    profile1.save()

    profile2, _ = Profile.objects.get_or_create(user=user2)
    profile2.name = 'Bob'
    profile2.bio = 'Can we build it? Yes we can!'
    profile2.save()
    
    print("Setting up follows...")
    # Alice follows Bob
    profile1.followers.add(profile2)
    profile1.save()

    print("Creating posts...")
    # Need to handle FileField nicely. We will just leave it empty or create a fake one if needed.
    # The frontend uses an image if available. Let's create dummy attachments.
    if not Post.objects.filter(title="Alice's first post").exists():
        Post.objects.create(
            user=profile1,
            title="Alice's first post",
            description="Welcome to my new Instagram clone account!"
        )
        
    if not Post.objects.filter(title="Bob's amazing build").exists():
        Post.objects.create(
            user=profile2,
            title="Bob's amazing build",
            description="Just finished a huge project today."
        )

    print("Seed complete! You can log in with username: 'alice' and password: 'password123'.")

if __name__ == '__main__':
    seed()
