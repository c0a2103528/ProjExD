from random import randint
import datetime

def shutudai(q):
    qn = randint(0, 2)
    print("問題：")
    print(q[qn])
    st = datetime.datetime.now()
    ans = input("答えるんだ：")
    ed = datetime.datetime.now()
    return qn, ans, (ed-st).seconds

def kaitou(answer, ans, i, sec):
    if answer in ans[i]:
        print("正解！！！")
    else:
        print("出直してこい")
    print(f"回答時間：{sec}秒")

if __name__ == "__main__":
    answers = [["ますお", "マスオ", "ますおさん", "マスオさん"],
            ["わかめ", "ワカメ", "わかめちゃん", "ワカメちゃん"],
            ["甥", "おい", "甥っ子", "おいっこ", "Nephew"]]

    quizzes = ["サザエの旦那の名前は？",
            "カツオの妹の名前は？",
            "タラヲはカツオから見てどんな関係？"]

    q_num, ans, sec = shutudai(quizzes)

    kaitou(ans, answers, q_num, sec)

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
        print(f"回答時間：{sec}秒")
    else:
        min = sec // 60
        sec -= 60 * min
        print(f"回答時間：{min}分{sec}秒")
"""
