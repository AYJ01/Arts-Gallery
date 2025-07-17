from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from datetime import datetime
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.filter(username=username).exists()
        if user:
            user = User.objects.get(username=username)
            if user.check_password(password):
                request.session['uid'] = user.id
                if user.usertype == 'Customer':
                    return redirect('/userhome')
                elif user.usertype == 'Gallery':
                    return redirect('/galleryhome')
                elif user.usertype == 'Artist':
                    return redirect('/artisthome')
                elif user.is_superuser:
                    return redirect('/adminhome')
                else:
                    return render(request, 'login.html', {'error': 'Invalid credentials'})
            else:
                return render(request, 'login.html', {'error': 'Invalid password'})
            
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def userregister(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        phone = request.POST['contact']
        address = request.POST['address']
        email = request.POST['email']
        bio = request.POST['bio']
        image = request.FILES['image']
        check=User.objects.filter(username=username).exists()
        if check:
            return render(request, 'userregister.html', {'error': 'Username already exists'})
        else:
            user = User.objects.create_user(username=email, password=password, usertype='Customer')
            user_tbl = User_tbl(user=user, username=username, phone=phone, address=address, email=email, bio=bio, image=image)
            user_tbl.save()
            return render(request, 'userregister.html', {'success': 'Registration successful! Please login.'})
    return render(request, 'userregister.html')

def artistregister(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        phone = request.POST['contact']
        address = request.POST['address']
        email = request.POST['email']
        bio = request.POST['bio']
        image = request.FILES['image']
        check=User.objects.filter(username=username).exists()
        if check:
            return render(request, 'artistregister.html', {'error': 'Username already exists'})
        else:
            user = User.objects.create_user(username=email, password=password, usertype='Artist')
            user_tbl = Artist_tbl(user=user, username=username, phone=phone, address=address, email=email, bio=bio, image=image)
            user_tbl.save()
            return render(request, 'artistregister.html', {'success': 'Registration successful! Please login.'})
    return render(request, 'artistregister.html')

def galleryregister(request):
    if request.POST:
        username = request.POST.get("username")
        ownername = request.POST.get("ownername")
        managername = request.POST.get("managername")
        typeofgallery = request.POST.get("typeofgallery")
        contact = request.POST.get("contact")
        email = request.POST.get("email")
        image = request.FILES.get("image")
        ldate = request.POST.get("ldate")
        address = request.POST.get("address")
        bio = request.POST.get("bio")
        password = request.POST.get("password") 
        check = User.objects.filter(username=username).exists()
        if check:
            return render(request, 'galleryregister.html', {'error': 'Username already exists'})
        else:
            user = User.objects.create_user(username=email, password=password, usertype='Gallery')
            user.save()
            user_tbl = Gallery_tbl(user=user, galleryname=username, owner=ownername, manager=managername, gallery_type=typeofgallery, phone=contact, email=email, image=image, launch_date=ldate, address=address, bio=bio)
            user_tbl.save()
            return render(request, 'galleryregister.html', {'success': 'Registration successful! Please login.'})
    return render(request, 'galleryregister.html')

def userhome(request):
    user=User_tbl.objects.get(user_id=request.session['uid'])
    if request.POST:
        username = request.POST['username']
        phone = request.POST['contact']
        address = request.POST['address']
        email = request.POST['email']
        bio = request.POST['bio']
        image = request.FILES['image']
        user.username = username
        user.phone = phone
        user.address = address
        user.email = email
        user.bio = bio
        user.image = image
        user.user.username = email
        user.user.email = email
        user.user.save()
        user.save()
        return render(request, 'userhome.html', {'user': user, 'success': 'Profile updated successfully!'})
    return render(request, 'userhome.html',{'user':user})

def adminhome(request):
    return render(request, 'adminhome.html')

def artisthome(request):
    user=Artist_tbl.objects.get(user_id=request.session['uid'])
    if request.POST:
        username = request.POST['username']
        phone = request.POST['contact']
        address = request.POST['address']
        email = request.POST['email']
        bio = request.POST['bio']
        image = request.FILES['image']
        user.username = username
        user.phone = phone
        user.address = address
        user.email = email
        user.bio = bio
        user.image = image
        user.user.username = email
        user.user.email = email
        user.user.save()
        user.save()
        return render(request, 'artisthome.html', {'user': user, 'success': 'Profile updated successfully!'})
    return render(request, 'artisthome.html',{'user':user})

def galleryhome(request):
    user=Gallery_tbl.objects.get(user_id=request.session['uid'])
    if request.POST:
        galleryname = request.POST['galleryname']
        ownername = request.POST['owner']
        managername = request.POST['manager']
        typeofgallery = request.POST['gallery_type']
        contact = request.POST['phone']
        email = request.POST['email']
        image = request.FILES['image']
        ldate = request.POST['launch_date']
        address = request.POST['address']
        bio = request.POST['bio']
        user.galleryname = galleryname
        user.owner = ownername
        user.manager = managername
        user.gallery_type = typeofgallery
        user.phone = contact
        user.email = email
        user.image = image
        user.launch_date = ldate
        user.address = address
        user.bio = bio
        user.user.username = email
        user.user.email = email
        user.user.save()
        user.save()
        return render(request, 'galleryhome.html', {'user': user, 'success': 'Profile updated successfully!'})
    return render(request, 'galleryhome.html',{'user':user})

def artistpost(request):
    user=Artist_tbl.objects.get(user_id=request.session['uid'])
    posts = Post.objects.filter(user=user)
    likes= Likes.objects.filter(post__user=user)
    comments = Comments.objects.filter(post__user=user)
    if request.POST:
        description = request.POST['description']
        image = request.FILES['image']
        post = Post.objects.create(user=user, image=image, description=description)
        post.save()
        return render(request, 'artistpost.html', {'user': user, 'success': 'Post created successfully!', 'posts': posts})
    return render(request, 'artistpost.html',{'user':user, 'posts': posts})

def deletepost(request):
    post = Post.objects.get(id=request.GET['id'])
    post.delete()
    return redirect('/artistpost')

def postlikes(request):
    post = Post.objects.get(id=request.GET['id'])
    likes = Likes.objects.filter(post=post)
    return render(request, 'postlikes.html', {'post': post,'likes':likes, 'success': 'Post liked successfully!'})

def userpost(request):
    try:
        msg = request.GET['msg']
    except:
        msg = ''
    user=User_tbl.objects.get(user_id=request.session['uid'])
    posts = Post.objects.all().order_by('-id')
    return render(request, 'userpost.html',{'user':user, 'posts': posts, 'msg': msg})

def togglelike(request):
    post = Post.objects.get(id=request.GET['id'])
    user = User_tbl.objects.get(user_id=request.session['uid'])
    like = Likes.objects.filter(post=post, user=user).first()
    msg=''
    if like:
        like.delete()
        msg='Unliked'
    else:
        like = Likes.objects.create(post=post, user=user)
        like.save()
        msg='Liked'
    return redirect(f'/userpost?msg={msg}')

def usercomments(request):
    user=User_tbl.objects.get(user_id=request.session['uid'])
    post = Post.objects.get(id=request.GET['id'])
    comments = Comments.objects.filter(post=post)
    if request.POST:
        comment = request.POST['comment']
        comments = Comments.objects.create(post=post, user=user, comment=comment)
        comments.save()
        return redirect(f'/usercomments?id={post.id}')
    return render(request, 'usercomments.html',{'user':user, 'post': post,'comments': comments})

def deletecomment(request):
    comment = Comments.objects.get(id=request.GET['id'])
    comment.delete()
    return redirect(f'/usercomments?id={comment.post.id}')

def usersliked(request):
    user = User_tbl.objects.get(user_id=request.session['uid'])
    posts = Post.objects.all()
    likes = Likes.objects.filter(user=user)
    return render(request, 'usersliked.html', {'user': user, 'posts': posts, 'liked': likes})

def userbid(request):
    user = User_tbl.objects.get(user_id=request.session['uid'])
    posts = Post.objects.get(id = request.GET['id'])
    bids = Auction.objects.filter(post=posts)
    if request.POST:
        bid = request.POST['bid']
        auction = Auction.objects.create(post=posts, user=user, bid_amount=bid)
        auction.save()
        return redirect(f'/userbid?id={posts.id}')
    return render(request, 'userbid.html', {'user': user, 'post': posts, 'bids': bids})

def artistbid(request):
    user = Artist_tbl.objects.get(user_id=request.session['uid'])
    posts = Post.objects.get(id = request.GET['id'])
    bids = Auction.objects.filter(post=posts)
    if request.POST:
        bid = request.POST['bid']
        posts.start_amount = bid
        posts.save()
        return redirect(f'/artistbid?id={posts.id}')
    return render(request, 'artistbid.html', {'user': user, 'post': posts, 'bids': bids})

def deletebid(request):
    user = User.objects.get(id=request.session['uid'])
    bid = Auction.objects.get(id=request.GET['id'])
    bid.delete()
    if user.usertype == 'Customer':
        return redirect(f'/userbid?id={bid.post.id}')
    elif user.usertype == 'Artist':
        return redirect(f'/artistbid?id={bid.post.id}')
    
def artistbidapprove(request):
    auction = Auction.objects.get(id=request.GET['id'])
    auction.post.status = 'accepted'
    auction.post.sold_to = auction.user
    auction.post.sold_date = auction.bid_date
    auction.post.price = auction.bid_amount
    auction.post.save()
    auction.status = 'accepted'
    auction.save()
    return redirect(f'/artistbid?id={auction.post.id}')

def payment(request):
    user = User_tbl.objects.get(user_id=request.session['uid'])
    posts = Post.objects.get(id = request.GET['id'])
    if request.POST:
        posts.status = 'sold'
        posts.save()
        return redirect(f'/usersliked?id={posts.id}')
    return render(request, 'payment.html', {'user': user, 'post': posts})

def userorders(request):
    user = User_tbl.objects.get(user_id=request.session['uid'])
    posts = Post.objects.filter(sold_to=user).order_by('-id')
    return render(request, 'userorders.html', {'user': user, 'posts': posts})

def artistvlogs(request):
    user = Artist_tbl.objects.get(user_id=request.session['uid'])
    vlogs = Vlogs.objects.filter(user=user)
    if request.POST:
        title= request.POST['title']
        description = request.POST['description']
        video = request.FILES['image']
        vlog = Vlogs.objects.create(user=user,title=title, video=video, description=description)
        vlog.save()
        return render(request, 'artistvlogs.html', {'user': user, 'vlogs': vlogs, 'success': 'Vlog created successfully!'})
    return render(request, 'artistvlogs.html', {'user': user, 'vlogs': vlogs})

def deletevlog(request):
    vlog = Vlogs.objects.get(id=request.GET['id'])
    vlog.delete()
    return redirect('/artistvlogs')

def uservlogs(request):
    user = User_tbl.objects.get(user_id=request.session['uid'])
    vlogs = Vlogs.objects.all()
    return render(request, 'uservlogs.html', {'user': user, 'vlogs': vlogs})

def galleryimages(request):
    user = Gallery_tbl.objects.get(user_id=request.session['uid'])
    images = GalleryImages.objects.filter(gallery=user).order_by('-id')
    if request.POST:
        image = request.FILES['image']
        description = request.POST['description']
        galleryimage = GalleryImages.objects.create(gallery=user, image=image, description=description)
        galleryimage.save()
        return render(request, 'galleryimages.html', {'user': user, 'images': images, 'success': 'Image uploaded successfully!'})
    return render(request, 'galleryimages.html', {'user': user, 'posts': images})

def deletegalleryimage(request):
    image = GalleryImages.objects.get(id=request.GET['id'])
    image.delete()
    return redirect('/galleryimages')

def galleryevents(request):
    user = Gallery_tbl.objects.get(user_id=request.session['uid'])
    events = Events.objects.filter(user=user)
    if request.POST:
        title= request.POST['title']
        description = request.POST['description']
        date = request.POST['date']
        time = request.POST['time']
        price = request.POST['price']
        max = request.POST['max']
        location = request.POST['location']
        image = request.FILES['image']
        event = Events.objects.create(user=user,title=title,price=price,image=image, description=description,date=date,time=time,location=location,max_participants=max,participants=0)
        event.save()
        return render(request, 'galleryevent.html', {'user': user, 'events': events, 'success': 'Event created successfully!'})
    return render(request, 'galleryevent.html', {'user': user, 'events': events})

def artistorders(request):
    user = Artist_tbl.objects.get(user_id=request.session['uid'])
    posts = Post.objects.filter(user=user, status='sold')
    return render(request, 'artistorders.html', {'user': user, 'posts': posts})

def artistevents(request):
    user = Artist_tbl.objects.get(user_id=request.session['uid'])
    today = datetime.now().date()
    events = Events.objects.filter(date__gte=today)
    booked= Bookslot.objects.filter(user=user)
    booked_events = [book.event.id for book in booked]
    bookedevents = Events.objects.filter(id__in=booked_events)
    return render(request, 'artistevents.html', {'user': user, 'events': events, 'booked_events': booked_events, 'bookedevents': bookedevents})

def buyslot(request):
    user = Artist_tbl.objects.get(user_id=request.session['uid'])
    event = Events.objects.get(id=request.GET['id'])
    if request.POST:
        booking = Bookslot.objects.create(user=user, event=event)
        booking.save()
        event.participants += 1
        event.save()
        return redirect('/artistevents')
    return render(request, 'buyslot.html', {'user': user, 'event': event})

def gallerybookings(request):
    event = Events.objects.get(user_id=request.GET['id'])
    bookings = Bookslot.objects.filter(event=event)
    return render(request, 'gallerybookings.html', {'event': event, 'bookings': bookings})

def artistprofile(request):
    user = User.objects.get(id=request.session['uid'])
    page=''
    if user.usertype == 'Customer':
        page='usercommon.html'
    elif user.usertype == 'Artist':
        page='artistcommon.html'
    elif user.usertype == 'Gallery':
        page='gallerycommon.html'
    artist = Artist_tbl.objects.get(id=request.GET['id'])
    posts= Post.objects.filter(user=artist)
    return render(request, 'artistprofile.html', {'user': user, 'artist': artist, 'page': page, 'posts': posts})

def userprofile(request):
    user = User.objects.get(id=request.session['uid'])
    page=''
    if user.usertype == 'Customer':
        page='usercommon.html'
    elif user.usertype == 'Artist':
        page='artistcommon.html'
    elif user.usertype == 'Gallery':
        page='gallerycommon.html'
    artist = User_tbl.objects.get(id=request.GET['id'])
    return render(request, 'userprofile.html', { 'user': artist, 'page': page})

def userchat(request):
    artists=Artist_tbl.objects.all()
    user = User_tbl.objects.get(user_id=request.session['uid'])
    chats = None
    try:
        artist=Artist_tbl.objects.get(id=request.session['reciever'])
        chats=User_Artist_Chat.objects.filter(user=user, artist__id=request.session['reciever'])
    except:
        artist=None
    if request.POST and artist is not None:
        chat = User_Artist_Chat.objects.create(user=user, artist=artist,message=request.POST['msg'], sender='user')
        chat.save()
    return render(request, 'userchat.html',{ 'user': user, 'artists': artists, 'artist': artist, 'messages': chats})

def recieverid(request):
    id = request.GET['id']
    request.session['reciever'] = id
    return redirect('/userchat')

def artistchat(request):
    artists=User_tbl.objects.all()
    user = Artist_tbl.objects.get(user_id=request.session['uid'])
    chats = None
    try:
        artist=User_tbl.objects.get(id=request.session['ureciever'])
        chats=User_Artist_Chat.objects.filter(artist=user, user=artist)
    except:
        artist=None
    if request.POST and artist is not None:
        chat = User_Artist_Chat.objects.create(user=artist, artist=user,message=request.POST['msg'], sender='artist')
        chat.save()
    return render(request, 'artistchat.html',{ 'user': user, 'artists': artists, 'artist': artist, 'messages': chats})

def urecieverid(request):
    id = request.GET['id']
    request.session['ureciever'] = id
    return redirect('/artistchat')

def artistgallerychat(request):
    galleries=Gallery_tbl.objects.all()
    artist = Artist_tbl.objects.get(user_id=request.session['uid'])
    chats = None
    try:
        gallery=Gallery_tbl.objects.get(id=request.session['greciever'])
        chats=Artist_Gallery_Chat.objects.filter(artist=artist, gallery=gallery)
    except:
        gallery=None
    if request.POST and gallery is not None:
        chat = Artist_Gallery_Chat.objects.create(gallery=gallery, artist=artist,message=request.POST['msg'], sender='artist')
        chat.save()
    return render(request, 'artistgallerychat.html',{ 'artist': artist, 'galleries': galleries, 'gallery': gallery, 'messages': chats})

def grecieverid(request):
    id = request.GET['id']
    request.session['greciever'] = id
    return redirect('/artistgallerychat')

def galleryartistchat(request):
    artists=Artist_tbl.objects.all()
    gallery = Gallery_tbl.objects.get(user_id=request.session['uid'])
    chats = None
    artist=None
    try:
        artist=Artist_tbl.objects.get(id=request.session['agreciever'])
        chats=Artist_Gallery_Chat.objects.filter(gallery=gallery, artist=artist)
    except:
        gallery=None
    if request.POST and gallery is not None:
        chat = Artist_Gallery_Chat.objects.create(gallery=gallery, artist=artist,message=request.POST['msg'], sender='gallery')
        chat.save()
    return render(request, 'gallerychat.html',{ 'gallery': gallery, 'artists': artists, 'artist': artist, 'messages': chats})

def agrecieverid(request):
    id = request.GET['id']
    request.session['agreciever'] = id
    return redirect('/galleryuserchat')

def adminusers(request):
    users = User_tbl.objects.all()
    return render(request, 'adminusers.html', {'users': users})

def adminartists(request):
    artists = Artist_tbl.objects.all()
    return render(request, 'adminusers.html', {'users': artists})

def admingalleries(request):
    galleries = Gallery_tbl.objects.all()
    return render(request, 'admingallery.html', {'galleries': galleries})

def toggleactive(request):
    user = User.objects.get(id=request.GET['id'])
    user.is_active = not user.is_active
    user.save()
    if user.usertype == 'Customer':
        return redirect('/adminusers')
    elif user.usertype == 'Artist':
        return redirect('/adminartists')
    elif user.usertype == 'Gallery':
        return redirect('/admingallery')

def adminreports(request):
    post = Post.objects.all()
    return render(request, 'adminorders.html', {'posts': post})

def artistcomments(request):
    user = Artist_tbl.objects.get(user_id=request.session['uid'])
    post = Post.objects.get(id=request.GET['id'])
    comments = Comments.objects.filter(post=post)
    if request.POST:
        comment = request.POST['comment']
        comments = Comments.objects.create(post=post, user=user, comment=comment)
        comments.save()
        return redirect(f'/artistcomments?id={post.id}')
    return render(request, 'artistcomments.html', {'user': user, 'post': post, 'comments': comments})