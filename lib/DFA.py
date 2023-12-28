from visual_automata.fa.dfa import VisualDFA
from typing import Dict, Set

class DFA:
    def __init__(self, states: Set[str], alphabet: Set[str], transitions: Dict[str, Set[str]], start_state: str, accept_states: Set[str]):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.accept_states = accept_states
    
    def to_visualDFA(self) -> VisualDFA:
        visualDFA_states = {DFA.frozen_set_to_str(state) for state in self.states}
        visualDFA_input_symbols = self.alphabet.copy()
        visualDFA_states_transitions = {}
        for key, val in self.transitions.items():
            new_key = DFA.frozen_set_to_str(key)
            visualDFA_states_transitions[new_key] = {}
            for symbol, target in val.items():
                visualDFA_states_transitions[new_key][symbol] = DFA.frozen_set_to_str(target)

        visualDFA_initial_state = DFA.frozen_set_to_str(self.start_state)
        visualDFA_accept_states = {DFA.frozen_set_to_str(state) for state in self.accept_states}

        visualDFA = VisualDFA(
            states=visualDFA_states,
            input_symbols=visualDFA_input_symbols,
            transitions=visualDFA_states_transitions,
            initial_state=visualDFA_initial_state,
            final_states=visualDFA_accept_states
        )
        
        return visualDFA

    def frozen_set_to_str(states: frozenset[str]) -> str:
        if not states:
            return '@'
        return '{' + ', '.join(sorted(states)) + '}'

