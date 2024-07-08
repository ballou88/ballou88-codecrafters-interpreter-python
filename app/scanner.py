from app.token_type import TokenType
from app.token import Token

NUMBER_LITERALS  = ['1','2','3','4','5','6','7','8','9','0']
KEYWORDS = {
    "and": TokenType.AND,
    "or": TokenType.OR,
    "class": TokenType.CLASS,
    "else": TokenType.ELSE,
    "false": TokenType.FALSE,
    "fun": TokenType.FUN,
    "for": TokenType.FOR,
    "if": TokenType.IF,
    "nil": TokenType.NIL,
    "print": TokenType.PRINT,
    "return": TokenType.RETURN,
    "super": TokenType.SUPER,
    "this": TokenType.THIS,
    "true": TokenType.TRUE,
    "var": TokenType.VAR,
    "while": TokenType.WHILE,

}

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
                self.addToken(TokenType.LEFT_PAREN)
            case TokenType.RIGHT_PAREN.value:
                self.addToken(TokenType.RIGHT_PAREN)
            case TokenType.LEFT_BRACE.value:
                self.addToken(TokenType.LEFT_BRACE)
            case TokenType.RIGHT_BRACE.value:
                self.addToken(TokenType.RIGHT_BRACE)
            case TokenType.COMMA.value:
                self.addToken(TokenType.COMMA)
            case TokenType.SEMICOLON.value:
                self.addToken(TokenType.SEMICOLON)
            case TokenType.DOT.value:
                self.addToken(TokenType.DOT)
            case TokenType.PLUS.value:
                self.addToken(TokenType.PLUS)
            case TokenType.MINUS.value:
                self.addToken(TokenType.MINUS)
            case TokenType.SLASH.value:
                if self.match('/'):
                    while self.peek() != '\n' and not self.is_at_end():
                        self.advance()
                else:
                    self.addToken(TokenType.SLASH)
            case TokenType.STAR.value:
                self.addToken(TokenType.STAR)
            case TokenType.BANG.value:
                if self.match(TokenType.EQUAL.value):
                    token = TokenType.BANG_EQUAL
                else:
                    token = TokenType.BANG
                self.addToken(token)
            case TokenType.EQUAL.value:
                if self.match(TokenType.EQUAL.value):
                    token = TokenType.EQUAL_EQUAL
                else:
                    token = TokenType.EQUAL
                self.addToken(token)
            case TokenType.LESS.value:
                if self.match(TokenType.EQUAL.value):
                    token = TokenType.LESS_EQUAL
                else:
                    token = TokenType.LESS
                self.addToken(token)
            case TokenType.GREATER.value:
                if self.match(TokenType.EQUAL.value):
                    token = TokenType.GREATER_EQUAL
                else:
                    token = TokenType.GREATER
                self.addToken(token)
            case ' ':
                pass
            case '\t':
                pass
            case '\r':
                pass
            case '\n':
                self.line += 1
                pass
            case '"':
                self.string()
            case c if c in NUMBER_LITERALS:
                self.number()
            case c if self.isAlpha(c):
                self.identifier()
            case _:
                self.error_class.error(self.line, f"Unexpected character: {character}")
                self.has_lex_error = True


    def identifier(self):
        while self.isAlphaNumeric(self.peek()):
            self.advance()
        text = self.source[self.start:self.current]
        if text in KEYWORDS:
            self.addToken(KEYWORDS[text])
        else:
            self.addToken(TokenType.IDENTIFIER)

    def isAlpha(self, character):
        return (character >= 'a' and character <= 'z') or (character >= 'A' and character <= 'Z') or (character == '_')

    def isAlphaNumeric(self, character):
        return self.isAlpha(character) or character in NUMBER_LITERALS

    def string(self):
        while c:= self.peek() != '"' and not self.is_at_end():
            if c == '\n':
                self.line += 1
            self.advance()
        if self.is_at_end():
            self.error_class.error(self.line, "Unterminated string.")
            self.has_lex_error = True
            return
        self.advance()
        value = self.source[self.start + 1:self.current - 1]
        self.addToken(TokenType.STRING, value)

    def number(self):
        while num := self.peek() in NUMBER_LITERALS:
            self.advance()
        if self.peek() == '.' and self.peek_next() in NUMBER_LITERALS:
            self.advance()
            while self.peek() in NUMBER_LITERALS:
                self.advance()
        value = self.source[self.start: self.current]
        self.addToken(TokenType.NUMBER, str(float(value)))

    def peek_next(self):
        if self.current + 1 >= len(self.source):
            return '\0'
        return self.source[self.current + 1]

    def advance(self):
        character = self.source[self.current]
        self.current += 1
        return character

    def addToken(self, token_type, literal="null"):
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

    def peek(self):
        if self.is_at_end():
            return '\0'
        else:
            return self.source[self.current]
