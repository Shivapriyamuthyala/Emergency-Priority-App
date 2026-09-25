import heapq

class EmergencyQueue:
    def __init__(self):
        self.heap = []

    def add_patient(self, name, priority):
        heapq.heappush(self.heap, (priority, name))

    def get_all(self):
        # Sort so HIGH priority (2) comes first
        return sorted(self.heap, key=lambda x: -x[0])
