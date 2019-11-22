from terminaltables import AsciiTable
from getpass import getpass

import random

HERD = ['回合', '範圍', '猜謎數字']
CONTENT = []
MIN = 0
MAX = 100


def main():
    print('-----終極密碼-----')
    while True:
        game_start()
        is_repeat_game = get_is_repeat_game()
        if not is_repeat_game:
            print('遊戲結束!!!')
            exit()


# 取得是否重新再玩一次
def get_is_repeat_game():
    while True:
        ans = input('請問要重新再來一局嗎？[y/n]：')
        if ans.lower() == 'y':
            return True
        elif ans.lower() == 'n':
            return False


# 遊戲開始
def game_start():
    ans = get_ans()
    print('設定完成 遊戲開始!!!!!')
    round = 1
    while True:
        guess = get_user_ans()
        CONTENT.append([round, '{min}-{max}'.format(min=MIN, max=MAX), guess])
        result = get_result(ans, guess)
        if result:
            break
        
        round += 1

    print('恭喜猜中數字 答案為：{ans} 總共耗費{round}回合'.format(
        ans=ans,
        round=round
    ))
    table = AsciiTable([HERD, *CONTENT])
    print(table.table)


# 取得答案
def get_ans():
    while True:
        ans_choose = input('請先選擇手動設定答案還是由電腦自行產生[y/n]：')
        if ans_choose.lower() == 'y':
            print('由玩家自行設定...')
            return get_user_ans(hide=True)
        elif ans_choose.lower() == 'n':
            print('由電腦設定...')
            return get_system_ans()


# 取得使用者自行設定之答案
def get_user_ans(hide=False):
    while True:
        prompt = '請輸入{min}-{max}數字：'.format(min=MIN, max=MAX)
        if hide:
            ans = getpass(prompt)
        else:
            ans = input(prompt)

        if not ans.isdigit():
            print('格式錯誤 答案含有非數字')
            continue

        ans = int(ans)
        if not MIN <= ans <= MAX:
            print('格式錯誤 答案要介於{min}-{max}'.format(min=MIN, max=MAX))
            continue

        return ans


# 取得電腦設定之答案
def get_system_ans():
    return random.randint(1, 101)


# 比對猜謎數字與答案
def get_result(ans, guess):
    # global為使用全域變數
    global MIN, MAX
    if ans > guess:
        MIN = guess
        return False
    elif ans < guess:
        MAX = guess
        return False
    elif ans == guess:
        return True

if __name__ == '__main__':
    main()
