"""
Wrapper for commands you run in the terminal which save the command and meta data
"""

import click
import subprocess


@click.command()
@click.argument("command", nargs=-1)
@click.option("--output", default=".")
def doc(command, output):
    notes = input("Notes: ")

    p = subprocess.Popen(command)
    p.wait()

    with open(output, "a+") as out_file:
        out_file.write(f"Command:\n{' '.join(command)}\n\n")
        from datetime import datetime

        now = datetime.now()
        out_file.write(f"Run at {now}\n")
        out_file.write(f"\nNotes:\n{notes}\n")
        out_file.write("*" * 80 + "\n")

doc()