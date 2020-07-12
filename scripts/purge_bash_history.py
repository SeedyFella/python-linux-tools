#!/usr/bin/python
"""Creates a copy of the ~/.bash_history file, excluding
lines which contain keywords defined in a list."""
from os import chmod, remove
from os.path import expanduser, isfile

# Define environment variables.
home = expanduser("~")
old_history_path = home + "/.bash_history"
new_history_path = home + "/.bash_history_new"

# Open the ~/.bash_history file to be purged.
try:
    old_history = open(old_history_path, "r")
except FileNotFoundError:
    print("ERROR:", old_history_path, "not found.")
    raise SystemExit(0)

# Check if ~/.bash_history_new already exists.
try:
    if isfile(new_history_path):
        remove(new_history_path)
    new_history = open(new_history_path, "x")
except FileExistsError:
    print("ERROR:", new_history_path, "already exists.")
    old_history.close()
    raise SystemExit(0)

# The strings to be purged. Edit this list to suit your needs.
purge_strings = [
    "clear",
    "exit",
    "ls",
    "ping",
    "time"
]

# Copy the old history file into the new one, excluding purge strings.
for line in old_history:
    if any(word in line for word in purge_strings):
        continue
    new_history.write(line)

# Close all files.
old_history.close()
new_history.close()

# Set new file permissions and finish.
chmod(new_history_path, 0o600)
