def hey(phrase):
    if phrase.strip() == '':
        return 'Fine. Be that way!'

    final_char = phrase.strip()[-1]

    if final_char == '?':
        if phrase.isupper():
            return "Calm down, I know what I'm doing!"
        else:
            return 'Sure.'
    elif phrase.isupper():
        return 'Whoa, chill out!'
    else:
        return 'Whatever.'
