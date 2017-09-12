#!/usr/bin/env/ python3.6

import docker, argparse, sys
from datetime import datetime

def logando(mensagem, e, logfile="docker-cli.log"):
   data_atual = datetime.now().strftime('%d/%m/%Y %H:%M')
   with open("docker-cli.log",'a') as log:
     texto = "%s \t %s \t %s \n" % (data_atual, mensagem, str(e))
     log.write(texto)


def criar_container(args):
   try:
      client = docker.from_env()
      executando = client.containers.run(args.imagem, args.comando)
      return(executando)
   except docker.errors.ImageNotFound as e:
     #print('Erro: Essa imagem nao existe!', sys.exc_info()[0])
     logando('Erro: Essa imagem nao existe!', e)
   except docker.errors.NotFound as e:
     logando('Erro: Esse comando nao existe', e)
   except Exception as e:
     logando('Erro! Favor verificar o comando digitado', e)
   finally:
     print('Comando executado')


def listar_containers(args):
   try: 
      client = docker.from_env()
      if args.todos:
        get_all = client.containers.list(all)
        for cada_container in get_all:
          conectando = client.containers.get(cada_container.id)
          print("O container da vez eh o %s utiliza a imagem %s e o comando %s"  % (conectando.short_id, conectando.attrs['Config']['Image'], conectando.attrs['Config']['Cmd']))
        else:
          get_exec = client.containers.list()
          for cada_container in get_exec:
            conectando = client.containers.get(cada_container.id)
            print('O container em execução eh ID: {} | NOME: {}  | CMD: {} '.format(conectando.short_id, conectando.attrs['Name'], conectando.attrs['Config']['Cmd']))
   except Exception as e:
    logando('Erro! Nenhum container para listar', e)

def procurar_container(args):
   try: 
     client = docker.from_env()
     get_all = client.containers.list(all)
     for cada_container in get_all:
       conectando = client.containers.get(cada_container.id)
       imagem_container = conectando.attrs['Config']['Image']
       if str(args.imagem).lower() in str(imagem_container).lower():
         print("O container ID: {} NOME: {} ".format(cada_container.short_id, conectando.attrs['Name']))
   except Exception as e:
     logando('Erro! Nenhum container encontrado')

def remover_container(args):
   client = docker.from_env()
   get_all = client.containers.list(all)

   for i in get_all:
     conecta = client.containers.get(i.id)
     portas = conecta.attrs['HostConfig']['PortBindings']
     if isinstance(portas,dict):
       for porta, porta1 in portas.items():
         porta1 = str(porta1)
         porta2 = ''.join(filter(str.isdigit, porta1))
         if int(porta2) <= 1024:
           print("Removendo o container %s que esta escutando na porta %s e bindando no host na porta %s" % (i.short_id, porta, porta2))
           removendo = i.remove(force=True)


parser = argparse.ArgumentParser(description="docker-cli criando na aula de python")
subparser = parser.add_subparsers()

criar_opt = subparser.add_parser('criar')
criar_opt.add_argument('--imagem', required=True)
criar_opt.add_argument('--comando', required=True)
criar_opt.set_defaults(func=criar_container)

criar_opt = subparser.add_parser('listar')
criar_opt.add_argument('--todos', action='store_true', help='TODOS os containers')
criar_opt.set_defaults(func=listar_containers)

criar_opt = subparser.add_parser('procurar')
criar_opt.add_argument('--imagem', required=True, help='Nome da imagem')
criar_opt.set_defaults(func=procurar_container)

criar_opt = subparser.add_parser('remover')
criar_opt.add_argument('--imagem', required=True, help='Nome da imagem')
criar_opt.set_defaults(func=procurar_container)


cmd = parser.parse_args()
cmd.func(cmd)
