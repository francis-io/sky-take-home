## TLDR Instructions
`make lint && make test`

`make build && docker run lotto-results:latest 10,10,10,10,10,10`
or
`python3 main.py 10,10,10,10,10,10`

## Requirements

* Python > 3.8 (for math.prod())
or
* Docker
* Make (optional)

This was tested on Ubuntu 20.04. Anything else, YMMV.

## notes

* I tried to not have any extra dependancies to keep things simple
* I don't use true random numbers for the winning numbers
* I don't deal with duplicate numbers at all
* I don't deal with floats at all
