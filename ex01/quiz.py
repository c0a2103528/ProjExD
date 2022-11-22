from random import randint
import datetime
"""
def main():
    answers = [["ますお", "マスオ"],
            ["わかめ", "ワカメ"],
            ["甥", "おい", "甥っ子", "おいっこ"]]
    quizzes = ["サザエの旦那の名前は？",
            "カツオの妹の名前は？",
            "タラオはカツオから見てどんな関係？"]

    def shutudai(q):
        print("問題：")
        quiz_num = randint(0, 2)
        print(q[quiz_num])
        return quiz_num

    def kaitou(answer, ans, i):
        if answer in ans[i]:
            print("正解！！！")
        else:
            print("出直してこい")

    q_num = shutudai(quizzes)

    st = datetime.datetime.now()
    ans = input("答えるんだ：")
    ed = datetime.datetime.now()

    kaitou(ans, answers, q_num)
    sec = (ed - st).seconds
    print(f"解答時間：{sec}秒")

"""
def main():
    answers = [["ますお", "マスオ"],
            ["わかめ", "ワカメ"],
            ["甥", "おい", "甥っ子", "おいっこ"]]
    quizzes = ["サザエの旦那の名前は？",
            "カツオの妹の名前は？",
            "タラオはカツオから見てどんな関係？"]

    print("問題：")
    quiz_num = randint(0, 2)
    print(quizzes[quiz_num])

    st = datetime.datetime.now()
    ans = input("答えるんだ：")
    ed = datetime.datetime.now()

    if ans in answers[quiz_num]:
        print("正解！！！")
    else:
        print("出直してこい")

    sec = (ed - st).seconds
    print(f"解答時間：{sec}秒")


main()