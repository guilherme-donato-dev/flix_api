import pandas as pd
from django.core.management.base import BaseCommand
from actors.models import Actor

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            'file_name',
            type=str,
            help='Nome do arquivo CSV com os atores'
        )

    def handle(self, *args, **options):
        file_name = options['file_name']

        try:
            #lendo o CSV com pandas
            df = pd.read_csv(file_name)

            #validando se as colunas estão certas
            expected_columns = {'name', 'birthday', 'nationality'}
            if not expected_columns.issubset(df.columns):
                self.stdout.write(self.style.ERROR('O CSV deve ter as colunas: name, birthday, nationality'))
                return

            #inserindo cada ator no banco
            for _, row in df.iterrows():
                actor, created = Actor.objects.get_or_create(
                    name=row['name'],
                    defaults={
                        'birthday': row['birthday'],
                        'nationality': row['nationality']
                    }
                )

                if created:
                    self.stdout.write(self.style.SUCCESS(f"Ator {row['name']} cadastrado com sucesso!"))
                else:
                    self.stdout.write(self.style.WARNING(f"Ator {row['name']} já existe no banco."))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Erro ao importar o arquivo: {e}"))
