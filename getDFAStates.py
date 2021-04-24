
def get_all_states(initial_state, nfa_states, keys):
    states = []
    to_print = "\n"
    for key in keys:
        new_state = get_state(initial_state, nfa_states, key)
        if new_state and new_state not in states:
            states.append(new_state)
            to_print+= f"{key} = {new_state}\n"
    print(to_print)
    return states

def get_state(a_set, nfa_states, key):
    result = set()
    for value in a_set:
        if cur_set := nfa_states[value].get(key):
            result.update(cur_set)
    while extra := get_transitions(result, nfa_states):
        result.update(extra)
    print(f"\n{key} = {result}")
    return result


def get_transitions(a_set, nfa_states):
    extra = set()
    for value in a_set:
        if cur_set := nfa_states[value].get("void"):
            if cur_set not in a_set:
                extra.update(cur_set)
    if extra.issubset(a_set):
        return
    return extra
