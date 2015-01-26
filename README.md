# cache-storing

The goal of this project is to provide an restful api storing and getting freshest data.
There is no guarantee for the coherence of data. 

## Installation:

```shell
git clone https://github.com/jlzirani/cache-storing.git
cd cache-storing
virtualenv --distribute --no-site-packages ve
source ve/bin/activate
pip install -r requirements.txt
```

## Run :

```shell
source ve/bin/activate # Do only once (if it's a new tty)
python restStore.py
```

## How to use:
We suppose that the server is running on the following address: 127.0.0.1:5000

### storing data:
It is done by upload data on the field "data" on http://127.0.0.1:5000/store

```shell
curl --form 'data=["t","h","e","g"]' http://127.0.0.1:5000/store
```

Result:
```shell
{"success": "ok"}
```

### getting data:
It is done by fetching http://127.0.0.1:5000/get
```shell
curl --form 'data=["t","h","e","g"]' http://127.0.0.1:5000/store
```

result:
```shell
["t","h","e","g"]
```

### flushing data:
It is done by etching http://127.0.0.1:5000/flush

result:
```shell
{"success": "ok"}
```
