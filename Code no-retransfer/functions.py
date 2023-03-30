import random
import variables
import math


def initial_positions():
    initial_positions = []
    for each_x in range(variables.grid_edge):
        x_positions = []
        for each_y in range(variables.grid_edge):
            x_positions.append([each_x, each_y, 0, 0,[],[],0])

        initial_positions.append(x_positions)    
    
    return initial_positions


def inital_local_neighbourhood(x_position, y_position, list_spaces):
    #Obtain the positions in which there can be a conjugation event
    neighbours_type = []
    for each_x in [-1,0,1]:
        for each_y in [-1,0,1]:
            new_x = (x_position+each_x)%variables.grid_edge
            new_y = (y_position+each_y)%variables.grid_edge
            type_this_neighbour = list_spaces[new_x][new_y][2]
            neighbours_type.append(type_this_neighbour)
    return neighbours_type

def inital_nutrient_neighbourhood(x_position, y_position, list_spaces):    
    neighbours_type = []
    for each_x in range(-3,4):
        for each_y in range(-3,4):
            new_x = (x_position+each_x)%variables.grid_edge
            new_y = (y_position+each_y)%variables.grid_edge
            type_this_neighbour = list_spaces[new_x][new_y][2]
            neighbours_type.append(type_this_neighbour)
    return neighbours_type

def growth_rate_function(maximum_growth_rate, c):
    if c >= variables.teta:
        growth_probability = maximum_growth_rate
    else:
        growth_probability = maximum_growth_rate*(c/variables.teta)
    return growth_probability

def function_local_neighbourhood(x_position, y_position, list_spaces, bacterium_type):
    #Obtain the positions in which there can be a conjugation event
    neighbours_type = []
    bacterium_index = -1
    for each_x in [-1,0,1]:
        for each_y in [-1,0,1]:
            new_x = (x_position+each_x)%variables.grid_edge
            new_y = (y_position+each_y)%variables.grid_edge
            type_this_neighbour = list_spaces[new_x][new_y][2]
            if each_x == 0 and each_y == 0:
                type_this_neighbour = bacterium_type
            neighbours_type.append(type_this_neighbour)
            if list_spaces[new_x][new_y][2] != 0:
                list_spaces[new_x][new_y][4][bacterium_index] = bacterium_type
            bacterium_index -= 1
    return [neighbours_type,list_spaces]

def function_nutrient_neighbourhood(x_position, y_position, list_spaces, bacterium_type):
    #Obtain the positions in which there can be a conjugation event
    neighbours_type = []
    bacterium_index = -1
    for each_x in range(-3,4):
        for each_y in range(-3,4):
            new_x = (x_position+each_x)%variables.grid_edge
            new_y = (y_position+each_y)%variables.grid_edge
            type_this_neighbour = list_spaces[new_x][new_y][2]
            if each_x == 0 and each_y == 0:
                type_this_neighbour = bacterium_type
            neighbours_type.append(type_this_neighbour)
            if list_spaces[new_x][new_y][2] != 0:
                try:
                    list_spaces[new_x][new_y][5][bacterium_index] = bacterium_type
                except:
                    print(list_spaces[new_x][new_y][5])
                    print(list_spaces[new_x][new_y][2])
            bacterium_index -= 1
    return [neighbours_type,list_spaces]

def bacterial_growth (focal_bacterium, list_spaces, filled_spaces):    
    
    positions_local_neighbourhood = focal_bacterium[4]    
    empty_positions = [i for i in range(len(positions_local_neighbourhood)) if positions_local_neighbourhood[i] == 0]

    if len(empty_positions) > 0:
        chosen_position = random.sample(empty_positions, 1)[0]        
        new_x = (focal_bacterium[0]+variables.decoder[chosen_position][0])%variables.grid_edge
        new_y = (focal_bacterium[1]+variables.decoder[chosen_position][1])%variables.grid_edge

        filled_spaces.append([new_x, new_y])
        final_type = focal_bacterium[2]
        if focal_bacterium[2] == 1 or focal_bacterium[2] == 4 or focal_bacterium[2] == 5 or focal_bacterium[2] == 6:
            cost = 0
        if focal_bacterium[2] == 2:
            cost = focal_bacterium[3]
        decreased_time = 0   
        if focal_bacterium[2] == 3:
            if focal_bacterium[6] != 0:
                decreased_time = focal_bacterium[6] - 1
                if decreased_time == 0:
                    cost = variables.permanent_plasmid_cost
                    variables.adaptations_number += 1
                else:
                   cost = focal_bacterium[3] 
            else:
                cost = focal_bacterium[3]
                
        if final_type == 2:
            if random.random() <= 10**-3:
                final_type = 6

        if final_type == 3:
            if random.random() <= 10**-3:
                if decreased_time == 0:
                    final_type = 4
                else:
                    final_type = 5
                    decreased_time = variables.adaptation_time                    

        
                    
        local_neighbours_type, list_spaces = function_local_neighbourhood(new_x, new_y, list_spaces, final_type)
        type_nutrient_neighbourhood, list_spaces = function_nutrient_neighbourhood(new_x, new_y, list_spaces, final_type)
        list_spaces[focal_bacterium[0]][focal_bacterium[1]][3] = cost
        list_spaces[focal_bacterium[0]][focal_bacterium[1]][6] = decreased_time

        if final_type == 4 and final_type == 5 and final_type == 6:
            cost = 0
        
        list_spaces[new_x][new_y] = [new_x, new_y, final_type, cost, local_neighbours_type, type_nutrient_neighbourhood, decreased_time]



    return [list_spaces, filled_spaces]

def conjugation_rate_function(c):
    if c >= variables.teta_2:
        conjugation_probability = variables.maximum_conjugation_rate
    elif c < variables.teta_1:
        conjugation_probability = 0
    else:
        conjugation_probability = variables.maximum_conjugation_rate*((c-variables.teta_1)/(variables.teta_2-variables.teta_1))
    return conjugation_probability

def conjugation(bacterium_to_conjugate, list_spaces):
    variables.recipient_bacteria -= 1
    tipo_recetora = list_spaces[bacterium_to_conjugate[0]][bacterium_to_conjugate[1]][2]
    
    if tipo_recetora == 4:
        list_spaces[bacterium_to_conjugate[0]][bacterium_to_conjugate[1]][2] = 3
        list_spaces[bacterium_to_conjugate[0]][bacterium_to_conjugate[1]][3] = variables.permanent_plasmid_cost
        list_spaces[bacterium_to_conjugate[0]][bacterium_to_conjugate[1]][6] = 0

    elif tipo_recetora == 6:
        list_spaces[bacterium_to_conjugate[0]][bacterium_to_conjugate[1]][2] = 2
        list_spaces[bacterium_to_conjugate[0]][bacterium_to_conjugate[1]][3] = variables.permanent_plasmid_cost
        list_spaces[bacterium_to_conjugate[0]][bacterium_to_conjugate[1]][6] = 0
    else:
        list_spaces[bacterium_to_conjugate[0]][bacterium_to_conjugate[1]][2] = 3
        list_spaces[bacterium_to_conjugate[0]][bacterium_to_conjugate[1]][3] = variables.initial_plasmid_cost
        list_spaces[bacterium_to_conjugate[0]][bacterium_to_conjugate[1]][6] = variables.adaptation_time
        
    return list_spaces





































    

