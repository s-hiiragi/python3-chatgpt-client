import config
import sys
import cmd
import openai
import argparse

try:
    import readline
except:
    try:
        import pyreadline as readline
    except:
        pass


openai.api_key = config.OPENAI_API_KEY
model = 'text-davinci-003'


class ChatGpt(cmd.Cmd):

    prompt = '> '

    def __init__(self, args):
        super().__init__()
        self.args = args
        self.ans = ''

    def do_ask(self, line):
        response = openai.Completion.create(
                engine=model,
                prompt=line,
                max_tokens=1024,
                n=1,
                #temperature=0.5,
                temperature=0.9,
        )
        self.ans = response['choices'][0]['text']
        print(self.ans)

    def do_ans(self, line):
        print(self.ans)

    def do_exit(self, line):
        return self.do_EOF(line)

    def do_EOF(self, line):
        return True

    def emptyline(self):
        pass


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--prompt', help='Ask a prompt and exit')
    args = parser.parse_args()

    if args.prompt:
        ChatGpt(args).onecmd(f'ask {args.prompt}')
    else:
        try:
            ChatGpt(args).cmdloop()
        except KeyboardInterrupt:
            pass

    return 0


if __name__ == '__main__':
    result = main()
    if result:
        sys.exit(result)

