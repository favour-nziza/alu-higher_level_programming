# SQL - More queries

MySQL users and privileges, constraints (`NOT NULL`, `UNIQUE`, `DEFAULT`,
`PRIMARY KEY`, `FOREIGN KEY`), subqueries and `JOIN`s.

| File | Description |
|------|-------------|
| 0-privileges.sql | Privileges of user_0d_1 and user_0d_2 |
| 1-create_user.sql | Create user_0d_1 with all privileges |
| 2-create_read_user.sql | Create hbtn_0d_2 and read-only user_0d_2 |
| 3-force_name.sql | Table `force_name` (name NOT NULL) |
| 4-never_empty.sql | Table `id_not_null` (id DEFAULT 1) |
| 5-unique_id.sql | Table `unique_id` (id DEFAULT 1 UNIQUE) |
| 6-states.sql | Database hbtn_0d_usa and table `states` |
| 7-cities.sql | Table `cities` with a foreign key to `states` |
| 8-cities_of_california_subquery.sql | Cities of California using a subquery |
| 9-cities_by_state_join.sql | Cities with their state using a JOIN |
| 10-genre_id_by_show.sql | Shows with at least one genre |
| 11-genre_id_all_shows.sql | All shows, NULL when no genre |
| 12-no_genre.sql | Shows without a genre |
| 13-count_shows_by_genre.sql | Number of shows per genre |
| 14-my_genres.sql | Genres of Dexter |
| 15-comedy_only.sql | Comedy shows |
| 16-shows_by_genre.sql | All shows and their genres |
