import csv
import variables

def writing_final_data (final_data, number_times_full_grid):
    name = "density_".strip()+str(variables.repeticao_atual).strip()+"_sem_transferencia_transconjugantes_data_times_full_grid".strip()+str(number_times_full_grid).strip()+"remaining_proportion".strip()+str(variables.remaining_proportion_grid).strip()+"teta_one".strip()+str(variables.teta_1).strip()+"initial_plasmid_cost".strip()+str(variables.initial_plasmid_cost).strip()+"permanent_plasmid_cost".strip()+str(variables.permanent_plasmid_cost).strip()+"adaptation_time".strip()+str(variables.adaptation_time).strip()+"conjugation_rate".strip()+str(variables.maximum_conjugation_rate).strip()+"D_R".strip()+str(variables.donor_bacteria).strip()+"_".strip()+str(variables.number_plasmid_free_bacteria).strip()+".csv".strip()
    with open(name, 'w', newline='') as csvfile:
        file = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        file.writerow(["recipients".strip()+','.strip()+ "donors".strip()+','.strip()+ "transconjugants".strip()+','.strip()+ "segregadas".strip()+','.strip()+ "adaptations_number".strip()+','.strip()+ "cycle".strip()])
        for each_line in range(0, len(final_data)):
            file.writerow([str(final_data[each_line][0]).strip()+','.strip()+str(final_data[each_line][1]).strip()+','.strip()+str(final_data[each_line][2]).strip()+','.strip()+str(final_data[each_line][3]).strip()+','.strip()+str(final_data[each_line][4]).strip()+','.strip()+str(final_data[each_line][5]).strip()])

def writing_conjugation_data (conjugation_data, number_times_full_grid):
    name = "conjugation_".strip()+str(variables.repeticao_atual).strip()+"_sem_transferencia_transconjugantes_data_times_full_grid_".strip()+str(number_times_full_grid).strip()+"remaining_proportion".strip()+str(variables.remaining_proportion_grid).strip()+"teta_one".strip()+str(variables.teta_1).strip()+"initial_plasmid_cost".strip()+str(variables.initial_plasmid_cost).strip()+"permanent_plasmid_cost".strip()+str(variables.permanent_plasmid_cost).strip()+"adaptation_time".strip()+str(variables.adaptation_time).strip()+"conjugation_rate".strip()+str(variables.maximum_conjugation_rate).strip()+"D_R".strip()+str(variables.donor_bacteria).strip()+"_".strip()+str(variables.number_plasmid_free_bacteria).strip()+".csv".strip()
    with open(name, 'w', newline='') as csvfile:
        file = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        file.writerow(["attempts".strip()+','.strip()+ "conjugation_events".strip()+','.strip()+"cycle".strip()])
        for each_line in range(0, len(conjugation_data)):
            file.writerow([str(conjugation_data[each_line][0]).strip()+','.strip()+str(conjugation_data[each_line][1]).strip()+','.strip()+str(conjugation_data[each_line][2]).strip()])

def positions (lista,number_times_full_grid):
    name = "positions_".strip()+str(variables.repeticao_atual).strip()+"_sem_transferencia_transconjugantes_data_times_full_grid_".strip()+str(number_times_full_grid).strip()+"remaining_proportion".strip()+str(variables.remaining_proportion_grid).strip()+"teta_one".strip()+str(variables.teta_1).strip()+"initial_plasmid_cost".strip()+str(variables.initial_plasmid_cost).strip()+"permanent_plasmid_cost".strip()+str(variables.permanent_plasmid_cost).strip()+"adaptation_time".strip()+str(variables.adaptation_time).strip()+"conjugation_rate".strip()+str(variables.maximum_conjugation_rate).strip()+"D_R".strip()+str(variables.donor_bacteria).strip()+"_".strip()+str(variables.number_plasmid_free_bacteria).strip()+".csv".strip()
    with open(name, 'w', newline='') as csvfile:
        file = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        file.writerow(["x".strip()+','.strip()+ "y".strip()+','.strip()+"tipo".strip()+','.strip()+"custo".strip()+','.strip()+"viz_prox".strip()+','.strip()+"viz_longe".strip()+','.strip()+"tempo_adapt".strip()])
        for each_x in range(len(lista)):
            for each_y in range(len(lista[0])):
                file.writerow([str(lista[each_x][each_y][0]).strip()+','.strip()+str(lista[each_x][each_y][1]).strip()+','.strip()+str(lista[each_x][each_y][2]).strip()+','.strip()+str(lista[each_x][each_y][3]).strip()+','.strip()+str(lista[each_x][each_y][4]).strip()+','.strip()+str(lista[each_x][each_y][5]).strip()+','.strip()+str(lista[each_x][each_y][6]).strip()])



