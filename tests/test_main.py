
from options.main import OptionAppTest

def test_options(tmp):
    with OptionAppTest() as app:
        res = app.run()
        print(res)
        raise Exception

def test_command1(tmp):
    argv = ['command1']
    with OptionAppTest(argv=argv) as app:
        app.run()
