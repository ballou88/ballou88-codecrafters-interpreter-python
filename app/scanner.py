from app.token_type import TokenType
from app.token import Token

class Scanner:
    def __init__(self, source, error_class):
        self.source = source
        self.start = 0
        self.current = 0
        self.line = 1
        self.tokens = []
        self.has_lex_error = False
        self.error_class = error_class


    def scan_tokens(self):
        while (not self.is_at_end()):
            self.start = self.current
            self.scan_token()

        self.tokens.append( Token(TokenType.EOF, "", "null", self.line))
        return self.tokens

    def scan_token(self):
        character = self.advance()
        match character:
            case TokenType.LEFT_PAREN.value:
                self.addToken(TokenType.LEFT_PAREN, "null")
            case TokenType.RIGHT_PAREN.value:
                self.addToken(TokenType.RIGHT_PAREN, "null")
            case TokenType.LEFT_BRACE.value:
                self.addToken(TokenType.LEFT_BRACE, "null")
            case TokenType.RIGHT_BRACE.value:
                self.addToken(TokenType.RIGHT_BRACE, "null")
            case TokenType.COMMA.value:
                self.addToken(TokenType.COMMA, "null")
            case TokenType.SEMICOLON.value:
                self.addToken(TokenType.SEMICOLON, "null")
            case TokenType.DOT.value:
                self.addToken(TokenType.DOT, "null")
            case TokenType.PLUS.value:
                self.addToken(TokenType.PLUS, "null")
            case TokenType.MINUS.value:
                self.addToken(TokenType.MINUS, "null")
            case TokenType.SLASH.value:
                self.addToken(TokenType.SLASH, "null")
            case TokenType.STAR.value:
                self.addToken(TokenType.STAR, "null")
            case TokenType.BANG.value:
                if self.match(TokenType.EQUAL.value):
                    token = TokenType.BANG_EQUAL
                else:
                    token = TokenType.BANG
                self.addToken(token, "null")
            case TokenType.EQUAL.value:
                if self.match(TokenType.EQUAL.value):
                    token = TokenType.EQUAL_EQUAL
                else:
                    token = TokenType.EQUAL
                self.addToken(token, "null")
            case TokenType.LESS.value:
                if self.match(TokenType.EQUAL.value):
                    token = TokenType.LESS_EQUAL
                else:
                    token = TokenType.LESS
                self.addToken(token, "null")
            case TokenType.GREATER.value:
                if self.match(TokenType.EQUAL.value):
                    token = TokenType.GREATER_EQUAL
                else:
                    token = TokenType.GREATER
                self.addToken(token, "null")
            case _:
                self.error_class.error(self.line, f"Unexpected character: {character}")
                self.has_lex_error = True

    def advance(self):
        character = self.source[self.current]
        self.current += 1
        return character

    def addToken(self, token_type, literal):
        text = self.source[self.start:self.current]
        self.tokens.append(Token(token_type, text, literal, self.line))

    def is_at_end(self):
        return self.current >= len(self.source)

    def match(self, expected):
        if self.is_at_end():
            return False
        if self.source[self.current] != expected:
            return False
        self.current += 1
        return True
