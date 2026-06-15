def solution(record):
    nickname = {}
    events = []
    
    for r in record:
        parts = r.split()
        action = parts[0]
        uid = parts[1]
        
        if action == "Enter":
            nickname[uid] = parts[2]
            events.append((action, uid))
        elif action == "Leave":
            events.append((action, uid))
        elif action == "Change":
            nickname[uid] = parts[2]
    
    result = []
    for action, uid in events:
        name = nickname[uid]
        if action == "Enter":
            result.append(f"{name}님이 들어왔습니다.")
        else:
            result.append(f"{name}님이 나갔습니다.")
    
    return result