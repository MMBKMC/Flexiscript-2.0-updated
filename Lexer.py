import re

def lexer(code):
    tokens = []
    keywords = ['SET', 'PRINT', 'IF', 'ELSE', 'ENDIF']  # Define keywords
    pattern = '|'.join([re.escape(keyword) for keyword in keywords])  # Compile regex pattern
    
    for token in re.split('(\s+)', code):
        if re.match(pattern, token):
            tokens.append(('KEYWORD', token))
        elif token.isdigit():
            tokens.append(('NUMBER', int(token)))
        elif token.isidentifier():
            tokens.append(('IDENTIFIER', token))
    
    return tokens
