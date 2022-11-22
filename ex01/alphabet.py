import random

chars_num = 10
miss_num = 2

def set_quiz():
    global chars_num
    global miss_num

    chars = []
    while (len(chars) < chars_num):
        char = random.randint(65, 90)
        if not(chr(char) in chars):
            chars.append(chr(char))
    print("対象文字：")
    print(chars)

    miss = []
    for i in range(miss_num):
        n = random.randint(0, chars_num - (1+i))
        miss.append(chars.pop(n))
    
    random.shuffle(chars)
    print("表示文字：")
    print(chars)
    
    return miss

def num_kaitou():
    global miss_num
    mn_ans =  input("欠損文字はいくつあるでしょうか？：")
    if int(mn_ans) == miss_num:
        res = 1
    else:
        res = 0
    return res

def moji_kaitou(miss_list):
    global miss_num
    m_ans = ["" for i in range(miss_num)]
    for i in range(miss_num):
        m_ans[i] = input(f"{i+1}つ目の文字を入力して下さい：")
    for i in m_ans:
        if i in miss_list:
            res = 1
        else:
            res = 0
            break
    return res


if __name__ == "__main__":
    while True:
        miss_list = set_quiz()
        nres = num_kaitou()
        if nres:
            print("正解です。それでは、具体的に欠損文字を1つずつ入力して下さい")
        else:
            print("不正解です。またチャレンジしてください。")
            continue

        mres = moji_kaitou(miss_list)
        if mres:
            print("正解です！！")
            break
        else:
            print("不正解です。またチャレンジしてください。")


