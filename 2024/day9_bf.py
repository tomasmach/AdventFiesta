def read_data(filename):
    with open(filename, 'r') as f:
        data = [int(d) for d in f.read().strip()]
    return data

def part1(data):
    disk_view = []
    file_num = 0

    for i in range(0, len(data) - 1, 2):
        for j in range(data[i]):
            disk_view.append(file_num)
        for k in range(data[i+1]):
            disk_view.append(".")
        file_num = file_num + 1

    if len(data) % 2 != 0:
        for j in range(data[-1]):
            disk_view.append(file_num)

    for i in range(len(disk_view) - 1, -1, -1):
        if disk_view[i] == ".":
            continue

        for j in range(len(disk_view)):
            if disk_view[j] == ".":
                disk_view[j] = disk_view[i]
                disk_view[i] = "."
                break

    del disk_view[0]
    final_list = []

    for i in range(len(disk_view)):
        if disk_view[i] == ".":
            break
        final_list.append(i * disk_view[i])

    print(sum(final_list))

def part2(data):
    disk_view = []
    file_num = 0

    for i in range(0, len(data) - 1, 2):
        for j in range(data[i]):
            disk_view.append(file_num)
        for k in range(data[i+1]):
            disk_view.append(".")
        file_num += 1

    if len(data) % 2 != 0:
        for j in range(data[-1]):
            disk_view.append(file_num)

    unique_ids = sorted(set(disk_view) - {'.'}, reverse=True)

    for current_id in unique_ids:
        file_positions = [i for i, x in enumerate(disk_view) if x == current_id]
        file_length = len(file_positions)
        min_pos = min(file_positions)
        free_start = None
        free_length = 0
        target_start = None

        for k in range(min_pos):
            if disk_view[k] == ".":
                if free_start is None:
                    free_start = k
                free_length += 1
            else:
                if free_length >= file_length:
                    target_start = free_start
                    break
                free_start = None
                free_length = 0

        if free_start is not None and free_length >= file_length and target_start is None:
            target_start = free_start

        if target_start is not None:
            for j, pos in enumerate(file_positions):
                disk_view[target_start + j] = current_id
                disk_view[pos] = "."

    checksum = 0
    for i, block in enumerate(disk_view):
        if block != ".":
            checksum += i * block

    print("Final disk_view:", disk_view)
    print("Checksum:", checksum)

data = read_data("input.txt")
part2(data)
