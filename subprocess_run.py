import subprocess

try:
    result= subprocess.run(
        ['python', 'lcm.py'],
        capture_output=True,
        text=True,
        check=True,
        timeout=5
    )
    print("result:",result.stdout)
except subprocess.CalledProcessError as e:
    print(e.stderr)
    print(e.returncode)
except FileNotFoundError as e:
    print(e)