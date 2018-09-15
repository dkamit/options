
from cement import App, TestApp, init_defaults
from cement.core.exc import CaughtSignal
from .core.exc import OptionAppError
from .controllers.base import Base
from tinydb import TinyDB
import os
from cement.utils import fs
from .controllers.items import Items
from .controllers.strategy import Strategy

# configuration defaults
CONFIG = init_defaults('options')
CONFIG['options']['db_file'] = '~/.options/db.json'
CONFIG['options']['foo'] = 'bar'

def extend_tinydb(app):
    app.log.info('extending options application with tinydb')
    db_file = app.config.get('options', 'db_file')
    
    # ensure that we expand the full path
    db_file = fs.abspath(db_file)
    app.log.info('tinydb database file is: %s' % db_file)
    
    # ensure our parent directory exists
    db_dir = os.path.dirname(db_file)
    if not os.path.exists(db_dir):
        os.makedirs(db_dir)
    app.extend('db', TinyDB(db_file))

class OptionApp(App):
    """Options primary application."""

    class Meta:
        label = 'options'

        # configuration defaults
        config_defaults = CONFIG

        # call sys.exit() on close
        close_on_exit = True

        # load additional framework extensions
        extensions = [
            'yaml',
            'colorlog',
            'jinja2',
        ]

        # configuration handler
        config_handler = 'yaml'

        # configuration file suffix
        config_file_suffix = '.yml'

        # set the log handler
        log_handler = 'colorlog'

        # set the output handler
        output_handler = 'jinja2'

        # register handlers
        handlers = [
            Items,
            Strategy
        ]

        # hooks
        hooks = [
            ('post_setup', extend_tinydb),
        ]


class OptionAppTest(TestApp,OptionApp):
    """A sub-class of OptionApp that is better suited for testing."""

    class Meta:
        label = 'options'


def main():
    with OptionApp() as app:
        try:
            app.run()

        except AssertionError as e:
            print('AssertionError > %s' % e.args[0])
            app.exit_code = 1

            if app.debug is True:
                import traceback
                traceback.print_exc()

        except OptionAppError:
            print('OptionAppError > %s' % e.args[0])
            app.exit_code = 1

            if app.debug is True:
                import traceback
                traceback.print_exc()

        except CaughtSignal as e:
            # Default Cement signals are SIGINT and SIGTERM, exit 0 (non-error)
            print('\n%s' % e)
            app.exit_code = 0


if __name__ == '__main__':
    main()
