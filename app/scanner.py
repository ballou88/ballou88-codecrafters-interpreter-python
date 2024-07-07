import token_type

class Scanner:
    def __init__(self, source):
        self.source = source
        self.start = 0
        self.current = 0
        self.line = 1
        self.tokens = []


    def scan_tokens(self):
        while (not is_at_end()):
            self.start = self.current
            scan_token()

        self.tokens.add( TokenType.EOF, "", None, line)
        return self.tokens

    def scan_token(self):
        character = self.advance()
        match character:
            case TokenType.LEFT_PAREN:
                self.addToken(TokenType.LEFT_PAREN)
            case TokenType.RIGHT_PAREN:
                self.addToken(TokenType.RIGHT_PAREN)


    def is_at_end(self):
        return self.current >= len(this.source)
