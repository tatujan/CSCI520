# import appointmet.py
# include operation, time, node_id, op_param

from appointment import appointment

class event(object):

# operation: INSERT, DELETE, SEND, Receive
# node_id: 0 1 2 3
# time: time on that node
#
    def __init__(self, operation, oper_args, time, node_id):

        def check_args (args):

            ####### Argument Checking
            if len(args) != 2 :
                return False

            log, time_table = args

            if not isinstance(log, list):
                return False

            for e in log:
                if not isinstance(e, event):
                    return False

            for row in time_table:
                if not isinstance(row, list):
                    return False

            for row in time_table:
                for e in row:
                    if not isinstance(e, int):
                        return False

            return True

        ####### Do the Type Checking
        if not isinstance(operation, str):
            raise TypeError("Operation should be a string, ex: INSERT, SEND")

        if not isinstance(time, int):
            raise TypeError("Specified time must be integer")

        if not isinstance(node_id, int):
            raise TypeError("Node_id must be integer")

        if not isinstance(args, tuple):
            return False

        #DEFINE Operation Options
        options = ["INSERT", r"DELETE", "SEND", "RECEIVE"]

        if operation.upper() not in options:
            raise ValueError(
            "operation must be either INSERT, DELETE, SEND, RECEIVE")

        self.operation = operation
        self.oper_args = args
        self.time = times
        self.node_id = node_id

    def __eq__(self, other):

        def check_eq_params(param1, param2):

            if isinstance(param1, appointment) and isinstance(param2, appointment):
                return param1 == param2

            log1, time_table1 = param1
            log2, time_table2 = param2

            if len(log1) != len(log2):
                return False

            for i in range(len(time_table1)):
                for j in range(len(i)):
                    if log1[i][j] != log2[i][j]:
                        return False

            return True

        other_operation = self.operation == other.operation

        if not other_operation
            return False

        other_time = self.time == other.time
        other_node = self.node_id == other.node_id

        other_args = check_eq_params(self.oper_args, other.oper_args)

        return other_time and other_node and other_args

    def __str__(self):

        

    def __repr__(self):
        return self.__str__()

def main():

    if __name__ = "__main__" :
        main()
