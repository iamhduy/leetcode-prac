class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capa = capacity
        self.cache = list()
        self.dict = dict()

    def __str__(self):
        s = ''
        s += "Cache:" + str(self.cache) + '\n'
        s += "Dict:" + str(self.dict) + '\n'
        return s

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.dict:
            self.update(key)
            return self.dict[key]
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        self.update(key)
        self.dict[key] = value

    def update(self, key):
        try:
            ind = self.cache.index(key, max(0, len(self.cache) - self.capa), len(self.cache))
            self.cache.pop(ind)
            self.cache.append(key)
        except ValueError:
            self.cache.append(key)

        if len(self.cache) > self.capa:
            old_key = self.cache[len(self.cache) - self.capa-1]
            if old_key in self.dict:
                self.dict.pop(old_key)


def parse(l1, l2):
    a = ''
    out = list()
    for i in range(len(l1)):
        cmd = l1[i]
        param = l2[i]
        if i <= 40:
            print(cmd, param)
            print(a)
        # print(cmd, param)
        res = ''
        if cmd == "LRUCache":
            a = LRUCache(param[0])
        elif cmd == "put":
            # print(a.cache)
            a.put(param[0], param[1])
        else:
            res = a.get(param[0])

        out.append(res)
    return out


cmd1 = ["LRUCache","put","put","put","put","put","get","put","get","get","put","get","put","put","put","get","put","get","get","get","get","put","put","get","get","get","put","put","get","put","get","put","get","get","get","put","put","put","get","put","get","get","put","put","get","put","put","put","put","get","put","put","get","put","put","get","put","put","put","put","put","get","put","put","get","put","get","get","get","put","get","get","put","put","put","put","get","put","put","put","put","get","get","get","put","put","put","get","put","put","put","get","put","put","put","get","get","get","put","put","put","put","get","put","put","put","put","put","put","put"]

param1 = [[10],[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]]

print(parse(cmd1, param1))
truth = ['null', 'null', 'null', 'null', 'null', 'null', -1, 'null', 19, 17, 'null', -1, 'null', 'null', 'null', -1,
         'null', -1, 5, -1, 12, 'null', 'null', 3, 5, 5]

for j in range(len(truth)):
    if truth[j] == 'null':
        truth[j] = ''
#print(truth)
cmd2 = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
pr2 = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
#print(parse(cmd2, pr2))
