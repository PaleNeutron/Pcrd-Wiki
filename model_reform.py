def main():
    with open("models_gen.py") as f:
        rl = f.readlines()

    new_ls = []
    for i, l in enumerate(rl[1:]):
        print(rl[i])

        if "models.Model" in rl[i]:
            l = l.replace("()", "(primary_key=True)")
            print("****"+l)
        new_ls.append(l)

    with open("./pcrd_unpack/models_gen.py", "w", newline="\n") as f:
        rl = f.writelines(new_ls)

if __name__ == '__main__':
    main()
