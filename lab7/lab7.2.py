from collections import Counter
import heapq

def least_interval(tasks, n):
    task_counts = Counter(tasks)  # Даалгавар бүрийн давтамжийг тоолно
    max_heap = [-cnt for cnt in task_counts.values()]  # Давтамжаар буурахаар эрэмбэлнэ
    heapq.heapify(max_heap)

    time = 0
    while max_heap:
        temp = []
        for _ in range(n + 1):  # n + 1 завсарт багтаахыг оролдоно
            if max_heap:
                temp.append(heapq.heappop(max_heap))
            else:
                break

        for cnt in temp:
            if cnt + 1 < 0:
                heapq.heappush(max_heap, cnt + 1)

        if max_heap:
            time += n + 1  # Хэрэв дараагийн даалгавар байвал бүрэн цаг нэмнэ
        else:
            time += len(temp)  # Үлдсэн даалгаврын тоогоор нэмнэ

    return time

# Жишээ өгөгдөл
tasks = ["A", "A", "A", "B", "B", "B"]
n = 2

# Хамгийн бага CPU хугацааг хэвлэх
result = least_interval(tasks, n)
print(f"Хамгийн бага CPU хугацаа: {result}")
