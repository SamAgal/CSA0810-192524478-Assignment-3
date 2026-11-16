"""Task 3: Dictionaries: Farmer Helpline Complaint Analysis."""

from collections import Counter

calls = [
    "seeds not received seeds delayed",
    "fertiliser price high",
    "seeds price high subsidy not received",
]
STOP = {"not", "high"}

def frequencies(texts, stop):
    counts = {}
    for text in texts:
        for word in text.split():
            w = word.lower()
            if w not in stop:
                counts[w] = counts.get(w, 0) + 1
    return counts

def top(counts, k):
    # Sort by count descending, then word alphabetical ascending
    sorted_items = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    return sorted_items[:k]

if __name__ == "__main__":
    freqs = frequencies(calls, STOP)
    print("Frequencies:", freqs)
    print("Top 3:", top(freqs, 3))
