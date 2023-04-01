import variables
import cycles
import bacteria_distribution
import files_writing
import functions

quantity_donors = [9900]*18+[5000]*18+[100]*18+[10]*18+[9900]*18+[5000]*18+[100]*18+[10]*18
quantity_recipients = [100]*18+[5000]*18+[9900]*18+[9990]*18+[100]*18+[5000]*18+[9900]*18+[9990]*18
adaptation_time_list = [70]*72+[400]*72
plasmid_cost_list = [0.2,0.4,0.6]*48
permanent_plasmid_cost_list = ([0]*3+[0.1]*3)*24
conjugation_rate_list = ([0.01]*6+[0.1]*6+[1]*6)*8
teta_one_list = [0.2]*144

for cada_rep in [1,2,3]:
    for each_quantity in range(0,144):
        variables.repeticao_atual = cada_rep
        variables.donor_bacteria = quantity_donors[each_quantity]
        variables.number_plasmid_free_bacteria = quantity_recipients[each_quantity]
        variables.adaptation_time = adaptation_time_list[each_quantity]
        variables.initial_plasmid_cost = plasmid_cost_list[each_quantity]
        variables.permanent_plasmid_cost = permanent_plasmid_cost_list[each_quantity]
        variables.maximum_conjugation_rate = conjugation_rate_list[each_quantity]
        variables.teta_1 = teta_one_list[each_quantity]
        list_spaces = functions.initial_positions()
        list_spaces, filled_spaces = bacteria_distribution.initial_bacteria(list_spaces)
        final_data = cycles.cycles(list_spaces, filled_spaces)

