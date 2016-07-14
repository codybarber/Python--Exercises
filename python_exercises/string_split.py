def split_string(string_input, delim):
    result = []
    startIndex = 0
    endIndex = string_input.index(delim)

    while True:
        part = string_input[:endIndex]
        result.append(part)
        startIndex = endIndex + len(delim)
        string_input = string_input[startIndex:]

        if delim in string_input:
            endIndex = string_input.index(delim)
        else:
            result.append(string_input)
            break

    return result

print split_string('JavaScript', 'a')
