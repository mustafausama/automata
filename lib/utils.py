from .NFA import NFA, DFA
import tkinter as tk
from PIL import Image, ImageTk

def input_NFA() -> NFA:

    print("\033[96m"+"NFA to DFA"+"\033[0m")

    # Enter states and validate them
    print("\033[93m"+"Enter states (space-separated): "+"\033[0m", end="")
    states = set(input().split())
    while not states or '' in states:
        print("\033[91m"+"--> Invalid state(s). Enter states (space-separated): "+"\033[0m", end="")
        states = set(input().split())

    # Enter alphabet and validate them
    print("\033[92m"+"Enter alphabet (space-separated): "+"\033[0m", end="")
    alphabet = set(input().split())
    while not alphabet or '' in alphabet:
        print("\033[91m"+"--> Invalid symbol(s). Enter alphabet (space-separated): "+"\033[0m", end="")
        alphabet = set(input().split())

    # Enter transitions and validate them
    print("\033[95m"+"Enter transitions"+"\033[0m")
    transitions = {}
    for state in sorted(states):
        transitions[state] = {}
        print("\033[33m"+"Enter transitions for source state "+state+"\033[0m")
        # Enter epslion transitions and validate them
        print("\033[94m"+"==> Enter target states for epslion transition (space-separated): \033[0m", end="")
        input_set = set(input().split())
        while not input_set.issubset(states):
            print("\033[91m"+"--> Invalid state(s). Enter epslion transitions (space-separated): \033[0m", end="")
            input_set = set(input().split())
        if input_set:
            transitions[state][''] = input_set
        # Enter other transitions and validate them
        for symbol in sorted(alphabet):
            print("\033[94m"+"==> Enter target states for symbol "+symbol+" (space-separated): \033[0m", end="")
            input_set = set(input().split())
            while not input_set.issubset(states):
                print("\033[91m"+"--> Invalid state(s). Enter target states for symbol "+symbol+"(space-separated): \033[0m", end="")
                input_set = set(input().split())
            if input_set:
                transitions[state][symbol] = input_set

    # Enter start state and validate it
    print("\033[92m"+"Enter start state: "+"\033[0m", end="")
    start_state = input()
    while(start_state not in states):
        print("\033[91m"+"--> Invalid state. Enter start state: "+"\033[0m", end="")
        start_state = input()

    # Enter accept states and validate them
    print("\033[95m"+"Enter accept states (space-separated): "+"\033[0m", end="")
    accept_states = set(input().split())
    while not accept_states.issubset(states):
        print("\033[91m"+"--> Invalid state(s). Enter accept states (space-separated): "+"\033[0m", end="")
        accept_states = set(input().split())

    # Create NFA
    nfa = NFA(
        states=states,
        alphabet=alphabet,
        transitions=transitions,
        start_state=start_state,
        accept_states=accept_states
    )
    
    return nfa

def print_dfa_formal_description(dfa):
    print("\033[94mDFA Formal Description:\033[0m")

    # print in orange color
    print("\033[38;2;255;165;0m")

    print("Q (States):", set(map(lambda x: DFA.frozen_set_to_str(x), list(dfa.states))))

    print("Σ (Alphabet):", dfa.alphabet)

    print("δ (Transitions):")
    for state, transitions in dfa.transitions.items():
        for symbol, target in transitions.items():
            print(f"    δ({DFA.frozen_set_to_str(state)}, '{symbol}') -> {DFA.frozen_set_to_str(target)}")

    print("q0 (Start State):", DFA.frozen_set_to_str(dfa.start_state))

    print("F (Accept States):", set(map(lambda x: DFA.frozen_set_to_str(x), list(dfa.accept_states))))

    print("DFA={Q, Σ, δ, q0, F}")
    print("\033[0m")

# Print DFA description in simulator-friendly format and save it in a file
def print_dfa_description(dfa):
    state_str = lambda x: DFA.frozen_set_to_str(x)
    # print("#states")
    # for state in sorted(dfa.states, key=state_str):
    #     print(state_str(state))

    # print("#initial")
    # print(state_str(dfa.start_state))

    # print("#accepting")
    # for accept_state in sorted(dfa.accept_states, key=state_str):
    #     print(state_str(accept_state))

    # print("#alphabet")
    # for symbol in sorted(dfa.alphabet):
    #     print(symbol)

    # print("#transitions")
    # for state, transitions in dfa.transitions.items():
    #     for symbol, target in transitions.items():
    #         print(f"{state_str(state)}:{symbol}>{state_str(target)}")
    string = ""
    print("DFA Description (simulator-friendly):", end="\n\n")
    string += "#states\n"
    for state in sorted(dfa.states, key=state_str):
        string += state_str(state) + "\n"

    string += "\n#initial\n"
    string += state_str(dfa.start_state) + "\n"

    string += "\n#accepting\n"
    for accept_state in sorted(dfa.accept_states, key=state_str):
        string += state_str(accept_state) + "\n"

    string += "\n#alphabet\n"
    for symbol in sorted(dfa.alphabet):
        string += symbol + "\n"

    string += "\n#transitions\n"
    for state, transitions in dfa.transitions.items():
        for symbol, target in transitions.items():
            string += f"{state_str(state)}:{symbol}>{state_str(target)}\n"
    print(string)
    with open("dfa_description.txt", "w") as f:
        f.write(string)



def display_image(window, image_path, title):
    img = Image.open(image_path)
    img = ImageTk.PhotoImage(img)

    label = tk.Label(window, image=img)
    label.image = img
    label.pack()

    title_label = tk.Label(window, text=title, font=("Helvetica", 16))
    title_label.pack()

def GUI_images(nfa_image_path, dfa_image_path):
    root = tk.Tk()
    root.title("NFA to DFA")

    display_image(root, nfa_image_path+'.png', "NFA")

    space_label = tk.Label(root, text="", height=1)
    space_label.pack()

    display_image(root, dfa_image_path+'.png', "DFA")

    root.mainloop()
