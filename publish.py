from jsonschema import validate, ValidationError
import sys, os, json, datetime, markdown, re

DIST_DIR = 'docs'

# Githubにてデプロイ中のエラーを検出
class AppError(Exception): pass

def main() -> None:
    args = sys.argv

    try:
        # 引数からjsonを取得、検証を行う
        contents = get_json_from_args(args)

        # 記事を出力する
        output_html(contents)
        
        # トップページを更新する
        update_main_page(contents)

        # 検索用インデックスのjsonを追加し、出力する
        merge_contents(contents)

        # コメントを受け付ける為のissueを作成する
        enable _comments()
        
        # コミットする
        commit()
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

# 記事内容をHTMLにて出力する
def output_html(contents: list) -> None:
    for content in contents:
        # HTMLを出力
        path = get_path_from_permanent_link(content['permanent_link'])
        filename = content['slug'] + '.html'
        html = markdown.markdown(content['content_markdown'])
        output_file(path, filename, html)

def get_path_from_permanent_link(permanent_link: str) -> str:
    return re.sub('/(\/| ){2,}/', '/', '/' + permanent_link + '/')

def update_main_page(contents: list) -> None:
    pass
        
def output_file(path: str, filename: str, html: str) -> None:
    os.makedirs(path, exist_ok=True)
    with open(path + filename, 'w') as f:
        f.write(html)

def merge_contents(contents: list) -> None:
    with open(DIST_DIR + '/data/contents.json', 'r+') as f:
        info = json.load(f)
        info += contents
        f.write(json.dumps(info))

def enable_comments() -> bool:
    pass
    
def commit() -> None:
    pass

# メイン処理
if __name__ == '__main__':
    main()
