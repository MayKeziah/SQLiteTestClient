-- "Query: list all places that projects are taking place at."
select distinct(name)
from PLACE, PROJECT
where name = location;