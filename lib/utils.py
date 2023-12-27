from .NFA import NFA
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
