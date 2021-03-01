def get_votes(vote_dict:dict):
    ''' Get the name and votes from the user, check if the input is legal by using the try: except statement. If the input is not legal try again,
    if the input is blank("") then quit the loop.'''
    inputs = "placeholder"
    while inputs != "":
        inputs = input("Candidate and votes: ")
        if inputs == "":
            continue
        name_and_vote = inputs.split(" ")
        name = name_and_vote[0].lower()
        try:
            votes = int(name_and_vote[1])
        except (ValueError,IndexError):
            print("Invalid no. of votes!")
            continue
        add_vote(vote_dict,name,votes)

def add_vote(vote_dict,name,votes):
    ''' Add the vote to the name, check if the name is in the dict if not create it and add the votes to the value,
    if the name already exists add the votes to the current amount of votes '''
    if name not in vote_dict:
        vote_dict[name] = votes
    else:
        vote_dict[name] += votes

def print_dict(vote_dict):
    ''' Print the dictionary in alphabetical order '''
    for key,value in sorted(vote_dict.items()):
        print(f"{key}: {value}")

def get_total_votes(vote_dict):
    ''' Get the total amount of votes by adding all the values together '''
    return sum(vote_dict.values())

def main():
    ''' Create the dictionary and call the corresponding functions '''
    vote_dict = {}
    get_votes(vote_dict)
    print_dict(vote_dict)
    print(f"Total no. of votes: {get_total_votes(vote_dict)}")

main()