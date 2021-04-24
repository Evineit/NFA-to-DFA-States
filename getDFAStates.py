
def get_all_states(initial_state, nfa_states, keys):
    states = []
    for key in keys:
        if new_state := get_state(initial_state, nfa_states, key) not in states:
            states.append(new_state)
    return states

def get_state(a_set, nfa_states, key):
    result = set()
    for value in a_set:
        if cur_set := nfa_states[value].get(key):
            result.update(cur_set)
    while extra := get_transitions(result, nfa_states):
        result.update(extra)
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
