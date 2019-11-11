#Challenge - 1

use publications;
select authors.au_id as ID_Autor, authors.au_lname as Nombre, authors.au_fname as Apellido, titles.title as Titulo, publishers.pub_name as Editorial
from authors
inner join titleauthor on authors.au_id=titleauthor.au_id
inner join titles on titles.title_id=titleauthor.title_id
inner join publishers on publishers.pub_id= titles.pub_id;

#Challenge - 2

select ID_Autor, Nombre, Apellido, Editorial, count(Titulo) as Num_Titulos
from (select authors.au_id as ID_Autor, authors.au_lname as Nombre, authors.au_fname as Apellido, titles.title as Titulo, publishers.pub_name as Editorial
from authors
inner join titleauthor on authors.au_id=titleauthor.au_id
inner join titles on titles.title_id=titleauthor.title_id
inner join publishers on publishers.pub_id= titles.pub_id) publicationsperauthor
group by ID_Autor, Editorial

#Challenge - 3

select authors.au_id as ID_Autor, authors.au_lname as Nombre, authors.au_fname as Apellido, sum(sales.qty) as Titulos_vendidos
from authors
inner join titleauthor on authors.au_id=titleauthor.au_id
inner join sales on sales.title_id=titleauthor.title_id
group by ID_Autor
order by Titulos_vendidos desc
limit 3;

#Challenge - 4

select authors.au_id as ID_Autor, authors.au_lname as Nombre, authors.au_fname as Apellido, sum(sales.qty) as Titulos_vendidos
from authors
inner join titleauthor on authors.au_id=titleauthor.au_id
inner join sales on sales.title_id=titleauthor.title_id
group by ID_Autor
order by Titulos_vendidos desc;






