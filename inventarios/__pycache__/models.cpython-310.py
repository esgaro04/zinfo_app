o
    G�4c{  �                   @   sF   d dl mZ d dlmZ d dlmZ d dlmZ G dd� dej�Z	dS )�    )�Delete)�
connection)�_MAX_LENGTH)�modelsc                   @   s�   e Zd Zejdd�Zejddd�Zejddd�Zej	dd�Z
ej	d	d�Zejd
d�Zejddd�Zej	dd�Zej	dd�Zejdd�ZdS )�	productosT)�primary_key�   �producto)�
max_length�verbose_nameZTipozValor entrada)r   zPrecio de ventazFecha de Vencimiento�2   ZDistribuidorZFacturasZCantidad)�defaultN)�__name__�
__module__�__qualname__r   �	AutoField�id�	CharFieldr	   Ztipo_producto�IntegerFieldZprecio_entradaZprecio_salida�	DateFieldZfecha_vencimientoZdistribuidorZfacturasZcantidad�BooleanFieldZactivo� r   r   �vC:\Users\Esteban Garcia\Documents\Documents\esteban garcia\Documents\pagina_zinfonia\admin_zinfo\inventarios\models.pyr      s    r   N)
�astr   �multiprocessingr   Zunittest.utilr   �	django.dbr   �Modelr   r   r   r   r   �<module>   s
    