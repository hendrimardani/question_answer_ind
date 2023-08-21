import argparse
import sys
import time
import random
from transformers import pipeline


if __name__ == "__main__":
    class color:
       PURPLE = '\033[95m'
       CYAN = '\033[96m'
       DARKCYAN = '\033[36m'
       BLUE = '\033[94m'
       GREEN = '\033[92m'
       YELLOW = '\033[93m'
       RED = '\033[91m'
       BOLD = '\033[1m'
       UNDERLINE = '\033[4m'
       END = '\033[0m'
    
    try:
        parser = argparse.ArgumentParser(description=f"{color.GREEN}Model has been trained by Hendri Mardani{color.END}")
        parser.add_argument('-f', '--file', type=str, required=True, help=f"Upload file berdasarkan lokasinya ektensi:{color.RED}[.txt]{color.END}")
        parser.add_argument('-m', '--model', type=str, required=True, help="Upload model pre-trained sesuai dengan lokasinya")
        args = parser.parse_args()
        
        file = args.file
        model = args.model
        token = model

        if file:
            with open(file) as f:
                context = f.read()

        def build_model(model, token, context, pertanyaan):
            qa_pipeline = pipeline(
            "question-answering",
            model=model,
            tokenizer=token
            )

            hasil = qa_pipeline({
                'context': context,
                'question': pertanyaan
            })

            return hasil["score"], hasil["answer"]

        def mengetik(s):
            for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(random.random() * 0.1)

        mengetik = mengetik(f"\nModel ini khusus yang berkaitan dengan {color.RED}context{color.END} yang di masukan!!....\
            \nUntuk pertanyaan bebas, selagi dalam {color.RED}context{color.END} yang dimasukkan.\nUntuk Keluar ketikan 'keluar'")

        def jawab2(s):
            for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(random.random() * 0.5)
            
            return c

        while True:
            print()
            mengetik
            pertanyaan = input(f"{color.GREEN}Mau tanya apa, tentang context yang di masukan? #>{color.END} ")

            if pertanyaan == "keluar":
                break

            score, jawab = build_model(model, token, context, pertanyaan)
            print()
            print(f"{color.YELLOW}================HASILNYA==========")
            print(f"{color.GREEN}Score: {score}")
            print(f"{color.PURPLE}Pertanyaan : {pertanyaan} {color.END}")
            # print(f"{color.RED}Jawab : {jawab} {color.END}")
            print(jawab2(f"{color.RED}Jawab : {jawab} {color.RED}"))
            print()
    except:
        print()
        print(f"{color.RED}Wajib pakai argument!!, ketik --help untuk bantuan{color.END}")
