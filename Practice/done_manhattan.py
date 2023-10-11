def compute_m_dist(first, second = (0,0)) -> float:
    return abs(first[0]-second[0])+abs(first[1]-second[1])

compute_m_dist((2, 3))