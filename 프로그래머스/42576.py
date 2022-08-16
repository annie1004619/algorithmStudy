def solution(participant, completion):
    p_dict = {}
    for name in participant:
        if name in p_dict:
            p_dict[name] += 1
        else:
            p_dict[name] = 1


    for name in completion:
        p_dict[name]=p_dict[name]-1
        
    for key,value in p_dict.items():
        if(value != 0):
            return key

participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["josipa", "filipa", "marina", "nikola"]

print(solution(participant,completion))