import subprocess

def proc():
    pass

def sub():
    print("Creating new subprocess")
    _p = subprocess.Popen([
    'python',
    "C:\Programming\Python\Discordbob\discordbot.py",
    ],
    shell = True
    )
    return _p

def main():
    p = sub()
    while True:
        try:
            proc()
        except KeyboardInterrupt:
            print("Interrput detected, restarting")
            p.terminate()
            p = sub()

if __name__ == '__main__':
    main()
