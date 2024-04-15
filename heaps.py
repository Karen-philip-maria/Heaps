import heapq
numbers = [23,34,5,6,7,8,9]
heapq.heapify(numbers)
print(numbers)

print(heapq.heappop(numbers))

heapq.heappush(numbers, 3)
print(numbers)