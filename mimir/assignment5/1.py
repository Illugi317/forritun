'''
program file.

During the design of your algorithm and your implementation, you should use git:

    Initialize a local directory with git init.
    Write the text of your algorithm in a file called max_int.py
    Inspect the result of git status
    Use git add . to move changes to the staging area.
    Commit your changes with git commit -m “Algorithm written for max_int”
    Then start implementing your algorithm
    During your implementation, make sure you do git status, git add, and git commit regularly.
    You can see a log of all your commits with git log.
    When you have finished your implementation:
        Create an account on github.com (if you don't already have it).
        Create a public repository on github
        Follow the instructions (that appear on github when you have created a new repository)
            under "push an existing repository from the command line"  (see also here)
        Push your changes to the remote repo with: git push
        Inspect your commits on github
'''


'''
    while lykkja
        input frá notenda sett inn í lista

        endar while lykkju ef tala er neikvæð

    Kíkja á lista eftir for lykkju og finna stærstu töluna með max fallinu

'''

number_list = []
num_int = 0
while num_int >= 0:
    num_int = int(input("Input a number: "))    # Do not change this line
    # Fill in the missing code
    number_list.append(num_int)

print("The maximum is", max(number_list))    # Do not change this line
