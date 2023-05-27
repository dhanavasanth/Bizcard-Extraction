<img align="top" height = 400 alt="Coding" width="950" src="https://i.gifer.com/7XOw.gif">

<div style="padding-top:75.000%;position:relative;"><iframe src="https://gifer.com/embed/7XOw" width="100%" height="100%" style='position:absolute;top:0;left:0;' frameBorder="0" allowFullScreen></iframe></div><p><a href="https://gifer.com">via GIFER</a></p>

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
  
Once you have the reader object, you can use it to extract the information from the Biz_Card.
WHhen the Biz_Card is extracted, you will get the following information:

![data](https://github.com/dhanavasanth/Bizcard-Extraction/assets/117557948/2b6dab12-d08d-4a80-98bb-f85e18840588)">

## DATAFRAME

![dataframe](https://github.com/dhanavasanth/Bizcard-Extraction/assets/117557948/ce2e8b1c-ad0e-4e4f-8d4c-9d6a62dba77f)

## Creating a user_interface website using Streamlit

This helps user to upload their extracted buissness card information and upload it to SQLite database and it will provide a searchable user interface.

## Home

![home](https://github.com/dhanavasanth/Bizcard-Extraction/assets/117557948/0e336a74-7a54-4a4d-930b-e43f7eb22eeb)

## Search Interface

![search](https://github.com/dhanavasanth/Bizcard-Extraction/assets/117557948/2dfae0de-2372-4943-a523-4a7eca9e5591)

## Support

 email : danavasanth@gmail.com 

