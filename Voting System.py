def voting_system(query, options):
    ballot = {} #An empty dictionary
    voting = True

    print('Its Voting Time!!!')
    while voting:
        print('Enter Name')
        nm = input().title()
        #Ensure that this person has not voted earlier
        if nm not in ballot.keys():
            print('Query: ', query)
            #Menu
            i = 0
            while i < len(options):
                print(i+1, ':', options[i])
                i+=1
            vote = int(input()) #vote
            if vote >=1 and vote<= len(options):
                ballot[nm] = options[vote-1] #make an entry into the dictionary
            else:
                ballot[nm] = 'WASTED' # make an entry into the dictionary
        else:
            print('ERR,', nm, 'has already voted!!!')

        print('Are there any more voters? (y/n) ')
        ch = input().lower()
        voting = (ch == 'y' or ch == 'yes')

    return ballot

def voting():

    print('Enter the issue to get votes for: ')
    query = input().capitalize()

    print('Enter Options')
    options = []
    stats = {'WASTED':0}

    take_options = True
    while take_options:
        print('Enter an option ')
        temp = input().title()
        options.append(temp)
        stats[temp] = 0

        print('Are there any more options? (y/n) ')
        ch = input().lower()
        take_options = (ch == 'y' or ch == 'yes')

    ballot_box = voting_system(query, options)

    for vote in ballot_box:
        stats[ballot_box[vote]]+=1

    print(query.center(80, '-'))
    for s in stats:
        print(s.rjust(70),':', stats[s])

voting()