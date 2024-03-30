def parser(tokens):
    parsed = []
    i = 0
    while i < len(tokens):
        if tokens[i][0] == 'SET':
            parsed.append(('SET', tokens[i+1][1], tokens[i+2][1]))
            i += 3
        elif tokens[i][0] == 'PRINT':
            parsed.append(('PRINT', tokens[i+1][1]))
            i += 2
        elif tokens[i][0] == 'IF':
            # Handle IF-ELSE-ENDIF block
            condition = tokens[i+1][1]
            if_block = []
            i += 2
            while i < len(tokens) and tokens[i][0] != 'ELSE' and tokens[i][0] != 'ENDIF':
                if_block.append(tokens[i])
                i += 1
            else_block = []
            if tokens[i][0] == 'ELSE':
                i += 1
                while i < len(tokens) and tokens[i][0] != 'ENDIF':
                    else_block.append(tokens[i])
                    i += 1
            parsed.append(('IF', condition, if_block, else_block))
            i += 1  # Move past ENDIF
        else:
            raise SyntaxError('Invalid token: ' + tokens[i][1])
    return parsed
