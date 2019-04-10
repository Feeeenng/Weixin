# coding = utf-8
_author_ = 'su'
import requests




class WeiXin():
    def __init__(self,cookie):
        self.cookie = cookie

    def JoinLotteries(self,url,headers):
        res = requests.get(url,headers=headers)
        # 获得抽奖列表 table
        table = res.json().get('data')
        url = 'https://lucky.nocode.com/lottery/{id}/join'
        for item in table:
            if item.get('joined') == False:
                res = requests.post(url.format(id=item.get('id')),headers=headers)
                if res.status_code == 200 and res.json().get('data') == True:
                    print('成功参与抽奖：')
                    prizes = item.get('prizes').get('data')
                    for prize in prizes:
                        print('奖品如下:',prize.get('name'))

    def main(self):
        headers = {}
        headers['Authorization'] = self.cookie
        print('正在参与公共福利抽奖...')
        self.JoinLotteries('https://lucky.nocode.com/public_lottery?page=1&size=5',headers)
        print('正在参与自助福利抽奖...')
        for i in range(1,20):
            self.JoinLotteries('https://lucky.nocode.com/square',headers)
        print('参与抽奖结束,等待下次参与')


if __name__ == '__main__':

    authorization = input('输入手机抓包得到的账号:')
    weixin = WeiXin(authorization)
    weixin.main()
