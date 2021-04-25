from pprint import pprint
from yaml import load, FullLoader

def solve(locket_e, nfa_states, keys):
    print(f"Cerradura Ɛ:  {locket_e} = A *\n")
    solution = {
        'A': locket_e
    }
    states = []
    states.append(locket_e)
    loop_num = 0
    for state in states:
        letter = chr(ord('A')+loop_num)
        loop_num += 1
        temp_list = get_all_states(state, nfa_states, keys, letter, states)
        for state_set in temp_list:
            if state_set not in states:
                states.append(state_set)
                # print(f"estado {chr(ord('A')+len(states))} - {state_set} fue agregado")
    for state in states:
        if state not in solution.values():
            solution[chr(ord(list(solution.keys())[-1])+1)] = state
    pprint(solution)
    print(f"size={len(solution)}")
    # TODO: print number of final states and non final states in dfa
    return solution


def get_all_states(initial_state, nfa_states, keys, context_state_key, context_states = []) -> list:
    states = []
    new_states = []
    to_print = ""
    for key in keys:
        new_state = get_state(initial_state, nfa_states, key)
        if new_state in context_states:
            to_print += f"{context_state_key}, {key} = {new_state} = {chr(ord('A')+context_states.index(new_state))}\n" if new_state else f"{context_state_key}, {key} = {{}}\n"
        elif new_state in new_states:
            to_print += f"{context_state_key}, {key} = {new_state} = {chr(ord('A')+len(context_states)+new_states.index(new_state))}\n" if new_state else f"{context_state_key}, {key} = {{}}\n"
        else:
            to_print += f"{context_state_key}, {key} = {new_state} = {chr(ord('A')+len(context_states)+len(new_states))} * \n" if new_state else f"{context_state_key}, {key} = {{}}\n"
        if new_state and new_state not in states:
            states.append(new_state)
            if new_state not in context_states:
                new_states.append(new_state)
    print(to_print)
    # print("\n")
    # pprint(states)
    return states


def get_state(a_set, nfa_states, key):
    result = set()
    for value in a_set:
        if value in nfa_states.keys():
            if cur_set := nfa_states[value].get(key):
                result.update(cur_set)
    while extra := get_transitions(result, nfa_states):
        result.update(extra)
    return result


def get_transitions(a_set, nfa_states):
    extra = set()
    for value in a_set:
        if value in nfa_states.keys():
            if cur_set := nfa_states[value].get("void"):
                if cur_set not in a_set:
                    extra.update(cur_set)
    if extra.issubset(a_set):
        return
    return extra

if __name__ == "__main__":
    x = input("file name:\n")
    print("-"*80)
    with open(f"{x}.yaml") as to_solve:
        loaded_yaml = load(to_solve, Loader=FullLoader)
        solve(loaded_yaml['locket_e'], loaded_yaml["nfa_states"], loaded_yaml["keys"])
