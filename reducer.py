#!/usr/bin/env python

from operator import itemgetter
import sys

d1= {} 

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    #print(line)
    line = line.strip()
    # print(line)
    # parse the input we got from mapper.py
    key, value = line.split('\t', 1)

    
    if key not in d1:
        d1[key]=[]
     
    d1[key].append(value)


    
""" Return the number of interests that user1 and user2
    have in common """
def overlap(user1, user2, interests):
    num_of_interests = 0;
    # Iterates through each value of user1
    for user1_values in interests[user1]:
        # if true, num_of_interests will be incremented by 1
        if (user1_values in interests[user2] ):
            num_of_interests += 1;
    return num_of_interests;

""" Determine the name of user who is most similar
to the input user defined by having the most interests
in common. Return a tuple: (most_similar_user, num_interests_in_common) """
def most_similar(user, interests):
    user_count = {};
    # Iterates through each user in the interest dictionary
    for dict_user in interests.keys():
        # Ignores the input user
        if (user != dict_user ):
            count = overlap(user, dict_user, interests);
            # All the count values with user names are stored as key and value in user_count
            user_count[dict_user] = count;
            count = 0;
    # maximum value in the user_count dict is found and returned
    most_similar_user = max(user_count, key = user_count.get);
    return (most_similar_user, user_count[most_similar_user])
 


for user in d1.keys():
    
     print (user ,most_similar(user, d1)[0] )
    
    
       
