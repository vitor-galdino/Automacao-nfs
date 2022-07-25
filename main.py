from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from rich import print
from rich.progress import track
import os, datetime, smtplib, keyboard
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders
from user_Email import login_address, password_address

list_wash = []
total = 0
checker_1 = '1'
checker_2 = '2'
checker_3 = '3'

os.system('cls')
while True:
    print('[bold bright_white]Escolha as opções de serviços de sua preferência:\n')
    try:
        print(f'[strike][1] Lavagem de peças finas.[/]    [green]R$ 29,90  {finasOK}')
    except:
        print('[1] Lavagem de peças finas.    [green]R$ 29,90')

    try:
        print(f'[strike][2] Lavagem de peças pesadas.[/]  [green]R$ 59,60  {pesadasOK}')
    except:
        print('[2] Lavagem de peças pesadas.  [green]R$ 59,60')
    
    try:
        print(f'[strike][3] Lavagem completa.[/]          [green]R$ 99,20  {completaOK}\n')
    except:
        print('[3] Lavagem completa.          [green]R$ 99,20\n')
    
    print('[0] Para continuar.') 
    print('[9] Para escolher novamente os serviços.\n')
    toWash = input('Digite a opção desejada:\n>> ') 

    services_choices = [checker_1, checker_2, checker_3, '0', '9']
    if toWash not in services_choices:
        os.system('cls')
        print('[bright_red]Nenhuma opção foi catalogada!')
        print('[white]Você deve ter escolhido o mesmo serviço ou nenhuma opção. [/][bright_red]Tente novamente!')
        print('\n[white]Pressione [bold bright_white]ENTER[/] para continuar...')
        input()
        os.system('cls')

    if toWash == checker_1:
        finasUnit = input('\nQuanta lavagens de peças finas será feito?\n>> ')
        list_wash.append(f'{finasUnit}x Lavagem de peças finas.           R$ 29,90')
        finasTimes = int(finasUnit)
        finasScore = finasTimes * 29.90
        total += finasScore
        finasOK = '[white](Opção catalogada!)'
        checker_1 = 'none_1'
        os.system('cls')

    elif toWash == checker_2:
        pesadasUnit = input('\nQuantas lavagens de peças pesadas será feito?\n>> ')
        list_wash.append(f'{pesadasUnit}x Lavagem de peças pesadas.         R$ 59,60')
        pesadasTimes = int(pesadasUnit)
        pesadasScore = pesadasTimes * 59.60
        total += pesadasScore
        pesadasOK = '[white](Opção catalogada!)'
        checker_2 = 'none_2'
        os.system('cls')

    elif toWash == checker_3:
        completaUnit = input('\nQuantas lavagens completas será feita?\n>> ')
        list_wash.append(f'{completaUnit}x Lavagem completa.                 R$ 99,20')
        completaTimes = int(completaUnit)
        completaScore = completaTimes * 99.20
        total += completaScore
        completaOK = '[white](Opção catalogada!)'
        checker_3 = 'none_3'
        os.system('cls')

    elif toWash == '9':
        os.system('cls')
        print('[bright_yellow]Resetando opções de serviços...')
        sleep(2)
        os.system('python main.py')

    elif toWash == '0':
        break

os.system("cls")
print("[bold bright_white]Informações do cliente:\n")
name = input("Nome: ")
city = input("Cidade: ")
cpf = input("CPF: ")
email = input("Email: ")

os.system('cls')
print("[bold bright_red]Confira se os dados estão certos!\n")
print(f"[bright_white]Nome: {name}\nCidade: {city}\nCPF: {cpf}\nEmail: {email}\n\nDescrição de serviços:\n")
for buy_list in list_wash:
    print(f'[bright_white]{buy_list}')

# converção numérica para o formato brasileiro
total = f'R$ {total:_.2f}'
total = total.replace('.', ',').replace('_', '.')
print(f'\n[bright_white]Valor Total: {total}')

print('\n\n[white]Está tudo certo?')
print('Pressione [bold bright_white]ENTER[/] para confirmar ou [bold bright_white]ESC[/] para cancelar.')
while True:   
    if keyboard.is_pressed('enter'):
        print('[green]Informações confirmadas!')
        break
    
    elif keyboard.is_pressed('esc'):
        os.system('cls')
        print('[bright_red]Informações não confirmadas!')
        print('[white]Voltando ao menu de serviços...')
        sleep(2.3)
        os.system('python main.py')

date = datetime.datetime.now()
dateToday = f'({date.day}-{date.month}-{date.year}){date.hour}h{date.minute}m [{date.second}s]'
NFSdate = f'INFORMAÇÕES ADICIONAIS\n\nNota fiscal emitida em:\nData: {date.day}/{date.month}/{date.year}   Hora: {date.hour}:{date.minute}'

archive = open(f"{name}{dateToday}.txt", "a")
archive.write(f"Nome: {name}\nCidade: {city}\nCPF: {cpf}\n\nDescrição de serviços:\n")
for buy_list in list_wash:
    archive.write(f'{buy_list}\n')
archive.write(f'\nValor Total:\n{total}\n\n\n{NFSdate}')
archive.close()

driver = webdriver.Chrome()
driver.minimize_window()
driver.implicitly_wait(15)

print('\n\n\n[bold bright_white]Cadastrando cliente...\n')
sleep(3)
os.system('cls')
print('[bold bright_white]Cadastro finalizado.\n')
print('[bold bright_white]Gerando[/] [bold bright_red]NOTA FISCAL[/][white]...')

driver.get("https://www.adobe.com/br/acrobat/online/convert-pdf.html")
# coloque o caminho do arquivo .txt aqui
driver.find_element(By.ID, "fileInput").send_keys(f"C:\\Users\YourPCName\OneDrive\Documentos\Automacao-nfs\{name}{dateToday}.txt")
driver.find_element(By.XPATH, '//*[@id="dc-hosted-11d0ce3a"]/div/div/div[2]/div/section[2]/div/div[1]/div[2]/button[1]').click()
print('[bold bright_white]Formatando para PDF...')
sleep(8)
print('[bold bright_white]Nota Fiscal gerada.\n\nArmazenando Nota Fiscal...')
os.remove(f'{name}{dateToday}.txt')

try:
    os.mkdir(f'Clientes/{name}')

except:
    print('\n[bold bright_green]Cliente já registrado! Armazenando Nota Fiscal em seu registro...')

# coloque o caminho do arquivo pdf de sua paste de download aqui
os.rename(f'C:\\Users\YourPCName\Downloads\{name}{dateToday}.pdf', f'Clientes/{name}/{name}{dateToday}.pdf')
sleep(3)
print('[bold bright_yellow]Nota Fiscal armazenada.\n\n\n')

print('[bold bright_white]Enviando Nota Fiscal para o email do destinatário...')
msg = MIMEMultipart()
msg['Subject'] = 'Nota Fiscal'
msg['From'] = login_address
msg['To'] = email
body = f"Prazer {name}, sua nota fiscal a seguir: "

msg.attach(MIMEText(body, 'plain')) 
filename = f"{name}{dateToday}.pdf"
# coloque o caminho do arquivo pdf da pasta Clientes aqui
attachment = open(f"C:\\Users\YourPCName\OneDrive\Documentos\Automacao-nfs\Clientes\{name}/{name}{dateToday}.pdf", "rb") 
p = MIMEBase('application', 'octet-stream') 
p.set_payload((attachment).read()) 
encoders.encode_base64(p) 
   
p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
msg.attach(p) 
s = smtplib.SMTP('smtp.gmail.com', 587) 
s.starttls() 
s.login(login_address, password_address) 
text = msg.as_string() 
s.sendmail(login_address, email, text) 
s.quit() 

for task in track(range(50),'[cyan][bold]Enviando email...[/]'):
    sleep(0.1)
print('[bold bright_green]Email enviado.')
driver.quit()