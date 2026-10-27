# from enum import Enum # use an enum singleton
import core
import time
import os
import json

class Log () : # make log a singleton

    def __init__(self):
        pass

    def store(self, directory:core.Directory, user:core.User, message:str) -> None:
        os.makedirs(directory.path, exist_ok=True)
        base = f"{directory.path}{user.name}_{time.strftime('%Y-%m-%d')}"

        # .log
        try : 
            with open(f'{base}.log', "a") as file:
                file.write(f"{time.strftime('%H hour %M min %S sec')}: {message}\n")
        except OSError as e:
            print(f'An error occurd: {e}')

        # .jsonl
        entry = {
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime()),
            "user": user.name,
            "message": message,
        }
        try : 
            with open(f'{base}.jsonl', "a") as file:
                file.write(json.dumps(entry, ensure_ascii=False) + "\n")
        except OSError as e:
            print(f'An error occurd: {e}')
        pass
    pass


if __name__ == "__main__": 
    u:core.User = core.User("testBot")
    d:core.Directory = core.Directory("./simple_package/tests/logs/")

    log:Log = Log()
    log.store(d, u, "testing")
    pass