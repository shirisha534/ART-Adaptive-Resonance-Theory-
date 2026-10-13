
import numpy as np

class ART:
    def __init__(self, vigilance=0.7):
        self.vigilance = vigilance
        self.categories = []

    def learn(self, pattern):
        pattern = np.array(pattern)
        for i, category in enumerate(self.categories):
            common = np.sum(pattern * category)
            total = np.sum(pattern)

            if total > 0 and common / total >= self.vigilance:
                self.categories[i] = np.maximum(category, pattern)
                return i + 1

        self.categories.append(pattern.copy())
        return len(self.categories)

art = ART(0.7)

patterns = [
    [1, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 0, 1, 1]
]

for pattern in patterns:
    category = art.learn(pattern)
    print(pattern, "-> Category", category)

print("Learned Categories:")
for category in art.categories:
    print(category)
