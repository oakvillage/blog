from jsonschema import validate, ValidationError
import sys, os, json

def main() -> None:
    args = sys.argv

    contents = get_json_from_args(args)
    if contents is None or not validate_json_schema(contents):
        sys.exit('json error.')

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

# コマンドライン引数からjsonを取得する
def get_json_from_args(args: list) -> dict|list:
    if 3 == len(args) and args[2] == os.environ.get('DEPLOY_KEY') :
        try:
            js = json.loads(args[1])
            return js
        except json.JSONDecodeError as e:
            print(e)
        except:
            print('error.')
    else:
        print('Argments are not valid.')
    return None

# メイン処理
if __name__ == '__main__':
    main()
