o
    ��5c/  �                   @   s�   d dl mZ d dlmZ d dlmZ d dlmZmZ d dl	m
Z
 ddlmZ ddlmZ d	d
� Zdd� Zdd� Zdd� Zdd� Zdd� Zdd� ZdS )�    )�product)�
connection)�flags)�render�redirect��HttpResponse�   )�	productos)�productosFormc                 C   s   t d�S )NZjuanr   ��request� r   �uC:\Users\Esteban Garcia\Documents\Documents\esteban garcia\Documents\pagina_zinfonia\admin_zinfo\inventarios\views.py�inicio   s   r   c                 C   �
   t | d�S )Nzoperadores/login.html�r   r   r   r   r   �login   �   
r   c                 C   s   t jjdd�}t| dd|i�S )NT)�activozpaginas/menu.html�paginas)r
   �objects�filterr   )r   r   r   r   r   r      s   r   c                 C   r   )Nzoperadores/sign.htmlr   r   r   r   r   �sign   r   r   c                 C   s6   t | jpd �}|�� r|��  td�S t| dd|i�S )Nr   zpaginas/agregar.html�
formulario)r   �POST�is_valid�saver   r   )r   r   r   r   r   �agregar   s
   r   c                 C   s   t jj|d�}|��  td�S )N��idr   )r
   r   �get�deleter   )r   r    r   r   r   r   �eliminar   s   r#   c                 C   s0   t jj|d�}t| jpd t d�}t| dd|i�S )Nr   )�instancezpaginas/editar.htmlr   )r
   r   r!   r   r   r   )r   r    r   r   r   r   �editar"   s   r%   N)�	itertoolsr   Zmultiprocessing.dummyr   �sysr   Zdjango.shortcutsr   r   �django.httpr   �modelsr
   �formsr   r   r   r   r   r   r#   r%   r   r   r   r   �<module>   s    