def solution(skill, skill_trees):
    answer = 0
    skill = list(skill)
    for skill_tree in skill_trees:
        skill_tree = list(skill_tree)
        sequence = []
        for s in skill_tree:
            if s in skill:
                sequence.append(s)
        answer += 1 if skill[:len(sequence)] == sequence else 0
    return answer