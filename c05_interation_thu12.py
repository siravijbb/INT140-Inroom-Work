#wc05_interation_thu12
#031 ภูมิรพี ดำรงค์มงคลกุล
#048 สิรวิชญ์ แพร่วศวกิจ
#065 คณิติ หัสนีย์
def song(n):
        if not isinstance(n, int):
            raise ValueError("Input must be an integer")
        if 1 <= n <= 9:
            for i in range(int(n)):
                for j in range(i + 1, int(n) + 1):
                    print(j, end="")
                print("")
        else:
            raise ValueError("Not in range: 1-9")


n = (input("Enter number of row:"))
song(int(n))
