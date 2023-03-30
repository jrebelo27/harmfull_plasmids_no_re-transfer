import functions
import random
import variables

def initial_bacteria(list_spaces):
    filled_spaces = []    
    grid_area = variables.grid_edge*variables.grid_edge
    while len(filled_spaces) < (variables.number_plasmid_free_bacteria+variables.donor_bacteria):
        position = [random.sample(range(variables.grid_edge),1)[0],random.sample(range(variables.grid_edge),1)[0]]
        if position not in filled_spaces:
            filled_spaces.append(position)
    donor_bacteria = filled_spaces[:variables.donor_bacteria]
    plasmid_free_bacteria = filled_spaces[variables.donor_bacteria:]    
    for each_plasmid_free_bacterium in plasmid_free_bacteria:
        list_spaces[each_plasmid_free_bacterium[0]][each_plasmid_free_bacterium[1]][2] = 1
        list_spaces[each_plasmid_free_bacterium[0]][each_plasmid_free_bacterium[1]][3] = 0
        list_spaces[each_plasmid_free_bacterium[0]][each_plasmid_free_bacterium[1]][4] = []
        list_spaces[each_plasmid_free_bacterium[0]][each_plasmid_free_bacterium[1]][5] = []
    for each_donor_bacterium in donor_bacteria:
        list_spaces[each_donor_bacterium[0]][each_donor_bacterium[1]][2] = 2
        list_spaces[each_donor_bacterium[0]][each_donor_bacterium[1]][3] = variables.permanent_plasmid_cost
        list_spaces[each_donor_bacterium[0]][each_donor_bacterium[1]][4] = []
        list_spaces[each_donor_bacterium[0]][each_donor_bacterium[1]][5] = []
    for each_bacterium in filled_spaces:
        list_spaces[each_bacterium[0]][each_bacterium[1]][4] = functions.inital_local_neighbourhood(each_bacterium[0], each_bacterium[1], list_spaces)
        list_spaces[each_bacterium[0]][each_bacterium[1]][5] = functions.inital_nutrient_neighbourhood(each_bacterium[0], each_bacterium[1], list_spaces)
    return [list_spaces, filled_spaces]
            
