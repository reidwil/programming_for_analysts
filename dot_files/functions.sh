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
            echo "There were no arguments passed"
            exit
    else
        output=$(search -1 $1)
        echo $output
    fi
}

require(){
    req_tools=("$@")
    for tool in "${req_tools[@]}"; do
    if ! command -v "$tool" > /dev/null; then
        fail "It looks like '${tool}' is not installed; please install it and run this setup script again."
        exit 1
    fi
    done
}

lets(){
    echo "${@}"
}