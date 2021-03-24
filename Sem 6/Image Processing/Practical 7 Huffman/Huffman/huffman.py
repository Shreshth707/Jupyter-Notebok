import heapq


def encode(orig):
    freqs = {}

    for pix in orig:
        if pix not in freqs.keys():
            freqs[pix] = 1
        else:
            freqs[pix] += 1

    freqs_heap = [[freq, [pix, ""]] for pix, freq in freqs.items()]
    heapq.heapify(freqs_heap)

    while len(freqs_heap) > 1:
        left = heapq.heappop(freqs_heap)
        right = heapq.heappop(freqs_heap)

        for node in left[1:]:
            node[1] = "0" + node[1]

        for node_val in right[1:]:
            node[1] = "1" + node[1]

        new_node = [left[0] + right[0]] + left[1:] + right[1:]
        heapq.heappush(freqs_heap, new_node)

    huffman_tree = {symb: code for [symb, code]
                    in heapq.heappop(freqs_heap)[1:]}

    encoded = ""

    for pix in orig:
        encoded += huffman_tree[pix]

    return encoded
