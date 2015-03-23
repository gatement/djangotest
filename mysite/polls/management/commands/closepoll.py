from django.core.management.base import BaseCommand, CommandError
from optparse import make_option
from polls.models import Poll

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--delete',
            action='store_true',
            dest='delete',
            default=False,
            help='Delete poll instead of closing it'),
        )
    args = '<poll_id poll_id ...>'
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        for poll_id in args:
            try:
                poll = Poll.objects.get(pk=int(poll_id))
            except Poll.DoesNotExist:
                raise CommandError('Poll "%s" does not exist' % poll_id)

            if options['delete']:
                poll.delete()
            else:
                poll.enabled = False
                poll.save()

            self.stdout.write('Successfully closed poll "%s"' % poll_id)
