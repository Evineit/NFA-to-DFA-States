from getDFAStates import get_state, get_all_states

locket_e = {0, 1, 5, 10}
# states = [locket_e]

nfa_states = {
    0: {
        "void": {1, 5, 10}
    },
    1: {
        "a": {2},
        "b": {3},
    },
    2: {
        "void": {4}
    },
    3: {
        "void": {4}
    },
    4: {
        "void": {1}
    },
    5: {
        "a": {6},
        "c": {7},
        "d": {8},
    },
    6: {
        "void": {9}
    },
    7: {
        "void": {9}
    },
    8: {
        "void": {9}
    },
    9: {
        "void": {5}
    },
    10: {
        "b": {12},
        "c": {11},
        "e": {13},
    },
    11: {
        "void": {14}
    },
    12: {
        "void": {14}
    },
    13: {
        "void": {14}
    },
    14: {
        "void": {10}
    }
}


def test_locket_get_states():
    assert get_state(locket_e, nfa_states, "a") == {2,4,1,6,9,5}

def test_get_b_states():
    assert get_state(locket_e, nfa_states, "b") == {3,4,1,12,14,10}

def test_get_c_states():
    assert get_state(locket_e, nfa_states, "c") == {7,5,9,11,14,10}

def test_get_d_states():
    assert get_state(locket_e, nfa_states, "d") == {8,9,5}

def test_get_e_states():
    assert get_state(locket_e, nfa_states, "e") == {13,14,10}

def test_get_all_states():
    assert len(get_all_states(locket_e, nfa_states)) == 5
