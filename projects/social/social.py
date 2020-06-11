import random
import math
import time

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

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            #print("WARNING: You cannot be friends with yourself")
            return False #not able to get new friendship
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            #print("WARNING: Friendship already exists")
            return False
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)
            return True

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
       
        # Add users
        # Use add_user to call num_users the right amount of times
        # Create friendships (bidirectional friendship)
        for i in range(0, num_users):
            self.add_user(f"User {i+1}")

        # # New friendship method:
        # # Randomly generate friendships, keeping new & rejecting duplicates until
        # # We get to the number we need(num_users * Avg_freindships //2)

        # # Keep tracj of good firendships and collisions (refactor add_friendship)
        target_friendships = num_users * avg_friendships // 2
        total_frienships = 0
        collisions = 0

        while total_frienships < target_friendships:
            user_id = random.randint(1, self.last_id)
            friend_id = random.randint(1, self.last_id)

            if self.add_friendship(user_id, friend_id): #if true
                total_frienships += 1 #since doubles in target_friendships
            else:
                collisions += 1
        print(f"Total collisions: {collisions}")

        # # Generate all friendship combos empty list
        # possible_friendships = []

        # # Avoid duplicates by making sure first number is smaller than second
        # # Create a list with all possible friendship combinations
        # for user_id in self.users:
        #     for friend_id in range(user_id+1, self.last_id+1):
        #         possible_friendships.append((user_id, friend_id))
        # # print(possible_friendships)
        
        # # Shuffle all possible friendships from the list
        # random.shuffle(possible_friendships)
        # # print(possible_friendships)

        # # Create for firstX pairs is total //2(how many calls ) 1:51
        # # Create N random friendships 
        # # n = avg_friendships * num_users // 2
        # # total_users = avg_friendships * num_users // 2
        # for i in range(num_users * avg_friendships// 2):
        #     friendship = possible_friendships[i]
        #     self.add_friendship(friendship[0], friendship[1])


        # * Hint 1: To create N random friendships, 
        # you could create a list with all possible friendship combinations, 
        # shuffle the list, then grab the first N elements from the list. 
        # You will need to `import random` to get shuffle.
        # * Hint 2: `add_friendship(1, 2)` is the same as `add_friendship(2, 1)`. 
        # You should avoid calling one after the other since it will do nothing but print a warning. 
        # You can avoid this by only creating friendships where user1 < user2. (friend 1 is lower than friend 2)

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        # Shortest tells us Breadth first
        # Extended network - traversal, connected components

        # Planning:
        # How am I going to build the graph?
        # Start at given user_id, use BFT to return each friend

        # pseudocode:
        # Create queue
        queue = Queue()
        # Enqueue path
        queue.enqueue([user_id]) #starting user
        # path = path[-1] #[user_id]
        # create visited, key is user in extended network, value is the path to that user
        visited = {}  # Note that this is a dictionary (looks only for the key), not a set
        # add to visited-
        #  ^ while queue is empty
        while queue.size() > 0:
            # dequeue first path
            path = queue.dequeue()
            #helper for the "vertex"
            user = path[-1] #explores the path to find the end, grabs the last one in the list
            # if not visited
            if user not in visited:
            #do the thing!!
            # add to visited
                visited[user] = path #path so far
            # for each neighbor
                for neighbor in self.friendships[user]:
                #copy path and enqueue
                    #new_path = path.copy()
                    # new_path = list(path)
                    # new_path.append(neighbor)
                    # queue.enqueue(new_path)

                    #returns a list without modifying the one in place that doesn’t require first creating a new path
                    queue.enqueue(path + [neighbor])

        



        # # Creates a dictionary to store the vertices
        # visited = {}  # Note that this is a dictionary, not a set
        
        # # Create a queue and enqueue starting vertex
        # queue = Queue()

        # # Create a path with the user_id
        # path = [user_id]

        # # Enqueues the starting vertex
        # # creates the path 
        # queue.enqueue(path)

        # # While the queue is not empty
        # while queue.size() > 0:
        #     # dequeue the first path
        #     current_path = queue.dequeue
        #     new_user_id = current_path[-1]

        #     if new_user_id not in visited:
        #         visited[new_user_id] = current_path

        #         friends = self.friendships(new_user_id)
        #         for friend in friends:
        #             path_copy = list(current_path)
        #             path_copy.append(friend)
        #             queue.enqueue(path_copy)


        return visited


if __name__ == '__main__':

    sg = SocialGraph()
    start_time = time.time()
    sg.populate_graph(1000, 5)
    end_time = time.time()
    print (f"runtime: {end_time - start_time} seconds")
    connections = sg.get_all_social_paths(1)
    # print(sg.friendships)
    # print(connections)
    users_in_extended_network = len(connections) - 1
    total_users = len(sg.users)
    print("----------------")
    print(f"Pecentage: {users_in_extended_network/ total_users * 100:2f}")
    total = 0
    # for user_id in connections:
    #     total += len(connections[user_id]) - 1
    # print(len(connections))
    # print(total / len(connections))

    # total_connections = 0
    # total_degrees = 0
    # iterations = 10
    # for i in range(0, iterations):
    #     sg.populate_graph(1000, 5)
    #     connections = sg.get_all_social_paths(1)
    #     total = 0
    #     for user_id in connections:
    #         total += len(connections[user_id]) - 1
    #     total_connections += len(connections)
    #     total_degrees += total / len(connections)
    #     print("-----")
    #     print(f"Friends in network: {len(connections)}")
    #     print(f"Avg degrees: {total / len(connections)}")
    # print(total_connections / iterations)
    # print(total_degrees / iterations)
    # sg = SocialGraph()
    # sg.populate_graph(10, 2)
    # print(f"friendships: ", sg.friendships)
    # print(f"----------------")
    # connections = sg.get_all_social_paths(1)
    # print(f"connections: ", connections)
    # print(f"----------------")
    # total_social_paths = 0
    # for user_id in connections:
    #     total_social_paths += len(connections[user_id]) -1 
    # print(f" Avg length of social path: {total_social_paths / len(connections)}")
