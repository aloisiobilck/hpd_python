#!/usr/bin/env/ python3

import docker 


def criar_container(imagem, comando):
   client = docker.from_env()
   executando = client.containers.run(imagem, comando)
   print(executando)



def listar_containers():

   client = docker.from_env()
   get_all = client.containers.list(all)
   for cada_container in get_all:
     conectando = client.containers.get(cada_container.id)
     print("O container da vez eh o %s utiliza a imagem %s e o comendo %s"  % (conectando.short_id, conectando.attrs['Config']['Image'], conectando.attrs['Config']['Cmd']))


def procurar_container(imagem):
   client = docker.from_env()
   get_all = client.containers.list(all)
   for cada_container in get_all: 
     conectando = client.containers.get(cada_container.id)
     imagem_container = conectando.attrs['Config']['Image']
     if str(imagem).lower() in str(imagem_container).lower():
      print("Achei o container %s que contem a palavra %s no nome de sua imagem: %s" % (cada_container.short_id, imagem, imagem_container))

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


#criar_container("alpine","echo FUDEU!!! VAIII")
#listar_containers()
#procurar_container("nginx")
#remover_container()
