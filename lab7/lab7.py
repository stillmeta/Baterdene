# Fractional Knapsack Problem
class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

    def __lt__(self, other):
        return (self.value / self.weight) > (other.value / other.weight)

def fractional_knapsack(capacity, items):
    items.sort(reverse=True)  # Эд зүйлсийг үнэ/жин харьцаагаар нь буурахаар эрэмбэлнэ
    total_value = 0.0
    for item in items:
        if capacity > 0 and item.weight <= capacity:
            # Бүрэн оруулж болох үед
            capacity -= item.weight
            total_value += item.value
        else:
            # Хэрэв бараа бүхэлдээ багтахгүй бол хэсгийг нь оруулна
            fraction = capacity / item.weight
            total_value += item.value * fraction
            break

    return total_value
items = [
    Item(60, 10),
    Item(100, 20),
    Item(120, 30),
]
capacity = 50

# Үр дүнг хэвлэнэ
max_value = fractional_knapsack(capacity, items)
print(f"Үүргэвчинд багтаах боломжтой хамгийн их үнэ: {max_value}")
