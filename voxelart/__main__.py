from pathlib import Path

import click

from . import launch


@click.command()
@click.option("--address", default="0.0.0.0", help="The address to run the server on")
@click.option("--port", default=6464, type=int, help="The port to run the server on")
@click.argument("directory", type=Path)
def app(address: str, port: int, directory: Path) -> None:
    """Create voxel arts for Minecraft BE world"""
    launch(address, port, directory)


if __name__ == "__main__":
    app()
