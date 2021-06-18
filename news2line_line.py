# -*- coding: utf-8 -*-
import requests  # http通信用のモジュールをインポート

line_token = 'xxx'  # トークン
api_url = 'https://notify-api.line.me/api/notify'  # APIのURL


def line_send(strings):
    """
    Line Notifyに文字列を送信する。

    Parameters
    ----------
    strings : str
        送信したい文字列。
    """

    token_dic = {'Authorization': 'Bearer' + ' ' + line_token}
    send_dic = {'message': strings}
    requests.post(api_url, headers=token_dic, data=send_dic)


# 以下はPythonモジュールでよく使われる単体テスト用のブロックです。
# このファイルをモジュールとしてインポートされた場合には以下は実行されませんが、このファイルを直接
# python news2line_line.py
# などとして実行した場合のみ、以下のコードが実行されます。
# これによりこのモジュールの正常性の確認が行なえます。
if __name__ == '__main__':
    line_send("とらだよー\nとらとら")  # line_send関数を呼び出す
