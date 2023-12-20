#!/bin/bash

export OPENAI_API_KEY="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"

build() {
  docker build -t my_python_app .
}

run() {
  docker run -e OPENAI_API_KEY=${OPENAI_API_KEY} -v $(pwd):/app my_python_app
}

case "$1" in
  build)
    build
    ;;
  run)
    run
    ;;
  *)
    echo "Usage: $0 {build|run}"
    exit 1
    ;;
esac

exit 0
