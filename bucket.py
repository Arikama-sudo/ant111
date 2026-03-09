def display(state):
    caps = [8, 5, 3]
    print("\nTry to get 4L of water into one of these buckets:\n")
    for level in range(8, 0, -1):
        print(f"{level} |", end='')
        for i in range(3):
            if state[i] >= level:
                print("#", end='')
            else:
                print(" ", end='')
            if i < 2:
                print("|", end='')
        print("|")
    print("  +---+---+---+")
    print("  8L  5L  3L\n")


def main():
    caps = [8, 5, 3]
    state = [0, 0, 0]

    bucket_to_idx = {8: 0, 5: 1, 3: 2}
    idx_to_bucket = [8, 5, 3]

    print("Water jug puzzle. Try to get 4L in any bucket.")
    print("Commands: (f)ill, (e)mpty, (p)our, (q)uit")
    display(state)

    while True:
        cmd = input("> ").strip().lower()

        if cmd == 'q':
            print("Quit.")
            break

        elif cmd == 'f':
            inp = input("Select a bucket 8, 5, 3, or QUIT: ").strip()
            if inp.lower() in ('quit', 'q'):
                break
            try:
                bucket = int(inp)
                if bucket not in bucket_to_idx:
                    print("Invalid bucket. Choose 8, 5, or 3.")
                    continue
                idx = bucket_to_idx[bucket]
                state[idx] = caps[idx]
                display(state)
                if 4 in state:
                    print("Congratulations! You have 4L in a bucket!")
                    break
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif cmd == 'e':
            inp = input("Select a bucket 8, 5, 3, or QUIT: ").strip()
            if inp.lower() in ('quit', 'q'):
                break
            try:
                bucket = int(inp)
                if bucket not in bucket_to_idx:
                    print("Invalid bucket. Choose 8, 5, or 3.")
                    continue
                idx = bucket_to_idx[bucket]
                state[idx] = 0
                display(state)
                if 4 in state:
                    print("Congratulations! You have 4L in a bucket!")
                    break
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif cmd == 'p':
            inp_from = input("From bucket (8,5,3) or QUIT: ").strip()
            if inp_from.lower() in ('quit', 'q'):
                break
            inp_to = input("To bucket (8,5,3) or QUIT: ").strip()
            if inp_to.lower() in ('quit', 'q'):
                break
            try:
                from_bucket = int(inp_from)
                to_bucket = int(inp_to)
                if from_bucket not in bucket_to_idx or to_bucket not in bucket_to_idx:
                    print("Invalid bucket. Choose 8, 5, or 3.")
                    continue
                if from_bucket == to_bucket:
                    print("Cannot pour into the same bucket.")
                    continue
                from_idx = bucket_to_idx[from_bucket]
                to_idx = bucket_to_idx[to_bucket]

                amount = min(state[from_idx], caps[to_idx] - state[to_idx])
                if amount == 0:
                    print("Nothing to pour or target is full.")
                else:
                    state[from_idx] -= amount
                    state[to_idx] += amount
                display(state)
                if 4 in state:
                    print("Congratulations! You have 4L in a bucket!")
                    break
            except ValueError:
                print("Invalid input. Please enter a number.")

        else:
            print("Unknown command. Use f, e, p, q.")


if name == "main":
    main()