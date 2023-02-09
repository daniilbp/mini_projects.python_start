from typing import Any, IO


class FileCM:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.file = None

    def __enter__(self) -> IO:
        if self.filename:
            self.file = open(self.filename, 'a', encoding='utf-8')
        else:
            self.file = open(self.filename, 'w', encoding='utf-8')
        return self.file

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> bool:
        self.file.close()
        return True


with FileCM('example_2.txt') as file:
    file.write('Hello!\n')
