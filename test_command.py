from pathlib import Path
command_file = Path("/tmp/football_robot_command")

if command_file.exists():
    command = command_file.read_text().strip()
    print("Command received", command)
else:
    print("No command file found")