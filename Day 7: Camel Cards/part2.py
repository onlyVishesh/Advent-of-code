with open('Day 7: Camel Cards/test cases.txt', 'r') as file:
    input = [line.strip() for line in file]

for i in range(len(input)):
    input[i] = input[i].split()

def handPriority(card):
    '''
    finding hand priority of each case
    pair of 5 -> 7
    pair of 4 -> 6
    full house -> 6
    pair of 3 -> 4
    2 pair of 2 -> 3
    1 pair of 2 -> 2
    no pair -> 1
    '''
    sameCard = 0
    for i in range(len(card)):
        count = 0
        # counting no. of same card
        for j in range(len(card)):
            # checking if card are same or J 
            if(card[i] == card[j] or card[j] == "J" ):
                count+=1
        if(sameCard<count):
            sameCard=count

    if(sameCard == 1):
        return sameCard
    
    elif(sameCard==2):
        cardList = [i for i in card]

        for i in range(len(card)):
            for j in range(len(card)):
                if(i == j):
                    continue
                elif(card[i] == card[j]):
                    cardList.remove(card[i])
        
        # removing J to check true priority
        if("J" in cardList):
            cardList.remove("J")
        # if 2 pair of 2 return 3 else 2 ie 1 pair of 2
        return 3 if len(cardList) == 1 else 2
    
    elif(sameCard==3):
        cardList = [i for i in card]

        for i in range(len(card)):
            for j in range(len(card)):
                if(i == j):
                    continue
                elif(card[i] == card[j]):
                    cardList.remove(card[i])
                    break
        # removing J to check true priority
        if("J" in cardList):
            cardList.remove("J")
        # full house return 5 else 4 ie pair of 3
        return 5 if len(cardList) == 0 else 4 
    
    else:
        return sameCard+2
    
# print(handPriority("AABXX"))

# converting each hand into no. based on their priority
def cardPriority(card):
    priority = {"A": "12", 
                "K": "11", 
                "Q": "10", 
                "T": "09", 
                "9": "08", 
                "8": "07", 
                "7": "06",
                "6": "05",
                "5": "04",
                "4": "03",
                "3": "02",
                "2": "01",
                "J": "00" #making j weakest valued card
              }

    return f"{priority[card[0]]}{priority[card[1]]}{priority[card[2]]}{priority[card[3]]}{priority[card[4]]}"
    
# Calculating final priority no. ie handPriority + cardPriority
def finalPriority(card):
    return int(f"{handPriority(card)}{cardPriority(card)}")


# Sorting based on their total priority no. 
def sort(arr):
    n = len(arr)
    swapped = False
    for i in range(n-1):
        for j in range(0,n-i-1):
            if finalPriority(arr[j][0]) > finalPriority(arr[j+1][0]):
                swapped = True
                arr[j], arr[j+1] = arr[j+1], arr[j]

    if not swapped:
        return

sort(input)

count = 0
for i in range(len(input)):
    # print(handPriority(input[i][0]),input[i][0],cardPriority(input[i][0]),input[i][1],i+1)
    count += int(input[i][1])*(i+1)

print(count)