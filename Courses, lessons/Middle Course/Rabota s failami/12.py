with open('new_scores.txt', 'w', encoding='utf-8') as file, open('class_scores.txt', 'r', encoding='utf-8') as old_file:
    for line in old_file:
        name, score = line.split()
        score = int(score) + 5
        if score > 100:
            score = 100
        print(name, score, file=file)

