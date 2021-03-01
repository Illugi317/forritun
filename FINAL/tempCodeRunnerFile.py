def get_votes(vote_dict:dict):
    inputs = "placeholder"
    while inputs != "":
        inputs = input("Candidate and votes: ")
        if inputs == "":
            continue
        name_and_vote = inputs.split(" ")
        name = name_and_vote[0].lower()
        try:
            votes = int(name_and_vote[1])
        except ValueError:
            print("Invalid no. of votes!")
            continue
        if name not in vote_dict:
            vote_dict[name] = votes
        else:
            vote_dict[name] += votes

def print_dict(vote_dict):
    for key,value in sorted(vote_dict.items()):
        print(f"{key}: {value}")

def get_total_votes(vote_dict):
    summa = 0
    for value in vote_dict.values():
        summa += value
    return summa

def main():
    vote_dict = {}
    get_votes(vote_dict)
    print_dict(vote_dict)
    print(f"Total no. of votes: {get_total_votes(vote_dict)}")

main()