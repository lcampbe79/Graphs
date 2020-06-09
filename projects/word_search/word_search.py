# Given two words (begin_word and end_word), and a dictionary's word list, 
# return the shortest transformation sequence from begin_word to end_word, such that:
# Only one letter can be changed at a time.
# Each transformed word must exist in the word list. Note that begin_word is not a transformed word.

# Note:
# Return None if there is no such transformation sequence.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume begin_word and end_word are non-empty and are not the same.

# Sample:
# begin_word = "hit"
# end_word = "cog"
# return: ['hit', 'hot', 'cot', 'cog']
# begin_word = "sail"
# end_word = "boat"
# ['sail', 'bail', 'boil', 'boll', 'bolt', 'boat']
# beginWord = "hungry"
# endWord = "happy"
# None
import string

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

word_set = set()

with open('words.txt', 'r') as f:
    for line in f:
        line = line.strip() #no new line
        word_set.add(line.lower())

letters = list(string.ascii_lowercase)

def get_neighbors(word):
    neighbors = []

    word_letters = list(word)

    # for each letter in the word
    for i in range(len(word_letters)):
        # replace with all in english letters
        for letter in letters:
            #copy the word letters, 1st letter
            temp = list(word_letters)
            #1st letter
            temp[i] = letter
            #make new word
            w = ''.join(temp)

            #see if we form a word
            if w != word and w in word_set:
                neighbors.append(w)
    return neighbors

def find_word_ladder(begin_word, end_word):
    visited = set()
    q = Queue()
    #initializes
    q.enqueue([begin_word])

    while q.size() > 0:
        #move to current list
        path = q.dequeue() 

        #get current vert, last element/node in the path list we are looking at
        cur_word = path[-1] #figure out where to go next, 

        if cur_word not in visited:
            visited.add(cur_word)

            #check to see if current word is the same as the end word
            if cur_word == end_word:
                return path
            
            #returns all current words if nothing comes back
            for neighbor in get_neighbors(cur_word):
                #copy path
                path_copy = list(path)
                path_copy.append(neighbor)
                q.enqueue(path_copy)

    return None

# print(get_neighbors('food'))
# print()
# print(get_neighbors('hit'))
# print()
print(find_word_ladder('hit', 'cog'))