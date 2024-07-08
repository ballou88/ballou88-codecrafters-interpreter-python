import sys
from app.scanner import Scanner


class Lox:
    def __init__(self, filename):
        with open(filename) as file:
            self.file_contents = file.read()

    def run(self):
        # scanner = Scanner(self.file_contents, sys.stderr)
        scanner = Scanner(self.file_contents, Lox)
        tokens = scanner.scan_tokens()
        for token in tokens:
            print(token)
        if scanner.has_lex_error:
            sys.exit(65)

    @classmethod
    def error(cls, line, message):
        cls.report(line, "", message)

    @classmethod
    def report(cls, line, where, message):
        print(f"[line {line}] Error{where}: {message}", file=sys.stderr)
