from visual_automata.fa.dfa import VisualDFA
from lib.utils import input_NFA, GUI_images
import tkinter as tk

NFA_image_name = 'NFA'
DFA_image_name = 'DFA'

ans = ''
while ans not in ['y', 'n']:
    print("Do you want to enter NFA manually or use the default NFA? (y:enter/n:default): ", end="")
    ans = input()

if ans == 'y':
    nfa = input_NFA()
else:
    from lib.default_nfa import default_nfa
    nfa = default_nfa

nfa.to_automathonNFA().view(NFA_image_name)

dfa = nfa.to_DFA().to_visualDFA()

# Print DFA table in green color
print("DFA table:"+'\033[32m')
print(dfa.table)
print('\033[0m')

dfa.show_diagram(filename=DFA_image_name)

GUI_images(NFA_image_name+'.gv', DFA_image_name)