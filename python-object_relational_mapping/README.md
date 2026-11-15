# Python - Object-relational mapping

Connecting Python to MySQL with `MySQLdb` (raw SQL) and `SQLAlchemy` (ORM).

| File | Description |
|------|-------------|
| 0-select_states.py | All states (MySQLdb) |
| 1-filter_states.py | States starting with `N` |
| 2-my_filter_states.py | States matching an argument (format) |
| 3-my_safe_filter_states.py | Same, safe from SQL injection |
| 4-cities_by_state.py | All cities with their state |
| 5-filter_cities.py | Cities of a given state |
| model_state.py | `State` SQLAlchemy model |
| 6-model_state.py | Create the `states` table |
| 7-model_state_fetch_all.py | All states (SQLAlchemy) |
| 8-model_state_fetch_first.py | First state |
| 9-model_state_filter_a.py | States containing `a` |
| 10-model_state_my_get.py | Id of a state by name |
| 11-model_state_insert.py | Add Louisiana |
| 12-model_state_update_id_2.py | Rename state 2 to New Mexico |
| 13-model_state_delete_a.py | Delete states containing `a` |
| model_city.py | `City` SQLAlchemy model |
| 14-model_city_fetch_by_state.py | All cities with their state |
