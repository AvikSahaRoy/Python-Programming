class Insertion_Sort:
    def __init__(self):
        self.n = int(input("Enter how many value you want to input: "))
        self.l = []
        for i in range(self.n):
            temp = int(input(f"Enter your {i} value: "))
            self.l.append(temp)

    def Process(self):      
        for i in range(1, self.n):
            key = self.l[i]
            j = i - 1
            while j>=0 and key < self.l[j]:
                self.l[j+1] = self.l[j]
                j -= 1
            self.l[j+1] = key
        print(self.l)

if __name__ == "__main__":
    s = Insertion_Sort()
    s.Process()