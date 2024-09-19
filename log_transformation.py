from datetime import datetime
import csv

with open("sample_auth_log_10000_Sep_12_24.txt", "r") as f:
    conteudo = f.read().splitlines()

nome_arquivo_csv = "logs-auth.csv"
HEADERS = ["Timestamp","Service","Message"]
dados = []
for linha in conteudo:
    # Separando a linha para extrair infos
    linha_split = linha.split(" ")
    # Extraindo os dados
    if linha_split[1]=="": # Caso de linhas que têm dois espaços após o mês abrev. 
        timestamp = f"{linha_split[2]} {linha_split[0]}, 2024 {linha_split[3]}"
        servico = linha_split[5].replace(":","").split('[')[0]
        msg_log_list = linha.split(" ")[6:]
        msg_final = ""
        for m in msg_log_list:
            msg_final= " ".join(msg_log_list)
    else:
        timestamp = f"{linha_split[1]} {linha_split[0]}, 2024 {linha_split[2]}"
        servico = linha_split[4].replace(":","").split('[')[0]
        msg_log_list = linha.split(" ")[5:]
        msg_final = ""
        for m in msg_log_list:
            msg_final= " ".join(msg_log_list)
    timestamp_obj = datetime.strptime(timestamp,"%d %b, %Y %H:%M:%S")
    timestamp_final_str = str(timestamp_obj)
    dados.append([timestamp_final_str,servico,msg_final])

with open(nome_arquivo_csv, "w", newline='') as csvfile:
    writer = csv.writer(csvfile)
    dados.insert(0,HEADERS)
    writer.writerows(dados)