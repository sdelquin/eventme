from fabric.api import local, prefix, cd, run, env

env.hosts = ["production"]


def deploy():
    local("git push")
    with prefix("source ~/.virtualenvs/eventme/bin/activate"):
        with cd("~/eventme"):
            run("git pull")
            run("pip install -r requirements.txt")
