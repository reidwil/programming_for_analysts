info() {
  printf "\r\033[00;35m$1\033[0m\n"
}

success() {
  printf "\r\033[00;32m$1\033[0m\n"
}

fail() {
  printf "\r\033[0;31m$1\033[0m\n"
}

search(){
    if [ -z "$2" ]
    then
        history | grep $1
    else
        history $1 | grep $2
    fi
}

run_last(){
    if [ -z "$1" ]
        then
            fail "There were no arguments passed"
            exit
    else
        output=$(search -1 $1)
        success $output
    fi
}

require(){
    req_tools=("$@")
    for tool in "${req_tools[@]}"; do
    if ! command -v "$tool" > /dev/null; then
        fail "It looks like '${tool}' is not installed; please install it and run this setup script again."
        exit
    fi
    done
}

dbt_profile(){
    cat $HOME/.dbt/profiles.yml
}

lets(){
    info "${@}"
}

create_venv() {
    info "Creating virtual environment in $1"
    python3 -m venv $1
}

go_to_vent() {
    info "Hopping into your virtual environment"
    source $1/bin/activate
}

reids_venv() {
    if [ -z "$1" ]
    then
        DIR=./env
    else
        DIR=$1
    fi
    create_venv $DIR
    go_to_vent $DIR
}