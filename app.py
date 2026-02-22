from calculator import add, divide
import subprocess

print(add(10, 5))
print(divide(10, 0))

subprocess.call("ls -la", shell=True)