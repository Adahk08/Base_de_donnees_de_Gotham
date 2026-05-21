# Gotham Series – Database Creation Project

## Overview
This project involves building a relational database from scratch for the TV series **Gotham**,
combining web scraping, data modeling and SQL to collect, structure and store all series data.

## Project Steps

### 1. Conceptual Data Modeling (MCD)
- Designed the conceptual data model (MCD) to structure entities and relationships
- Entities : Characters, Episodes, Seasons, Actors, Locations

### 2. Data Collection – Web Scraping
- Scraped data from web sources using **BeautifulSoup** and **Requests**
- Collected : character names, episode titles, broadcast dates, cast information

### 3. Database Creation – PostgreSQL
- Created tables based on the MCD using SQL (DDL)
- Inserted scraped data using Python + **psycopg2**
- Applied constraints : primary keys, foreign keys, data integrity

## Technologies Used

| Tool | Usage |
|------|-------|
| Python | Web scraping, data insertion |
| BeautifulSoup | HTML parsing |
| Requests | HTTP requests |
| PostgreSQL | Relational database |
| psycopg2 | Python-PostgreSQL connector |
| SQL | DDL & DML |

## Key Skills Demonstrated
- Conceptual data modeling (MCD)
- Web scraping and data collection
- Database design and management
- Python-SQL integration

## Author
Adama Diallo – BUT Science des Données – IUT de Carcassonne
