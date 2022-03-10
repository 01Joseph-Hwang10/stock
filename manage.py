import click
from stock_tracker.src.app import init_app_dev

@click.group()
def cli():
    pass

@click.command()
def dev():
    init_app_dev().run()

cli.add_command(dev)

if __name__ == '__main__':
    cli()
