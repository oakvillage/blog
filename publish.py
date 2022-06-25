from typing import Union
import sys, os, json

def main() -> None:
    args = sys.argv

    contents = getJsonFromArgs(args)
    if contents is not None:
        print(json.dumps(contents))
        print(type(contents))

# コマンドライン引数からjsonを取得する
def getJsonFromArgs(args: list) -> dict|list:
    if 3 == len(args) and args[2] == os.environ.get('DEPLOY_KEY') :
        try:
            js = json.loads(args[1])
            return js
        except json.JSONDecodeError as e:
            print(e)
    else:
        print('Argments are not valid.')
    return None

# メイン処理
if __name__ == '__main__':
    main()
