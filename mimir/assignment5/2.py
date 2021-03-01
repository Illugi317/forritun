'''
Design an algorithm that generates the first n numbers in the following sequence:; 1, 2, 3, 6, 11, 20, 37, ___, ___, ___, …
Make sure that you write up the algorithm before starting to code.
Then implement the algorithm in Python. Put your algorihmic description as a comment in the program file.

During the design of your algorithm and your implementation, you should use git:

    Write the text of your algorithm in a file called sequence.py
    Inspect the result of git status
    Use git add . to move changes to the staging area.
    Commit your changes with git commit -m “Algorithm written for sequence”
    Then start implementing your algorithm
    During your implementation, make sure you do git status, git add, and git commit regularily.
    You can see a log of all your commits with git log.
    When you have finished your implementation:
        Push your changes to the remote repo with: git push
        Inspect your commits on github


'''

'''
    tek in input frá notanda um hversu marga tölur

    geri lista til að halda utan um þrjár seinustu tölur

    geri for lykkju sem keyrir eins oft og inputtið
        plúsa tölurnar í listanum til að fá núverandi tölu
        prenti út töluna

        bæti tölunni við og hendi út fyrst stakinu úr listanum

'''

n = int(input("Enter the length of the sequence: ")) # Do not change this line

num_list = [0, 1 ,2]

# prenta út initialized tölurnar
print(num_list[1])
print(num_list[2])

for a in range(n -2):
    curr_num = sum(num_list)
    print(curr_num)

    num_list.append(curr_num)
    num_list.remove(num_list[0])