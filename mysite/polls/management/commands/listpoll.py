from django.core.management.base import BaseCommand, CommandError
from polls.models import Poll

class Command(BaseCommand):
    args = ''
    help = 'List polls'

    def handle(self, *args, **options):
        for poll in Poll.objects.all():
            self.stdout.write("%s %s (enabled=%s)" % (poll.id, poll.name, poll.enabled))
