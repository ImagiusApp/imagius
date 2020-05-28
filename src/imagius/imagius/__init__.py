from imagius.constants import HUMAN_APP_NAME
from imagius import init


def run(argv):
    init.init_app_data_dir()
    from imagius.log import LOGGER
    LOGGER.info(
        '======================================Imagius starting up=======================================')
    init.init_app_db()

    from imagius import settings
    settings.load_settings()
