import click
from stock_tracker.src.app import init_app_dev
from scripts.health_check import main as do_health_check
from scripts.upload import upload_config, push_code

@click.group()
def cli():
    pass

@click.command()
def dev():
    init_app_dev().run()

@click.command('health-check')
def health_check():
    do_health_check()

class UploadMode:
    config = 'config'
    code = 'code'
    all = 'all'

@click.command()
@click.argument('command', nargs=1)
def upload(command):
    if command == UploadMode.config or command == UploadMode.all or command == None:
        upload_config()
    if command == UploadMode.code or command == UploadMode.all or command == None:
        push_code()

cli.add_command(dev)
cli.add_command(health_check)
cli.add_command(upload)

if __name__ == '__main__':
    cli()
