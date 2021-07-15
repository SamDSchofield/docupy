"""
Wrapper for commands you run in the terminal which save the command and meta data
"""

import click
import subprocess
from datetime import datetime
from pathlib import Path


@click.command()
@click.argument("command", nargs=-1)
@click.option("--output", default=".")
def doc(command, output):
    Path(output).parent.mkdir(parents=True, exist_ok=True)
    notes = input("Notes: ")
    with open(output, "a+") as out_file:
        out_command = " ".join(command)
        out_file.write(f"Command:\n{out_command}\n\n")

        now = datetime.now()
        out_file.write(f"Run at {now}\n")
        out_file.write(f"\nNotes:\n{notes}\n")
        out_file.write("*" * 80 + "\n")

    if len(command[0].split()) > 1:
       command = command[0].split()
    p = subprocess.Popen(command)
    p.wait()


doc()