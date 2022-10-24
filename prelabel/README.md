rabbitmq
```
docker run --rm -it -p 15672:15672 -p 5672:5672 rabbitmq:3-management
```

python 3.9

```
# for pip
pip install -r requirements.txt
```

```
# for conda
conda env create -f rabbitmq-env.yml
conda activate rabbitmq-env
```