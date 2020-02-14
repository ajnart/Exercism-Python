def latest(scores):
    return(scores[-1])


def personal_best(scores):
    return(max(scores))


def personal_top_three(scores: list):
    scores.sort(reverse=True)
    while len(scores) > 3:
        scores.pop(-1)
    return scores
