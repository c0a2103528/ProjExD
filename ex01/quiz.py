from random import randint
import datetime

def main():
    def shutudai(q, qn):
        print("問題：")
        print(q[qn])
        st = datetime.datetime.now()
        ans = input("答えるんだ：")
        ed = datetime.datetime.now()
        return ans, (ed-st).seconds

    def kaitou(answer, ans, i, sec):
        if answer in ans[i]:
            print("正解！！！")
        else:
            print("出直してこい")
        print(f"解答時間：{sec}秒")

    answers = [["ますお", "マスオ"],
            ["わかめ", "ワカメ"],
            ["甥", "おい", "甥っ子", "おいっこ"]]

    quizzes = ["サザエの旦那の名前は？",
            "カツオの妹の名前は？",
            "タラオはカツオから見てどんな関係？"]

    quiz_num = randint(0, 2)
    ans, sec = shutudai(quizzes, quiz_num)

    kaitou(ans, answers, quiz_num, sec)

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
    if sec < 60:
        print(f"解答時間：{sec}秒")
    else:
        min = sec // 60
        sec -= 60 * min
        print(f"解答時間：{min}分{sec}秒")
"""

main()