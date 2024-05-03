import subprocess as sub

result = sub.run(['ls', '-l'], capture_output=True, text=True) # type: ignore

print(result.stdout)

filename = 'example.txt'

sub.run(['touch',filename])

with open('output.txt', 'w') as output_file:
    sub.run(['echo', 'Hello world'], stdout=output_file)

try:
    sub.run(['cat', 'nonexistentfile.txt'],check=True)
except sub.CalledProcessError as e:
    print(f"Error: {e}")