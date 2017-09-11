#!/usr/bin/env/ python3

import docker
import argparse 

def criar_container(args):
   client = docker.from_env()
   executando = client.containers.run(args.imagem, args.comando)
   print(executando)
   return(executando)

def listar_containers(args):
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

def procurar_container(args):
   client = docker.from_env()
   get_all = client.containers.list(all)
   for cada_container in get_all:
     conectando = client.containers.get(cada_container.id)
     imagem_container = conectando.attrs['Config']['Image']
     if str(args.imagem).lower() in str(imagem_container).lower():
      print("O container ID: {} NOME: {} ".format(cada_container.short_id, conectando.attrs['Name']))

def remover_container():
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


cmd = parser.parse_args()
cmd.func(cmd)



