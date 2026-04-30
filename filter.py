if __name__ == "__main__":
    outfile = open("list_filtered.txt", "w")
    data : str = open("list.txt", "r").read()
    for i in range(0, len(data) - 4):
        if data[i:i+5].isupper() and data[i:i+5].isalpha():
            print(data[i:i+5], file=outfile)
