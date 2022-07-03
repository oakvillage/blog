from jsonschema import validate, ValidationError
import sys, os, json

DIST_DIR = 'docs'

# Githubにてデプロイ中のエラーを検出
class AppError(Exception): pass

def main() -> None:
    args = sys.argv
    # 引数からjsonを取得、検証を行う
    contents = get_json_from_args(args)
    # if contents is None or not validate_json_schema(contents):
    #     sys.exit('json error.')

    try:
        # 記事を出力する
        output_html(contents)

        # 検索用インデックスのjsonを追加し、出力する

        # コメントを受け付ける為のissueを作成する

    except AppError as e:
        print('')
        sys.exit('')

    except:
        sys.exit('')

# コマンドライン引数からjsonを取得する
def get_json_from_args(args: list) -> dict|list:
    if 3 == len(args) and args[2] == os.environ.get('DEPLOY_KEY') :
        try:
            js = json.loads(args[1])
            return js
        except json.JSONDecodeError as e:
            print(e)
        except:
            print('System error.')
    else:
        print('Argments are not valid.')
    return None

# 受け取ったjsonを検証する
def validate_json_schema(contents: dict|list) -> bool:
    with open('schema.json') as schemaObj:
        schema = json.load(schemaObj)
        try:
            validate(contents, schema)
            return True
        except ValidationError as e:
            print('json validate error')
    return False

# 記事内容をHTMLにて出力する
def output_html(contents: list) -> None:
    for content in contents:
        filename = 
        with open(filename) as js:
            

# メイン処理
if __name__ == '__main__':
    main()
