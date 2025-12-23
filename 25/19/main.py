import copy
from collections import deque

data = open("input.txt", encoding="utf-8").read().rstrip()

boxes = [[] for _ in range(5)]

for line in data.split("\n"):
    name, shape, weight = line.split(", ")

    name = name[-1]
    shape = shape == "rund" or shape == "sylinder"
    weight = int(weight)
    boxes[0].append((name, shape, weight))


NUM_BOXES = len(boxes[0])


def get_next_moves(boxes) -> tuple[list[tuple[str, bool, int]], int, int]:
    moves = []

    for start_i, start_box in enumerate(boxes):
        if not start_box:
            continue

        for j in range(min(len(start_box), 3)):

            to_move = start_box[len(start_box) - 1 - j :]

            # rund/sylinder on rund/sylinder
            if any(
                to_move[i][1] and to_move[i + 1][1] for i in range(len(to_move) - 1)
            ):
                continue

            # to heavy
            weight = sum(map(lambda x: x[2], to_move))
            if weight > 10:
                continue

            for end_i, end_box in enumerate(boxes):
                if start_i == end_i:
                    continue

                if end_box:
                    # heavy on lighter box
                    if to_move[0][2] > end_box[-1][2]:
                        continue

                    # rund/sylinder
                    if to_move[0][1] and end_box[-1][1]:
                        continue

                moves.append((to_move, start_i, end_i))

    return moves


visited = set()
q = deque([(boxes, "")])  # boxes: list[list[tuple[str, bool, int ]]], path: str

while q:
    boxes, path = q.popleft()

    if len(boxes[4]) == NUM_BOXES:
        print(path)
        break

    for to_move, start, end in get_next_moves(boxes):

        next_boxes = copy.deepcopy(boxes)

        for _ in range(len(to_move)):
            next_boxes[start].pop()

        next_boxes[end].extend(to_move)

        hasable = tuple(tuple(x) for x in next_boxes)
        if hasable in visited:
            continue
        visited.add(hasable)

        q.append(
            (
                next_boxes,
                f"{path} [{",".join(list(map(lambda x: x[0], to_move)))}] {str(start)} > {str(end)}.",
            )
        )
