<img align="top" height = 400 alt="Coding" width="950" src="media/ocr_bg.gif">

<h1 align="center">Biz_Card Extraction using Easy_OCR"</h1>

Extracting informations from the Biz_Card using Easy_OCR is a very simple task.

## Deployment

To deploy this project run

```bash
  pip install easyocr
  
  reader = easyocr.Reader(['ch_sim','en'])
```
This all, but with Regular Expressions...you will be able to segregate each info's in respective way.

```bash
  import regex as re
```
  
user info is extracted from the Biz_Card and stored in a database.

<img align="top" height = 200 alt="Coding" width="900" src="">

