class PriorityQueue:
    class Exception(Exception):
        pass

    class _Entry:
        def __init__(self, key, priority):
            self.key = key
            self.priority = priority

        def __repr__(self):
            return f"Entry({self.key}, {self.priority})"

        def __str__(self):
            return self.__repr__()

    def __init__(self, compare):
        self.heap = list()
        self.locations = dict()
        self.compare = compare

    @staticmethod
    def _left(idx):
        return (2 * idx) + 1

    @staticmethod
    def _right(idx):
        return (2 * idx) + 2

    @staticmethod
    def _parent(idx):
        return idx // 2

    def _swap(self, idx1, idx2):
        self.locations[self.heap[idx1].key] = idx2
        self.locations[self.heap[idx2].key] = idx1
        tmp = self.heap[idx1]
        self.heap[idx1] = self.heap[idx2]
        self.heap[idx2] = tmp

    def _heapifyup(self, idx):
        while idx > 0 and self.compare(self.heap[idx].priority, self.heap[PriorityQueue._parent(idx)].priority):
            parent = PriorityQueue._parent(idx)
            self._swap(idx, parent)
            idx = parent

    def _heapifydown(self, idx):
        left = PriorityQueue._left(idx)
        right = PriorityQueue._right(idx)
        uppermost = idx
        if left < len(self.heap) and self.compare(self.heap[left].priority, self.heap[uppermost].priority):
            uppermost = left
        if right < len(self.heap) and self.compare(self.heap[right].priority, self.heap[uppermost].priority):
            uppermost = right
        if uppermost != idx:
            self._swap(uppermost, idx)
            self._heapifydown(uppermost)

    def min(self):
        if len(self.heap) == 0:
            raise PriorityQueue.Exception("cannot min() empty priority queue")
        return self.heap[0].key

    def min_priority(self):
        if len(self.heap) == 0:
            raise PriorityQueue.Exception("cannot min_priority() empty priority queue")
        return self.heap[0].priority

    def extract_min(self, include_priority=False):
        if len(self.heap) == 0:
            raise PriorityQueue.Exception("cannot extract_min() empty priority queue")
        out = self.heap[0]
        self._swap(0, len(self.heap) - 1)
        self.heap.pop(-1)
        del self.locations[out.key]
        self._heapifydown(0)
        if include_priority:
            return out.key, out.priority
        return out.key

    def __len__(self):
        return len(self.heap)

    def __contains__(self, key):
        return key in self.locations

    def __getitem__(self, key):
        if key not in self.locations:
            raise PriorityQueue.Exception(f"cannot get priority for nonexistent key {key}")
        return self.heap[self.locations[key]].priority

    def __setitem__(self, key, priority):
        if key not in self.locations:
            self.heap.append(PriorityQueue._Entry(key, priority))
            self.locations[key] = len(self.heap) - 1
            self._heapifyup(len(self.heap) - 1)
        else:
            idx = self.locations[key]
            old_priority = self.heap[idx].priority
            self.heap[idx].priority = priority
            if priority < old_priority:
                self._heapifyup(idx)
            else:
                self._heapifydown(idx)

    def __repr__(self):
        return "PriorityQueue(" + ", ".join(f"({e.key}, {e.priority})" for e in self.heap) + ")"

    def __str__(self):
        return self.__repr__()
