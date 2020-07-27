from fabric.api import local


def bash():
    local("docker exec -it $(docker ps | grep server_ | awk '{{ print $1 }}') bash")


def dev():
    local("docker-compose run --rm --service-ports server")


def kill():
    local("docker kill $(docker ps -q)")


def load():
    local("docker exec -it $(docker ps | grep server_ | awk '{{ print $1 }}') python /server/load_employees.py")
