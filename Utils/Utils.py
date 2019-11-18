# Utilities
def lists_have_same_elems_in_order(first, second):
        if len(first) != len(second):
            return False
        else:
            for i in range(len(first)):
                if first[i] != second[i]:
                  return False
            return True
