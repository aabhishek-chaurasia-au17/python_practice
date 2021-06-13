
# Python | Remove empty tuples from a list

"""
Input : tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'), ('krishna', 'akbar', '45'), ('',''),()]
Output : [('ram', '15', '8'), ('laxman', 'sita'), ('krishna', 'akbar', '45'), ('', '')]

Input : tuples = [('','','8'), (), ('0', '00', '000'), ('birbal', '', '45'), (''), (),  ('',''),()]
Output : [('', '', '8'), ('0', '00', '000'), ('birbal', '', '45'), ('', '')]
"""

def Remove_tuples(tuples):

    tuples2 = []   

    for i in tuples:
        if i != ():
            # print(i, end=" ")
            tuples2.append(tuples)
    return tuples2
            


if __name__=="__main__":

    tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'), ('krishna', 'akbar', '45'), ('',''),()]
    
    print(Remove_tuples(tuples))