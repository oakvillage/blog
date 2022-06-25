import sys, os

def main():
    contents = args = sys.argv[1]
    deploy_key = sys.argv[2]
    if deploy_key == os.environ.get('DEPLOY_KEY'):
        print(contents)
    else:
        print('deploy_key invalid.')

# メイン処理
if __name__ == '__main__':
    main()
