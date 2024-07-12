#  (Генерация последовательности n, где число повторяется столько раз,
# чему оно равно)
from typing import List


def generate_sequence(n: int) -> List[int]:
    """Генерация последовательности."""
    sequence = []
    i = 1

    while len(sequence) < n:
        sequence.extend([i] * i)
        i += 1

    return sequence[:n]


n = int(input("Введите количество элементов последовательности: "))
result = generate_sequence(n)
print(result)
