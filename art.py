
import numpy as np

patterns = np.array([
    [1, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 0, 1, 1]
])

vigilance = 0.7
categories = []

for pattern in patterns:
    assigned = False

    for category in categories:
        common = np.sum(pattern * category)
        similarity = common / np.sum(pattern)

        if similarity >= vigilance:
            category[:] = np.maximum(category, pattern)
            assigned = True
            break

    if not assigned:
        categories.append(pattern.copy())

for i, category in enumerate(categories):
    print("Category", i + 1, ":", category)
