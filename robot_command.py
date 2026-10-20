#!/usr/bin/env python3

import sys

COMMAND_FILE = "/var/lib/football_robot/robot_command.txt"

if len(sys.argv) > 1:
    command = sys.argv[1].upper()

    if command == "START":
        with open(COMMAND_FILE, "w") as file:
            file.write("START")

        print("START command written")
    else:
        print("Unknown command:", command)
