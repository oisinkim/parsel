import time
from parsel import logger
from parsel.rund.conf import Config
from parsel.logger import exe
from parsel.logger import pipe


def install_datastax_debian_repos(config):
    if config.get_config("instance", "datastax_debian_attempted"):
        return
    exe('gpg --keyserver pgp.mit.edu --recv-keys 2B5C1B00')
    exe('gpg --export --armor 2B5C1B00 | sudo apt-key add -')
    exe('wget -O - http://installer.datastax.com/downloads/ubuntuarchive.repo_key | sudo apt-key add -')
    exe('wget -O - http://debian.datastax.com/debian/repo_key | sudo apt-key add -')
    exe('sudo rm /etc/apt/sources.list.d/datastax.sources.list', log=False, expectError=True)
    pipe('echo "deb http://debian.datastax.com/community stable main"',
                'sudo tee -a /etc/apt/sources.list.d/datastax.sources.list')
    pipe('curl -s http://installer.datastax.com/downloads/ubuntuarchive.repo_key', 'sudo apt-key add -')
    pipe('curl -s http://opscenter.datastax.com/debian/repo_key', 'sudo apt-key add -')
    pipe('curl -s http://debian.datastax.com/debian/repo_key', 'sudo apt-key add -')
    exe('sudo apt-get update')
    time.sleep(5)
    # Never install again
    logger.info("install_datastax_debian_repos done  .\n")
    config.set_config("instance", "datastax_debian_attempted", True)

if __name__ == "__main__":
    install_datastax_debian_repos(Config())