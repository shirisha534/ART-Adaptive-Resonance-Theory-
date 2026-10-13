
import numpy as np

patterns = np.array([
    [0.9, 0.1],
    [0.8, 0.2],
    [0.1, 0.9]
])

vigilance = 0.9
categories = []

for pattern in patterns:
    pattern = pattern / np.linalg.norm(pattern)
    assigned = False

    for category in categories:
        similarity = np.dot(pattern, category)

        if similarity >= vigilance:
            category[:] = (category + pattern) / 2
            category[:] = category / np.linalg.norm(category)
            assigned = True
            break

    if not assigned:
        categories.append(pattern.copy())

for i, category in enumerate(categories):
    print("Category", i + 1, ":", np.round(category, 2))
