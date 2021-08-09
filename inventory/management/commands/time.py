from django.core.management.base import BaseCommand,CommandError
from django.utils import timezone
from inventory.models import Warehouse

class Command(BaseCommand):
    help = 'Displays current time'


    def add_arguments(self, parser):
        parser.add_argument('warehouse_id', nargs='+', type=int)

    def handle(self, *args, **kwargs):
        time = timezone.now().strftime('%X')
        self.stdout.write("It's now %s" % time)

        for warehouse in kwargs['warehouse_id']:
            try:
                poll = Warehouse.objects.get(pk=warehouse)
            except Warehouse.DoesNotExist:
                raise CommandError('Warehouse "%s" does not exist' % warehouse)
            

            self.stdout.write(self.style.SUCCESS('Successfully read warehouse "%s"' % warehouse))

                


    