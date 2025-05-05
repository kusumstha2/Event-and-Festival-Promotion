from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import (
    Organizer, Event, Ticket, Booking, Media, AuditLog,
    Notification, QRCode, EventAnalytics, EventReview
)
from .serializers import (
    OrganizerSerializer, EventSerializer, TicketSerializer, BookingSerializer,
    MediaSerializer, AuditLogSerializer, NotificationSerializer, QRCodeSerializer,
    EventAnalyticsSerializer, EventReviewSerializer
)

class OrganizerViewSet(viewsets.ModelViewSet):
    queryset = Organizer.objects.all()
    serializer_class = OrganizerSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class MediaViewSet(viewsets.ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer

class AuditLogViewSet(viewsets.ModelViewSet):
    queryset = AuditLog.objects.all()
    serializer_class = AuditLogSerializer

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

class QRCodeViewSet(viewsets.ModelViewSet):
    queryset = QRCode.objects.all()
    serializer_class = QRCodeSerializer

class EventAnalyticsViewSet(viewsets.ModelViewSet):
    queryset = EventAnalytics.objects.all()
    serializer_class = EventAnalyticsSerializer

class EventReviewViewSet(viewsets.ModelViewSet):
    queryset = EventReview.objects.all()
    serializer_class = EventReviewSerializer
