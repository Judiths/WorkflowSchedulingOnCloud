class ParetoAlgorithm(object):
    @staticmethod
    def get_pareto_result(pareto_list):
        new_pareto_list = list()

        if pareto_list is not None:
            i = 0
            while i < len(pareto_list):
                defeat = False
                j = 0
                while j < len(pareto_list):
                    if i != j:
                        if (pareto_list[j].makespan <= pareto_list[i].makespan and pareto_list[j].cost < pareto_list[i].cost) \
                                or (pareto_list[j].cost <= pareto_list[i].cost and pareto_list[j].makespan < pareto_list[i].makespan):
                            defeat = True
                            break
                    j += 1
                if defeat is False:
                    new_pareto_list.append(pareto_list[i])
                i += 1
        return new_pareto_list

    @staticmethod
    def get_pareto_result_with_restraint(pareto_list, rel_restraint):
        new_pareto_list = list()

        if pareto_list is not None:
            i = 0
            while i < len(pareto_list):
                defeat = False
                j = 0
                while j < len(pareto_list):
                    if i != j:
                        if (pareto_list[j].makespan <= pareto_list[i].makespan and pareto_list[j].cost < pareto_list[
                            i].cost) \
                                or (pareto_list[j].cost <= pareto_list[i].cost and pareto_list[j].makespan <
                                    pareto_list[i].makespan):
                            defeat = True
                            break
                    j += 1
                if defeat is False and pareto_list[i].reliability >= rel_restraint:
                    new_pareto_list.append(pareto_list[i])
                i += 1
        return new_pareto_list
