"""
Input: Statements and expression with the Friends class.
Output: The behaviour as described.
Example:
f = Friends([{"1", "2"}, {"3", "1"}])
f.add({"1", "3"})
>> False
f.add({"4", "5"})
>> True
"""

class Friends():
    def __init__(self, connections):
        self.connections = connections

    def add(self, data):
        if data in self.connections:
            return False
        else:
            list_tuple = list(self.connections)
            list_tuple.append(set(data))
            self.connections = tuple(list_tuple)
            print(self.connections)
            return True

    def remove(self, data):
        if data in self.connections:
            list_tuple = list(self.connections)
            list_tuple.remove(set(data))
            self.connections = tuple(list_tuple)
            return True
        else:
            return False

    def names(self):
        stack = []
        for i in self.connections:
            for j in i:
                if j not in stack:
                    stack.append(j)
        return set(stack)

    def connected(self, name):
        stack = []
        for i in self.connections:
            if name in i:
                listed = list(i)
                ind = listed.index(name)
                if ind == 0:
                    stack.append(listed[1])
                else:
                    stack.append(listed[0])
        return set(stack)


# test add (self.connection append data + Tru when set or reversed set not in self.connections )
f = Friends(({'1', '2'}, {'3', '1'}))
print(f.add({'2', '1'}))
print(f.add({'5', '1'}), end='\n\n')

# test remove (self.connections.remove(i) when data in self.connections)

s = Friends(({'1', '2'}, {'3', '1'}))
print(s.remove({'1', '3'}))
print(s.remove({'4', '5'}))

# test names
r = Friends([{"a", "b"}, {"b", "c"}, {"c", "d"}])
print(r.names())

# test connected
c = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}))
print(c.connected("a"))
print(c.connected("r"))