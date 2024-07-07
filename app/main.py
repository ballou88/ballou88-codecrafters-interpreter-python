import sys
import scanner

VALID_CHARACTERS = {
    "(": "LEFT_PAREN",
    ")": "RIGHT_PAREN",
    "{": "LEFT_BRACE",
    "}": "RIGHT_BRACE",
    "+": "PLUS",
    "-": "MINUS",
    "*": "STAR",
    "/": "SLASH",
    ".": "DOT",
    ",": "COMMA",
    ";": "SEMICOLON",
}

def print_error(line, character):
    print(f"[line {line}] Error: Unexpected character: {character}", file=sys.stderr)

def print_match(character):
    print(f"{VALID_CHARACTERS[character]} {character} null")

def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!", file=sys.stderr)

    if len(sys.argv) < 3:
        print("Usage: ./your_program.sh tokenize <filename>", file=sys.stderr)
        exit(1)

    command = sys.argv[1]
    filename = sys.argv[2]

    if command != "tokenize":
        print(f"Unknown command: {command}", file=sys.stderr)
        exit(1)

    with open(filename) as file:
        file_contents = file.read()
    scanner = Scanner(file_contents)
    scanner.scan_tokens()
    print("EOF  null") # Placeholder, remove this line when implementing the scanner
    if has_lex_error:
        sys.exit(65)



if __name__ == "__main__":
    main()
