# Modules
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
# Models
## zero shot classifier
1. Install ZSIC from given repo
2. You have to specify class by list of class ex. ["cat", "dog"]
```
pip install git+https://github.com/PrithivirajDamodaran/ZSIC.git
```

## tesseract ocr
1. Not only install pytesseract you have to install the tesseract package. <br>
2. Follow the instuction in the below link.
```
https://stackoverflow.com/questions/50951955/pytesseract-tesseractnotfound-error-tesseract-is-not-installed-or-its-not-i
```