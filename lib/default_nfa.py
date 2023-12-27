from .NFA import NFA

default_nfa = NFA(
    states={'1', '2', '3', '4', '5'},
    alphabet={'a', 'b'},
    transitions={
        '1': {'': {'2'}, 'a': {'3'}},
        '2': {'a': {'4', '5'}},
        '3': {'b': {'4'}},
        '5': {'a': {'4'}, 'b': {'4'}}
    },
    start_state='1',
    accept_states={'5'}
)
