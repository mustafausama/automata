from typing import Dict, Set
from collections import deque
from .DFA import DFA
import automathon

class NFA:
    def __init__(self, states: Set[str], alphabet: Set[str], transitions: Dict[str, Set[str]], start_state: str, accept_states: Set[str]):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.accept_states = accept_states
        self.eplison_closure_cache = {}
        self.target_states_cache = {}

    def epsilon_closure(self, states: frozenset[str]) -> frozenset[str]:
        if states in self.eplison_closure_cache:
            return self.eplison_closure_cache[states]
        epsilon_closure_set = set(states)

        stack = list(states)
        while stack:
            current_state = stack.pop()
            if current_state in self.transitions and '' in self.transitions[current_state]:
                for state in self.transitions[current_state]['']:
                    if state not in epsilon_closure_set:
                        epsilon_closure_set.add(state)
                        stack.append(state)

        self.eplison_closure_cache[states] = frozenset(epsilon_closure_set)
        return frozenset(epsilon_closure_set)
    
    def target_states(self, states: frozenset[str], symbol: str) -> frozenset[str]:
        if states in self.target_states_cache and symbol in self.target_states_cache[states]:
            return self.target_states_cache[states][symbol]

        target_states_set = set()
        for state in states:
            state_closure = self.epsilon_closure(frozenset([state]))
            for sc in state_closure:
                if sc in self.transitions and symbol in self.transitions[sc]:
                    target_states_set.update(self.transitions[sc][symbol])
        
        target_states_set = set(self.epsilon_closure(frozenset(target_states_set)))
        if states not in self.target_states_cache:
            self.target_states_cache[states] = {}

        self.target_states_cache[states][symbol] = frozenset(target_states_set)

        return self.target_states_cache[states][symbol]

    def to_DFA(self) -> DFA:
        dfa_states = set()
        dfa_alphabet = self.alphabet.copy()
        dfa_transitions = {}
        dfa_initial_state = self.epsilon_closure(frozenset([self.start_state]))
        dfa_accept_states = set()
        
        unprocessed_states = deque([dfa_initial_state])
        
        while unprocessed_states:
            current_state = unprocessed_states.popleft()
            dfa_states.add(current_state)
            dfa_transitions[current_state] = {}
            for symbol in self.alphabet:
                target_state = self.target_states(current_state, symbol)
                if target_state not in unprocessed_states and target_state not in dfa_states:
                    unprocessed_states.append(target_state)
                dfa_transitions[current_state][symbol] = target_state
            if any(accept in self.accept_states for accept in current_state):
                dfa_accept_states.add(current_state)
        
        return DFA(dfa_states, dfa_alphabet, dfa_transitions, dfa_initial_state, dfa_accept_states)

    def to_automathonNFA(self) -> automathon.NFA:
        nfa = automathon.NFA(
            Q=self.states,
            sigma=self.alphabet,
            delta=self.transitions,
            initialState=self.start_state,
            F=self.accept_states
        )
        return nfa 
        
