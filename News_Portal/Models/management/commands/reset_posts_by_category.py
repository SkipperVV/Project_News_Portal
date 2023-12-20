from django.core.management.base import BaseCommand, CommandError, CommandParser
from Models.models import Post, Category
'''Напишите команду для manage.py, которая будет удалять все 
новости из какой-либо категории, но только при подтверждении действия в консоли при выполнении команды.
в консоли:
python manage.py reset_posts_by_category "имя_категории"'''

class Command(BaseCommand):
    help = 'удаляет все новости из выбранной категории'

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('category', type=str)

    def handle(self, *args, **options):
        # Соберем наши категории:
        all_categ = [x for x in Category.objects.all()]

        try:
            categ_name = Category.objects.get(name=options['category'])
        except Category.DoesNotExist:
            print('Нет такой категории. В наличии только:', *all_categ)
            return
        
        print(f'\nВыбор статей для удаления категории: {categ_name}\nЧтобы удалить сразу все статьи этой категории, введите: all')

        for issue in Post.objects.filter(category = categ_name):
            answer= input(f'\nУверены, что нужно удалить статью "{issue.title}" автора "{issue.author}"?: yes/no?  ')
            
            match answer:
                case 'yes':
                    issue.delete()
                    self.stdout.write(self.style.SUCCESS(f'Статья "{issue.title}" успешно удалена'))
                case 'all':
                    print('Удаляю все статьи')
                    Post.objects.filter(category = categ_name).delete()
                    return
                case _:
                    print('Удаление отменено')

        print(f'Все статьи категории {categ_name} просмотренны и ненужные удалены.')


