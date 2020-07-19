from django.conf import settings
from django.core.mail import send_mail
from django.core.management.base import BaseCommand
from django.utils import timezone

from events.models import Event


class Command(BaseCommand):
    help = 'Отправка уведомлений на почту пользователям'

    def handle(self, *args, **options):
        print(self.help)

        time_edge = timezone.now() + timezone.timedelta(hours=1)
        events = Event.objects.filter(start_time__lte=time_edge, notified=False)

        count = 0

        for event in events:
            title = f'Уведомление: {event.title}'
            message = f'''<h1>{event.title}</h1>
                <p>{event.description}</p>
                <strong>Начало события: {event.start_time}</strong>'''

            try:
                if send_mail(title, message, settings.EMAIL_HOST_USER, [event.user.email], fail_silently=False):
                    event.notified = True
                    event.save()
                    count += 1
            except Exception as e:
                print(e)

        print(f'Отправлено: {count}')
