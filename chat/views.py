from django.shortcuts import render, redirect
from chat.models import Room, Message
from django.http import HttpResponse, JsonResponse

# Home view
def home(request):
    return render(request, 'home.html')

# Room view (update to use room id for fetching messages)
def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)  # Get room by name
    return render(request, 'room.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })

# Check if room exists, create new one if not
def checkview(request):
    room = request.POST["room_name"]
    username = request.POST["username"]
    if Room.objects.filter(name=room).exists():
        return redirect('/' + room + '/?username=' + username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/' + room + '/?username=' + username)

# Send message view (updated to save message with room object)
def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']
    room = Room.objects.get(id=room_id)  # Fetch room by ID
    new_message = Message.objects.create(value=message, user=username, room=room)
    new_message.save()
    return HttpResponse("Message sent successfully")

# Get messages for a room (updated to use room id in URL)
def getMessages(request, room):
    room_obj = Room.objects.get(name=room)  # Fetch room by name
    messages = Message.objects.filter(room=room_obj).order_by('date')
    message_list = [{"user": msg.user, "value": msg.value, "date": msg.date.strftime("%Y-%m-%d %H:%M:%S")} for msg in messages]
    return JsonResponse({"messages": message_list})
