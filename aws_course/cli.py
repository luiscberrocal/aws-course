"""Console script for aws_course."""

import click


@click.command()
def main():
    """Main entrypoint."""
    click.echo("aws-course")
    click.echo("=" * len("aws-course"))
    click.echo("2024 AWS Course")


if __name__ == "__main__":
    main()  # pragma: no cover
