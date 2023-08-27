### Cara Penggunaaan

pip install -r requirement.txt
```
python3 utama.py --file {lokasi file.txt} --model {lokasi model question_answer_ind}
```

### Untuk keterangan selengkapnya
```
python3 utama.py --help
```
### Models
Dikarenakan file > 25 mb, download model pre-trained [disini](https://drive.google.com/drive/folders/1GKQPdh0vATghcYpT1gZsH_Pf3nmVztDV?usp=drive_link)

### Datasets
Dikarenakan file > 25 mb, download datasets [disini](https://drive.google.com/drive/folders/11kNG1oWC5uvGfNHhuKK7xoMcuEO9cTmR?usp=drive_link)

### Tahap-tahap proses
1. Import module.
2. Load datasets.
3. Pisahkan datasets antara data training dengan data test(data validation)
4. Ploting data dengan menggunakan bantuan library seperti: **matplotlib** atau **seaborn**. Tujuannya adalah untuk meihat sebaran data, jumlah data, pola data, dll.
5. Melakukan Text Preprocessing yang berfungsi untuk memproses data string kedalam bentuk token matrix untuk diproses oleh mesin.
6. Load model yang sudah dilatih(pre-trained model)
7. Lakukan prediksi data pada model yang sudah dilatih, tujuannya adalah untuk melihat hasil dari data yang sudah dilatih. Pada tahap ini biasanya dimasukan kedalam tahap akhir (**Evaluation**).

### Training hyperparameters

The following hyperparameters were used during training:

-

##### NOTE:

- Total Data Training **130+rb baris**
- Total Data Test(Validation) **118+rb baris**
- Total Dataset **148+rb baris**
- Total jam training **5.30 jam**
- Loss = 1.431

### Referensi
- [Matplotlib](https://matplotlib.org/)
- [Hugging Face](https://huggingface.co/)
- [Seaborn](https://seaborn.pydata.org/)
- [Pandas](https://pandas.pydata.org/)


![vokoscreenNG-2023-08-20_14-26-03](https://github.com/hendrimardani/question_answer_ind/assets/49816104/43b02d05-ed66-4450-b541-63bc1fa2608d)


