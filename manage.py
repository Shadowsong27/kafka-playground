import click


@click.group()
def cli():
    pass


@cli.command()
def start_publish_streaming_data():
    from main import publish_data
    publish_data()


@cli.command()
def start_consume_streaming_data():
    from main import consume_data
    consume_data()


if __name__ == '__main__':
    cli()
