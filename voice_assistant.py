import subprocess

command = input("Command: ").lower()

apps = {
    "notepad": "notepad.exe",
    "calculator": "calc.exe"
}

if command in apps:
    subprocess.Popen(apps[command])
else:
    print("Unknown command")