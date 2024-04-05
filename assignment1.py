import sys
# this function will check for stablity of given matching pair and returns number of pair which causing unstability.
def checkSatableMatching(n,preferenceList,matchingPair):
    matchingPairDict={}
    preferenceListPosDict={}
    unstablepair=0
    for pair in matchingPair:
        matchingPairDict[pair[0]]=pair[1]
    pos=0
    for preference in preferenceList:
        preferenceListPosDict[preference[0]]=pos
        pos+=1
#         check for swaping if possible
    for i in range(n-1):
        for j in range(i+1,n):
            # check  if b2 is present before b1 in prerence list of a1
            condition_satisfied_count=0
            # loop in prefence list of a1
            for women in preferenceList[preferenceListPosDict[matchingPair[i][0]]]:
                if(women == matchingPair[i][1]):
                    break
                if(women==matchingPair[j][1]):
                    condition_satisfied_count+=1
                    break
            # loop in prefrenece list of b1 , for unstable : a2 should come before a1
            for men in preferenceList[preferenceListPosDict[matchingPair[i][1]]]:
                if(men == matchingPair[i][0]):
                    break
                if(men==matchingPair[j][0]):
                    condition_satisfied_count+=1
                    break
            # loop in prefrenece list of a2 , for unstable : b1 should come before b2
            for women in preferenceList[preferenceListPosDict[matchingPair[j][0]]]:
                if(women == matchingPair[j][1]):
                    break
                if(women==matchingPair[i][1]):
                    condition_satisfied_count+=1
                    break
            # loop in prefrenece list of b2 , for unstable : a1 should come before a2
            for men in preferenceList[preferenceListPosDict[matchingPair[j][1]]]:
                if(men == matchingPair[j][0]):
                    break
                if(men==matchingPair[i][0]):
                    condition_satisfied_count+=1
                    break
        # If all 4 condition are satisfied then both indices can swap their partner and make stable matching
        if(condition_satisfied_count==4):
            unstablepair+=1
    return unstablepair

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as file:
        lines = file.readlines()
        n=int(lines[0])
        preferenceList=[]
        matchingPair=[]
        # Extract the preference list from input and store in 2-d list
        for i in range(1,2*n+1):
            lines[i]=lines[i].split("\n")[0]
            preferenceList.append(list(map(str,lines[i].split(" "))))
        # Extract the matching pair from input and store in 2-d list
        for i in range(2*n+1,3*n+1):
            lines[i] = lines[i].split("\n")[0]
            matchingPair.append(list(map(str, lines[i].split(" "))))
        # call checkStableMatching function for checking stable matching
        unstable_pair=checkSatableMatching(n,preferenceList,matchingPair)
        file1 = open('stableOutput.txt', 'w')
        if(unstable_pair==0):
            file1.write("1 0") # first number indicate the stable matching, second number indicates 0 unstable pair.
        else:
            file1.write("0 "+str(unstable_pair)) # first number indicate the stable matching, second number indicates 0 unstable pair.


