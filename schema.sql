drop table if exists mims;
create table mims (
  id integer primary key autoincrement,
  url text not null,
  topText text not null,
  bottomText text not null,
  image text not null,
  dateAdded text not null
);

drop table if exists traffic;
create table mims (
  id integer primary key autoincrement,
  url text not null,
  dateVisited text not null
);

