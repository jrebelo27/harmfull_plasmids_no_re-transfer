import random
import variables
import functions
import files_writing
import time
import numpy

def cycles (list_spaces, filled_spaces):
    duplications = 0
    final_data = []
    conjugation_data = []
    grid_area = variables.grid_edge*variables.grid_edge    
    number_times_full_grid = 0
    each_cycle = 0
    counter = 0
    number_conjugation_attempts = 0
    number_conjugations = 0
    inicio = time.time()
    while number_times_full_grid <= 1073:        
        each_cycle += 1
        position_focal_bacteria = random.sample(filled_spaces, 1)[0]        
        focal_bacteria = list_spaces[position_focal_bacteria[0]][position_focal_bacteria[1]]
        x_position = focal_bacteria[0]
        y_position = focal_bacteria[1]
        #check the amount of nutrients; that is, how many empty spaces
        number_empty_spaces = focal_bacteria[5].count(0)
        #grid of 7x7, so at most there can only be 49 empty spaces 
        c = number_empty_spaces/49        
        if c > 0:
            #bacterial growth
            growth_rate = variables.maximum_growth_rate-focal_bacteria[3]
            growth_probability = functions.growth_rate_function(growth_rate, c)
            if random.random() <= growth_probability:
                list_spaces, filled_spaces = functions.bacterial_growth(focal_bacteria, list_spaces, filled_spaces)
            #conjugation            
            if focal_bacteria[2] == 2:                
                bacteria_neighbourhood = focal_bacteria[4]
                recipient_positions = [i for i in range(len(bacteria_neighbourhood)) if (bacteria_neighbourhood[i] == 1 or bacteria_neighbourhood[i] == 4 or bacteria_neighbourhood[i] == 5 or bacteria_neighbourhood[i] == 6)]
                if len(recipient_positions) > 0:
                    number_conjugation_attempts += 1
                    conjugation_probability = functions.conjugation_rate_function(c)
                    if random.random() <= conjugation_probability:
                        number_conjugations += 1
                        bacterium_to_conjugate = random.sample(recipient_positions, 1)[0]                            
                        new_x = (focal_bacteria[0]+variables.decoder[bacterium_to_conjugate][0])%variables.grid_edge
                        new_y = (focal_bacteria[1]+variables.decoder[bacterium_to_conjugate][1])%variables.grid_edge
                        list_spaces = functions.conjugation([new_x, new_y], list_spaces)  
            if len(filled_spaces)/grid_area >= variables.maximum_proportion_full_grid:            
                counter = 0
                number_times_full_grid += 1
                print(number_times_full_grid)
                conjugation_data.append([number_conjugation_attempts, number_conjugations, number_times_full_grid])
                number_conjugation_attempts = 0
                number_conjugations = 0
                recipients = 0
                donors = 0
                transconjugants = 0
                segregants = 0
                for each_x_space in range(len(list_spaces)):
                    for each_y_space in range(len(list_spaces[0])):
                        if list_spaces[each_x_space][each_y_space][2] == 1:
                            recipients += 1
                        elif list_spaces[each_x_space][each_y_space][2] == 2:
                            donors+= 1
                        elif list_spaces[each_x_space][each_y_space][2] == 3:
                            transconjugants += 1
                        elif list_spaces[each_x_space][each_y_space][2] == 4 or list_spaces[each_x_space][each_y_space][2] == 5 or list_spaces[each_x_space][each_y_space][2] == 6:
                            segregants += 1  
                final_data.append([recipients, donors, transconjugants,segregants,variables.number_adaptations, each_cycle])        
                random.shuffle(filled_spaces)
                number_to_eliminate = int((variables.maximum_proportion_full_grid - variables.remaining_proportion_grid)*grid_area)
                spaces_to_eliminate = filled_spaces[0:number_to_eliminate]
                filled_spaces = filled_spaces[number_to_eliminate:len(filled_spaces)]
                for each_space in range(len(spaces_to_eliminate)):     
                    x_position = spaces_to_eliminate[each_space][0]
                    y_position = spaces_to_eliminate[each_space][1]
                    list_spaces[x_position][y_position] = [x_position, y_position,0,0,[],[],0]
                    index_bacterium = -1
                    for each_x in [-1,0,1]:
                        for each_y in [-1,0,1]:
                            new_x = (x_position+each_x)%variables.grid_edge
                            new_y = (y_position+each_y)%variables.grid_edge
                            if list_spaces[new_x][new_y][2] != 0:
                                list_spaces[new_x][new_y][4][index_bacterium] = 0
                            index_bacterium -= 1
                    index_bacterium = -1
                    for each_x in range(-3,4):
                        for each_y in range(-3,4):
                            new_x = (x_position+each_x)%variables.grid_edge
                            new_y = (y_position+each_y)%variables.grid_edge
                            if list_spaces[new_x][new_y][2] != 0:
                                list_spaces[new_x][new_y][5][index_bacterium] = 0
                            index_bacterium -= 1
                if (recipients+segregants) == 950000 or (donors+segregants) == 950000 or (transconjugants+segregants) == 950000:
                    files_writing.writing_final_data(final_data, number_times_full_grid)
                    number_times_full_grid = 1074
                if number_times_full_grid%500 == 0:                
                    files_writing.writing_final_data(final_data, number_times_full_grid)
    #files_writing.writing_conjugation_data(conjugation_data, number_times_full_grid)
    files_writing.writing_final_data(final_data, number_times_full_grid)
    files_writing.positions(list_spaces, number_times_full_grid)
