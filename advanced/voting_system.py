class VotingSystem:
    def __init__(self):
        self.candidates = {}  # stores candidates and their votes
        self.total_votes = 0  # tracks total number of votes

    def add_candidate(self, name):
        # Adds a new candidate to the voting system
        self.candidates[name] = 0

    def cast_vote(self, candidate_name):
        # Cast a vote for a candidate if valid
        if candidate_name in self.candidates:
            self.candidates[candidate_name] += 1
            self.total_votes += 1
            print(f"Vote casted for {candidate_name}")
        else:
            print("Invalid candidate. Vote not counted.")

    def display_results(self):
        #Display the voting results
        if self.total_votes == 0:
            print("No votes cast yet.")
            return
        
        print("\nElection Results:")
        for candidate, votes in self.candidates.items():
            print(f"{candidate}: {votes} votes")

        # Determine the winner
        winner = max(self.candidates, key=self.candidates.get)
        print(f"\nThe winner is: {winner} with {self.candidates[winner]} votes!")

    def get_total_votes(self):
        # Returns the total number of votes cast
        return self.total_votes

def main():
    print("Welcome to the Online Voting System!\n")

    # Create the voting system
    voting_system = VotingSystem()

    # Add candidate's name
    store_candidate_name = [] # stores candidate's name temporarily
    count = 0
    while True:
        try:
            limit = int(input("How many candidates would you like to register: "))
            if limit <= 0:
                print("Number of candidates must be greater than 0.")
                return
            
            while count < limit:
                candidate_name = input("Enter candidate name: ").strip().lower().capitalize()
                if candidate_name:
                    if candidate_name in store_candidate_name:
                        print("Candidate names cannot be the same.")
                        continue
                    
                    store_candidate_name.append(candidate_name)
                    for index in store_candidate_name:
                        voting_system.add_candidate(store_candidate_name[-1])
                    #print(store_candidate_name)
                count += 1
            if count == limit:
                break
        except ValueError:
            print("Please enter a number.")

    # Simulate voting
    while True:
        
        print("\nAvailable candidates:")
        for idx, candidate in enumerate(voting_system.candidates, start=1):
            print(f"{idx}. {candidate}")
        print("\nPlease ensure you start with capital letters when typing name of candidate.\n")
        
        voter_name = input("Enter your name to vote (or type 'exit' to finish voting): ")
        if voter_name.lower() == "exit":
            break

        vote = input(f"Hello {voter_name}, please vote by typing the candidate name: ").strip()
        voting_system.cast_vote(vote)

    # Display the results
    voting_system.display_results()

if __name__ == "__main__":
    main()