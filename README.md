### How to use

pip install -r requirement.txt
```
python3 utama.py --file {path file.txt} --model {path model question_answer_ind}
```

### For more information
```
python3 utama.py --help
```
### Models
Due to files > 25 mb, download the pre-trained model [here](https://drive.google.com/drive/folders/1GKQPdh0vATghcYpT1gZsH_Pf3nmVztDV?usp=drive_link)

### Datasets
Due to files > 25 mb, download datasets [here](https://drive.google.com/drive/folders/11kNG1oWC5uvGfNHhuKK7xoMcuEO9cTmR?usp=drive_link)

### Process stages
1. Import module.
2. Load datasets.
3. Separate the dataset between training data and test data (data validation)
4. Plotting data with the help of libraries such as: **matplotlib** or **seaborn**.
5. Perform text preprocessing which functions to process string data into token matrix form for processing by the machine.
6. Perform data prediction on the trained model, the goal is to see the results of the trained data.

### Training hyperparameters

- learning_rate: 2e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epochs | Step | Validation Loss |
| :---:         |     :---:      |          :---: | :------: |
|  1.5927  |  1.0  |  8156  |  1.7891  |
|  1.3008  |  2.0  |  16312  |  1.7875  |
|  1.0979  |  3.0  |  24468  |  1.8589  |

### Framework version

- Transformers 4.33.0.dev0
- Pytorch 2.0.0
- Datasets 2.1.0
- Tokenizers 0.13.3

##### NOTE:

- Total Training Data **130+ thousand lines**
- Total Test Data (Validation) **118+ thousand lines**
- Total Datasets **148+ thousand lines**
- Total Training hours **5.30 hours**
- Loss = 1.431

### Referensi
- [Matplotlib](https://matplotlib.org/)
- [Hugging Face](https://huggingface.co/)
- [Seaborn](https://seaborn.pydata.org/)
- [Pandas](https://pandas.pydata.org/)


![vokoscreenNG-2023-08-20_14-26-03](https://github.com/hendrimardani/question_answer_ind/assets/49816104/43b02d05-ed66-4450-b541-63bc1fa2608d)


