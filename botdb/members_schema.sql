--members_schema.sql

-- The bot keeps track of relationships with members, and the names they prefer
create table member (
    name        text primary key,
    relationship text,
    nickname text
);
