```sh
mysql> DESCRIBE check_group;
+-------------+-------------+------+-----+---------+----------------+
| Field       | Type        | Null | Key | Default | Extra          |
+-------------+-------------+------+-----+---------+----------------+
| id          | int(11)     | NO   | PRI | NULL    | auto_increment |
| group_name  | varchar(45) | NO   |     | NULL    |                |
| description | longtext    | YES  |     | NULL    |                |
| ok          | int(11)     | YES  |     | NULL    |                |
| warning     | int(11)     | YES  |     | NULL    |                |
| critical    | int(11)     | YES  |     | NULL    |                |
| service_id  | int(11)     | NO   | MUL | NULL    |                |
| user_id     | int(11)     | NO   | MUL | NULL    |                |
+-------------+-------------+------+-----+---------+----------------+
8 rows in set (0,00 sec)

mysql> DESCRIBE check_group_attribute;
+----------------+--------------+------+-----+---------+----------------+
| Field          | Type         | Null | Key | Default | Extra          |
+----------------+--------------+------+-----+---------+----------------+
| id             | int(11)      | NO   | PRI | NULL    | auto_increment |
| attribute_name | varchar(45)  | NO   |     | NULL    |                |
| value          | varchar(100) | NO   |     | NULL    |                |
| type_value     | int(11)      | YES  |     | NULL    |                |
| group_id       | int(11)      | NO   | MUL | NULL    |                |
+----------------+--------------+------+-----+---------+----------------+
5 rows in set (0,00 sec)

mysql> DESCRIBE check_host;
+-------------+-------------+------+-----+---------+----------------+
| Field       | Type        | Null | Key | Default | Extra          |
+-------------+-------------+------+-----+---------+----------------+
| id          | int(11)     | NO   | PRI | NULL    | auto_increment |
| hostname    | varchar(45) | NO   |     | NULL    |                |
| description | longtext    | YES  |     | NULL    |                |
| status      | int(11)     | NO   |     | NULL    |                |
| group_id    | int(11)     | NO   | MUL | NULL    |                |
+-------------+-------------+------+-----+---------+----------------+
5 rows in set (0,00 sec)

mysql> DESCRIBE check_host_attribute;
+----------------+--------------+------+-----+---------+----------------+
| Field          | Type         | Null | Key | Default | Extra          |
+----------------+--------------+------+-----+---------+----------------+
| id             | int(11)      | NO   | PRI | NULL    | auto_increment |
| attribute_name | varchar(45)  | NO   |     | NULL    |                |
| value          | varchar(100) | NO   |     | NULL    |                |
| type_value     | int(11)      | YES  |     | NULL    |                |
| host_id        | int(11)      | NO   | MUL | NULL    |                |
+----------------+--------------+------+-----+---------+----------------+
5 rows in set (0,00 sec)

mysql> DESCRIBE check_service;
+--------------+-------------+------+-----+---------+----------------+
| Field        | Type        | Null | Key | Default | Extra          |
+--------------+-------------+------+-----+---------+----------------+
| id           | int(11)     | NO   | PRI | NULL    | auto_increment |
| service_name | varchar(45) | NO   |     | NULL    |                |
+--------------+-------------+------+-----+---------+----------------+
2 rows in set (0,00 sec)

mysql> SELECT * FROM check_group;
+----+---------------+-----------------------+------+---------+----------+------------+---------+
| id | group_name    | description           | ok   | warning | critical | service_id | user_id |
+----+---------------+-----------------------+------+---------+----------+------------+---------+
|  1 | Group_ping_01 | here is default group |   11 |      20 |      100 |          1 |       1 |
|  2 | Group_ping_02 |                       |   10 |      40 |      100 |          1 |       1 |
+----+---------------+-----------------------+------+---------+----------+------------+---------+
2 rows in set (0,00 sec)

mysql> SELECT * FROM check_group_attribute;
+----+----------------+-------+------------+----------+
| id | attribute_name | value | type_value | group_id |
+----+----------------+-------+------------+----------+
|  1 | interval_time  | 20    |          0 |        1 |
|  2 | number_packet  | 20    |          0 |        1 |
|  3 | interval_ping  | 20    |          0 |        2 |
|  4 | number_packet  | 20    |          0 |        2 |
+----+----------------+-------+------------+----------+
4 rows in set (0,00 sec)

mysql> SELECT * FROM check_host;
+----+----------+-------------+--------+----------+
| id | hostname | description | status | group_id |
+----+----------+-------------+--------+----------+
|  3 | New DNS  | cc          |     -1 |        1 |
|  4 | Google   | okokok      |     -1 |        1 |
+----+----------+-------------+--------+----------+
2 rows in set (0,00 sec)

mysql> SELECT * FROM check_host_attribute;
+----+----------------+----------+------------+---------+
| id | attribute_name | value    | type_value | host_id |
+----+----------------+----------+------------+---------+
|  1 | ip_address     | 1.1.1.1  |          4 |       3 |
|  2 | ip_address     | 8.8.8.87 |          4 |       4 |
+----+----------------+----------+------------+---------+
2 rows in set (0,00 sec)

mysql> SELECT * FROM check_host;
+----+----------+-------------+--------+----------+
| id | hostname | description | status | group_id |
+----+----------+-------------+--------+----------+
|  3 | New DNS  | cc          |     -1 |        1 |
|  4 | Google   | okokok      |     -1 |        1 |
+----+----------+-------------+--------+----------+
2 rows in set (0,00 sec)
```
