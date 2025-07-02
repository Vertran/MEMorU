import datetime

def make_log(level, text, annotations=None):
    time = datetime.datetime.now().strftime('%d.%m.%Y, %H:%M:%S')


    with open("game.log", "a", encoding="utf-8") as f:
        f.write(f"[{level.upper()}] [{time}]: {text}\n")
        if annotations:
            f.write(f"{annotations}\n")


make_log('info', 'Logger initialized.')