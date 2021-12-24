<h1 align="center">Image Fingerprint</h1> 

[![capa](img/capa.png "capa")](https://www.nytimes.com/newsgraphics/2014/02/14/fashion-week-editors-picks/index.html "capa") 

![](https://img.shields.io/static/v1?label=python&message=3.8.8&color=blue&style=for-the-badge&logo=PYTHON) 
![](https://img.shields.io/static/v1?label=R&message=3.6.1&color=blue&style=for-the-badge&logo=R)


> Status do Projeto: ✔️ Concluído

### Sumário 

- [Descrição do projeto](#descrição-do-projeto)
- [Pré-requisitos](#pré-requisitos)
- [Como usar](#como-usar)
- [Inspiração](#inspiração)
- [Crédito das imagens](#crédito-das-imagens)
- [Licença](#licença)
 


## Descrição do projeto 

<p align="justify">
	O script analisa a imagem fornecida obtendo a moda dos valores de cada linha de pixel presente na imagem, formando outra de mesmas dimensões com a moda das linhas. Foram feitas duas versões, uma em python e a outra em R.
</p>


## Pré-requisitos

1. [Python](https://www.python.org/downloads/)
	- [pillow](https://pillow.readthedocs.io/en/stable/index.html)
	- [statistics](https://docs.python.org/3.9/library/statistics.html?highlight=mode#)
2. [R](https://www.r-project.org/)
	- [magick](https://cran.r-project.org/web/packages/magick/vignettes/intro.html)
	- [modeest](https://cran.r-project.org/web/packages/modeest/index.html)



## Como usar

No terminal, clone o projeto: 

```
git clone https://github.com/GuilhermeRinaldi/image_fingerprint
```

No arquivo coloque as informações de origem e destino da imagem, para python: 

```python
img = Image.open('name + .extension')
...
out.save('name + .extension')
```
**Para imagens no mesmo local do arquivo**

Para R:
```R
img <- image_read('path/name + .extension')
...
image_write(out, path = "name + .extension", format = "extension")
```
Agora basta rodar o script.

**Devido ao funcionamento é recomendavel o recorte da imagem para melhores resultados**

[![exemplo de corte](img/exemplo_de_corte.png "exemplo de corte")](https://www.nytimes.com/newsgraphics/2014/02/14/fashion-week-editors-picks/index.html "exemplo de corte")


## Inspiração

Inspirado pelo texto [Create Fashion Fingerprints with R](https://www.r-bloggers.com/2014/10/create-fashion-fingerprints-with-r/ "Create Fashion Fingerprints with R").

## Crédito das imagens 

As imagens foram retiradas de [Front Row to Fashion Week 2014](https://www.nytimes.com/newsgraphics/2014/02/14/fashion-week-editors-picks/index.html "Front Row to Fashion Week 2014")                  

## Licença 

The [MIT License]() (MIT)

Copyright © 2021 - Image Fingerprint
                                                      
