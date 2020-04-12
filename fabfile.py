from fabric.api import local, cd, run, env, prefix

env.hosts = ['cloud']


def deploy():
    local('git push')
    with prefix('source ~/.virtualenvs/bin/activate'):
        with cd('~/eventme'):
            run('git pull')
            run('pip install -r requirements.txt')
