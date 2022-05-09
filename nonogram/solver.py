def determine_filled_empty_sets(group_sizes,
                                size,
                                filled=None,
                                empty=None):
    if empty is None:
        empty = set()
    if filled is None:
        filled = set()
    ps = valid_placements(group_sizes, size, filled, empty)
    counters = [0 for _ in range(size)]
    for p in ps:
        for begin, end_excl in p:
            for pos in range(begin, end_excl):
                counters[pos] += 1

    num_ps = len(ps)
    new_filled = set()
    new_empty = set()
    for pos, cnt in enumerate(counters):
        if cnt == 0:
            new_empty.add(pos)
        elif cnt == num_ps:
            new_filled.add(pos)

    return new_filled, new_empty


def valid_placements(group_sizes,
                     size,
                     filled=None,
                     empty=None):
    if empty is None:
        empty = set()
    if filled is None:
        filled = set()
    ps = _placements(group_sizes, size)
    return list(filter(lambda p: _is_valid(p, filled, empty), ps))


def _placements(group_sizes, size, start=0):
    if not group_sizes:
        return [[]]
    first_size = group_sizes[0]
    remaining = group_sizes[1:]
    avail_size = size - start - sum(remaining) - len(remaining)
    if first_size > avail_size:
        return []
    max_offset = avail_size - first_size
    ret = []
    for offset in range(max_offset + 1):
        begin = start + offset
        end_excl = begin + first_size
        placement = (begin, end_excl)
        new_start = start + offset + first_size + 1
        for ps in _placements(remaining, size, new_start):
            ret.append([placement] + ps)
    return ret


def _is_valid(placement, filled=None, empty=None):
    if empty is None:
        empty = set()
    if filled is None:
        filled = set()
    for pos in filled:
        if not _is_filled(pos, placement):
            return False
    for pos in empty:
        if _is_filled(pos, placement):
            return False
    return True


def _is_filled(pos, placement):
    for begin, end_excl in placement:
        if pos in range(begin, end_excl):
            return True
    return False
