from fabric.api import local, cd, run, env

env.hosts = ['cloud']


def deploy():
    local('git push')
    with cd('~/eventme'):
        run('git pull')
        run('pipenv install')
