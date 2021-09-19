from collections import Counter

def solution(participant, completion):
    participant = Counter(participant)
    for name in completion:
        participant[name] -= 1

    for name in participant.keys():
        if participant[name] > 0:
            return name