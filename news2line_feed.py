# -*- coding: utf-8 -*-
import feedparser  # RSSやAtomなどのサイトメタデータを処理するモジュールをインポート


def feed(rssurl):
    """
    フィードを取得して処理する。

    Parameters
    ----------
    rssurl : str
        フィードのURL。

    Returns
    -------
    ret : str
        エントリーのタイトル文字列とそのURLの羅列。
    """

    d = feedparser.parse(rssurl)  # feedparserのインスタンスを生成する
    strings = [d.feed.title + "\n"]  # まずstringsにサイトタイトルを入れ、一行空の行を足す
    for entry in d['entries']:  # エントリーの数だけループ
        title = entry.title  # エントリーのタイトル
        link = entry.link + "\n"  # エントリーのURL
        strings.append(title)
        strings.append(link)

    ret = "\n".join(strings)
    return ret


# 以下はPythonモジュールでよく使われる単体テスト用のブロックです。
# このファイルをモジュールとしてインポートされた場合には以下は実行されませんが、このファイルを直接
# python news2line_feed.py
# などとして実行した場合のみ、以下のコードが実行されます。
# これによりこのモジュールの正常性の確認が行なえます。
if __name__ == '__main__':
    rssurl = 'https://karapaia.com/index.rdf'  # RSSのURLとしてカラパイアのRSSのURLを指定する。
    print(feed(rssurl))  # feed関数を呼び出し標準出力に出力。
