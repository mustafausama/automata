from lib.utils import input_NFA, GUI_images, print_dfa_formal_description, print_dfa_description

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

# save the NFA image
nfa.to_automathonNFA().view(NFA_image_name)

dfa = nfa.to_DFA()

visualDFA = dfa.to_visualDFA()

# print the description of DFA in a formal format
print_dfa_formal_description(dfa)

# print the DFA table
print("DFA table:"+'\033[32m')
print(visualDFA.table)
print('\033[0m')

# print the description of DFA in a simulator-friendly format
print_dfa_description(dfa)

# save the DFA image
visualDFA.show_diagram(filename=DFA_image_name)

GUI_images(NFA_image_name+'.gv', DFA_image_name)