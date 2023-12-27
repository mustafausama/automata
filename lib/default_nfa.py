from .NFA import NFA

default_nfa = NFA(
    states={'1', '2', '3', '4'},
    alphabet={'a', 'b'},
    transitions={
        '1': {'a': {'4'}},
        '2': {'a': {'3'}, 'b': {'2'}},
        '3': {'a': {'4'}, 'b': {'1', '4'}},
        '4': {'b': {'3'}},
    },
    start_state='1',
    accept_states={'3'}
)
