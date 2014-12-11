import subprocess
exe_path = '/Users/chanita/projects/pronto/ban2stats/client/webservice_client.py'
from django.core.management import call_command
from django.core.management.base import BaseCommand

def attack(ip, service_name):
    command_arguments = [exe_path,  service_name, "https", "81", ip]
    process = subprocess.Popen(command_arguments, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (output, err) = process.communicate()
    exit_code = process.wait()
    if exit_code > 0:
        result = 'error.'
        command_output = err
    else:
        result = 'success.'
        command_output = output
    print result, command_output


class Command(BaseCommand):
    help = 'Generate attacks.'

    def handle(self, *args, **options):

        # for i in range(172,173):
        #     ip = '114.82.{0}.3'.format(i)
        #     attack(ip, 'Evil Service')
        #
        # for i in range(2,220):
        #     ip = '114.{0}.19.3'.format(i)
        #     attack(ip, 'Company Portal')
        #
        # for i in range(33, 80):
        #     ip = '114.48.19.{0}'.format(i)
        #     attack(ip, 'Human Resource Control Portal')
        #
        # for i in range(20, 233):
        #     ip = '114.48.20.{0}'.format( i)
        #     attack(ip, 'Financial Department Portal')
        # for i in range(40, 233):
        #     ip = '114.48.20.{0}'.format( i)
        #     attack(ip, 'Financial Department Portal')
        # for i in range(83, 133):
        #     ip = '114.48.20.{0}'.format( i)
        #     attack(ip, 'Financial Department Portal')
        # for i in range(12, 140):
        #     ip = '114.109.188.{0}'.format( i)
        #     attack(ip, 'Financial Department Portal')
        # for i in range(32, 109):
        #     ip = '72.14.20.{0}'.format( i)
        #     attack(ip, 'Financial Department Portal')
        # for i in range(2, 179):
        #     ip = '72.14.12.{0}'.format( i)
        #     attack(ip, 'Human Resource Control Portal')
        #
        # for i in range(12, 240):
        #     ip = '114.109.{0}.4'.format( i)
        #     attack(ip, 'Financial Department Portal')
        # for i in range(32, 109):
        #     ip = '72.90.20.{0}'.format( i)
        #     attack(ip, 'Financial Department Portal')
        # for i in range(2, 179):
        #     ip = '72.14.1.{0}'.format(i)
        #     attack(ip, 'Human Resource Control Portal')
        #
        # call_command('rebuild_index', interactive=False, verbosity=0)
        #
        # for i in range(172,210):
        #     for j in range(2,220):
        #         for k in range(2,220):
        #             for l in range(1, 248):
        #                 ip = '{0}.{1}.{2}.{3}'.format(i, j, k, l)
        #                 attack(ip, 'Evil Service')
        #
        #             ip = '114.{0}.{1}.{2}'.format(i, j, k)
        #             attack(ip, 'Company Portal')
        #
        #         ip = '{3}.{1}.{2}.{0}'.format(i, j, k, l)
        #         attack(ip, 'Human Resource Control Portal')
        #
        #         ip = '114.{j}.20.{0}'.format(i,j)
        #         attack(ip, 'Financial Department Portal')
        #
        #     for j in range(40, 233):
        #         ip = '114.48.{1}.{0}'.format(i,j)
        #         attack(ip, 'Financial Department Portal')

        for i in range(83, 133):
            ip = '114.48.20.{0}'.format( i)
            attack(ip, 'Financial Department Portal')

        for i in range(12, 140):
            ip = '114.109.188.{0}'.format(i)
            attack(ip, 'Financial Department Portal')
        for i in range(32, 109):
            ip = '72.14.20.{0}'.format(i)
            attack(ip, 'Financial Department Portal')
        for i in range(2, 179):
            ip = '72.14.12.{0}'.format(i)
            attack(ip, 'Human Resource Control Portal')

        call_command('rebuild_index', interactive=False, verbosity=0)

        for i in range(12, 240):
            ip = '114.109.{0}.4'.format(i)
            attack(ip, 'Financial Department Portal')
            for j in range(32, 109):
                ip = '72.90.20.{0}'.format(i)
                attack(ip, 'Financial Department Portal')
                for k in range(2, 179):
                    ip = '{2}.{1}.1.{0}'.format(i, j, k)
                    attack(ip, 'Human Resource Control Portal')

        call_command('rebuild_index', interactive=False, verbosity=0)

        for i in range(172,210):
            for j in range(2,220):
                for k in range(2,220):
                    for l in range(1, 248):
                        ip = '{0}.{1}.{2}.{3}'.format(i,j,k,l)
                        attack(ip, 'Evil Service')

                    ip = '114.{0}.{1}.{2}'.format(i,j,k)
                    attack(ip, 'Company Portal')

                ip = '{3}.{1}.{2}.{0}'.format(i,j,k)
                attack(ip, 'Human Resource Control Portal')

                ip = '114.{j}.20.{0}'.format(i,j)
                attack(ip, 'Financial Department Portal')

            for j in range(40, 233):
                ip = '114.48.{1}.{0}'.format(i,j)
                attack(ip, 'Financial Department Portal')

        call_command('rebuild_index', interactive=False, verbosity=0)

        for i in range(83, 133):
            ip = '114.48.20.{0}'.format( i)
            attack(ip, 'Financial Department Portal')

        for i in range(12, 140):
            ip = '114.109.188.{0}'.format(i)
            attack(ip, 'Financial Department Portal')
        for i in range(32, 109):
            ip = '72.14.20.{0}'.format(i)
            attack(ip, 'Financial Department Portal')
        for i in range(2, 179):
            ip = '72.14.12.{0}'.format(i)
            attack(ip, 'Human Resource Control Portal')

        call_command('rebuild_index', interactive=False, verbosity=0)

        for i in range(12, 240):
            ip = '114.109.{0}.4'.format(i)
            attack(ip, 'Financial Department Portal')
            for j in range(32, 109):
                ip = '72.90.20.{0}'.format(i)
                attack(ip, 'Financial Department Portal')
                for k in range(2, 179):
                    ip = '{2}.{1}.1.{0}'.format(i, j, k)
                    attack(ip, 'Human Resource Control Portal')
                    for l in range(2,243):
                        ip = '{0}.{1}.{2}.{4}'.format(k,j,l,i)
                        attack(ip, 'Magic Department')

        call_command('rebuild_index', interactive=False, verbosity=0)
        self.stdout.write('Done.')