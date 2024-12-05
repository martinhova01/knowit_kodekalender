from collections import defaultdict
import copy

def main():
    candidates = {}
    for line in open("kandidater.txt").read().rstrip().split("\n"):
        _split = line.split(" - ")
        candidates[_split[0]] = _split[1]
    
    total_seats = defaultdict(int)
    
    for line in open("stater.txt").read().rstrip().split("\n"):
        
        #parse
        _split = line.split(" - ")
        seats = int(_split[2])
        votes = {}
        for vote_candidate in  _split[3].split(", "):
            key, value = vote_candidate.split(": ")
            votes[key] = int(value)
        
        total_votes = sum(votes.values())
        exact, _floor, rest, seats_pr_candidate = {}, {}, {}, {}
        for candidate in candidates.keys():
            exact[candidate] = (votes[candidate] * seats) / total_votes
            _floor[candidate] = (votes[candidate] * seats) // total_votes
            rest[candidate] = exact[candidate] % 1
        
        seats_pr_candidate = copy.deepcopy(_floor)
        rest_seats = seats - sum(seats_pr_candidate.values())
        
        # add the last seats
        for key, value in sorted(rest.items(), key=lambda item: item[1], reverse=True)[:rest_seats]:
            seats_pr_candidate[key] += 1
        
        # add to global seats
        for candicate, seats in seats_pr_candidate.items():
            total_seats[candicate] += seats
        
    
    winner = max(total_seats.items(), key= lambda item: item[1])
    print(f"{candidates[winner[0]]} - {winner[1]}")
        

if __name__ == "__main__":
    main()