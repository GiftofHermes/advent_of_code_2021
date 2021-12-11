


with open('data/input.txt', 'r') as f:
    data = [line.strip() for line in f.readlines()]

mapping = {'(':')',
           '[':']',
           '{':'}',
           '<':'>',}

def find_illegal_character(line, mapping):
    queue = []
    for letter in line:
        if letter in ['(', '[', '{', '<']:
            queue.append(letter)
        elif queue and letter in [')', ']', '}', '>'] and mapping[queue[-1]] == letter:
            queue.pop(-1)
        else:
            return letter

def calculate_syntax_error_score(illegal_characters):
    score = 0
    for character in illegal_characters:
        if character == ')':
            score += 3
        elif character == ']':
            score += 57
        elif character == '}':
            score += 1197
        elif character == '>':
            score += 25137
    return score

def find_incomplete_characters(line, mapping):
    queue = []
    for letter in line:
        if letter in ['(', '[', '{', '<']:
            queue.append(letter)
        elif queue and letter in [')', ']', '}', '>'] and mapping[queue[-1]] == letter:
            queue.pop(-1)

    incomplete_characters = reversed([mapping[letter] for letter in queue])
    return incomplete_characters

def calculate_autocomplete_score(incomplete_characters):
    score = 0
    for character in incomplete_characters:
        score *= 5
        if character == ')':
            score += 1
        elif character == ']':
            score += 2
        elif character == '}':
            score += 3
        elif character == '>':
            score += 4
    return score



illegal_characters = filter(lambda x: x, [find_illegal_character(line, mapping) for line in data])
score = calculate_syntax_error_score(illegal_characters)
#print(score) # solution 1

incomplete_lines = list(filter(lambda x: not find_illegal_character(x, mapping), data))
incomplete_characters = [find_incomplete_characters(line, mapping) for line in incomplete_lines]
autocomplete_scores = sorted([calculate_autocomplete_score(incomplete) for incomplete in incomplete_characters])
middle_score_index = (len(autocomplete_scores)-1)//2
print(autocomplete_scores[middle_score_index])
