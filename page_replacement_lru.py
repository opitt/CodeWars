
def lru(n, reference_list):
    lru = []
    cache = []
    for page in reference_list:
        if page in cache:
            lru_idx = cache.index(page)
            lru.remove(lru_idx)
            lru.append(lru_idx)
            continue
        # page fault
        if len(cache)<n:
            # still empty slots
            cache.append(page)
            lru.append(len(cache)-1)
        else:
            # take the least recently used
            cache[lru[0]] = page
            lru.append(lru[0])
            lru.pop(0)
    cache.extend([-1 for _ in range(n-len(cache))])
    return cache

print(lru(3, [1, 2, 3, 4, 3, 2, 5]))
