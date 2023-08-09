import os
from consultas.cpf import consultar_api_cpf
from consultas.email_consulta import consultar_api_email
from consultas.telefone import consultar_api_telefone
from consultas.nome import consultar_api_nome
from datetime import datetime

def save_to_file(data, filename):
    try:
        with open(filename, "w") as file:
            file.write(data)
            print(f"Resultado salvo em {filename}")
    except Exception as e:
        print(f"Erro ao salvar o resultado: {e}")

def generate_filename(opcao):
    return f"{opcao}.txt"

def formatar_data(data_str):
    if data_str:
        data_obj = datetime.strptime(data_str, '%Y-%m-%d %H:%M:%S')
        return data_obj.strftime('%d/%m/%Y')
    return ""

def formatar_telefones(telefones):
    telefone_str = "\n".join([f"({telefone['DDD']}) {telefone['TELEFONE']}" for telefone in telefones])
    return telefone_str

def formatar_enderecos(enderecos):
    endereco_str = "\n".join([f"{endereco['LOGR_TIPO']} {endereco['LOGR_NOME']}, {endereco['LOGR_NUMERO']} - {endereco['BAIRRO']}, {endereco['CIDADE']}/{endereco['UF']} - {endereco['CEP']}" for endereco in enderecos])
    return endereco_str

def main():
    os.system("cls")
    os.system("color 2")
    print("██████╗  █████╗ ████████╗ ██████╗ ██████╗  ██████╗ ████████╗")
    print("██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗██╔═══██╗╚══██╔══╝")
    print("██████╔╝███████║   ██║   ██║   ██║██████╔╝██║   ██║   ██║   ")
    print("██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗██║   ██║   ██║   ")
    print("██║  ██║██║  ██║   ██║   ╚██████╔╝██████╔╝╚██████╔╝   ██║   ")
    print("╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═════╝  ╚═════╝    ╚═╝   ")
    print("                                                               ")
    print("                Painel de Buscas by Kinuzo                     ")
    print("                                                               ")
    print("Menu de Consultas:")
    print(" ___________________ ")
    print("|                   |")
    print("|   1 - CPF         |")
    print("|   2 - Nome        |")
    print("|   3 - Email       |")
    print("|   4 - Telefone    |")
    print("|___________________|")
    print("                                                               ")
    opcao = input("Escolha uma opção (1/2/3/4): ")
    
    if opcao == "1":
        cpf = input("Digite o CPF que deseja consultar: ")
        resultado = consultar_api_cpf(cpf)
        
        if resultado:
            data = resultado['results']
            formatted_data = f"""
• CPF: {data['CPF']}
• RG: {data['RG']}
• ORGÃO EXPEDIDOR: {data['ORGAO_EMISSOR']}

• NOME: {data['NOME']}
• NASCIMENTO: {formatar_data(data['NASC'])}
• SEXO: {data['SEXO']}

• MÃE: {data['NOME_MAE']}
• PAI: {data['NOME_PAI']}

• NACIONALIDADE: {data.get('NACIONALIDADE', '')}
• RENDA: {data.get('RENDA', '')}

• ENDEREÇOS:
{formatar_enderecos(data['enderecos'])}

• TELEFONES PROPRIETÁRIO:
{formatar_telefones(data['telefones'])}
"""
            print("Resultado da consulta:")
            print(formatted_data)
            
            filename = "resultado.txt"
            save_to_file(str(formatted_data), filename)
        else:
            print("Consulta não foi bem-sucedida.")
            
    elif opcao == "2":
        nome = input("Digite o nome que deseja consultar: ")
        resultado = consultar_api_nome(nome)
        
        if resultado:
            data = resultado['results'][0]
            formatted_data = f"""
• CPF: {data['CPF']}
• NOME: {data['NOME']}
• NASCIMENTO: {formatar_data(data['NASC'])}
• NOME MÃE: {data['NOME_MAE']}
• NOME PAI: {data['NOME_PAI']}
• RG: {data['RG']}
• ORGÃO EMISSOR: {data['ORGAO_EMISSOR']}
• SEXO: {data['SEXO']}
• RENDA: {data['RENDA']}
"""

            print("Resultado da consulta:")
            print(formatted_data)
            
            filename = "resultado.txt"
            save_to_file(str(formatted_data), filename)
        else:
            print("Consulta não foi bem-sucedida.")
            
    elif opcao == "3":
        email = input("Digite o email que deseja consultar: ")
        resultado = consultar_api_email(email)
    
        if resultado:
            data = resultado['results'][0]
            formatted_data = f"""
• CPF: {data['CPF']}
• NOME: {data['NOME']}
• NASCIMENTO: {formatar_data(data['NASC'])}
• NOME MÃE: {data['NOME_MAE']}
• NOME PAI: {data['NOME_PAI']}
• RG: {data['RG']}
• ORGÃO EMISSOR: {data['ORGAO_EMISSOR']}
• SEXO: {data['SEXO']}
• RENDA: {data['RENDA']}
"""
            print("Resultado da consulta:")
            print(formatted_data)
            
            filename = "resultado.txt"
            save_to_file(str(formatted_data), filename)
        else:
            print("Consulta não foi bem-sucedida.")
            
    elif opcao == "4":
        telefone = input("Digite o telefone que deseja consultar: ")
        resultado = consultar_api_telefone(telefone)
        
        if resultado and 'results' in resultado:
            data = resultado['results']
            formatted_data = f"""
• CPF: {data['CPF']}
• NOME: {data['NOME']}
• NASCIMENTO: {formatar_data(data['NASC'])}
• NOME MÃE: {data['NOME_MAE']}
• NOME PAI: {data['NOME_PAI']}
• RG: {data['RG']}
• ORGÃO EMISSOR: {data['ORGAO_EMISSOR']}
• SEXO: {data['SEXO']}
• RENDA: {data['RENDA']}
"""
            print("Resultado da consulta:")
            print(formatted_data)
            
            filename = "resultado.txt"
            save_to_file(str(formatted_data), filename)
        else:
            print("Consulta não foi bem-sucedida.")
            
    else:
        print("Opção inválida.")

if __name__ == "__main__":
    main()
