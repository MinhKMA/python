```sh
mysql> select * from check_host;
+----+----------+--------+----------+---------+
| id | hostname | status | group_id | user_id |
+----+----------+--------+----------+---------+
|  2 | Gooloe   |     -1 |        1 |       2 |
|  3 | New DNS  |     -1 |        1 |       2 |
|  4 | Google2  |     -1 |        4 |       2 |
+----+----------+--------+----------+---------+
3 rows in set (0,00 sec)

mysql> select * from check_group_attribute;
+----+----------------+-------+------------+----------+
| id | attribute_name | value | type_value | group_id |
+----+----------------+-------+------------+----------+
|  1 | interval_time  | 20    |          0 |        1 |
|  2 | number_packet  | 15    |          0 |        1 |
|  3 | interval_time  | 25    |          0 |        2 |
|  4 | number_packet  | 17    |          0 |        2 |
+----+----------------+-------+------------+----------+
4 rows in set (0,00 sec)

mysql> select * from check_group;
+----+---------------+------+---------+----------+------------+
| id | group_name    | ok   | warning | critical | service_id |
+----+---------------+------+---------+----------+------------+
|  1 | Group_ping_01 |   10 |      30 |      100 |          1 |
|  2 | Group_ping_02 |   15 |      30 |       90 |          1 |
|  3 | ping_01_admin |   20 |      30 |      100 |          1 |
|  4 | Group_htpp_01 |    6 |      10 |      100 |          2 |
+----+---------------+------+---------+----------+------------+
4 rows in set (0,01 sec)

mysql> SELECT * FROM check_group OUTER JOIN check_group_attribute ON check_group.group_id = check_group_attribute.group_id;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'OUTER JOIN check_group_attribute ON check_group.group_id = check_group_attribute' at line 1
mysql> SELECT * FROM check_group INNER JOIN check_group_attribute ON check_group.group_id = check_group_attribute.group_id;
ERROR 1054 (42S22): Unknown column 'check_group.group_id' in 'on clause'
mysql> SELECT * FROM check_group INNER JOIN check_group_attribute ON check_group.id = check_group_attribute.group_id;
+----+---------------+------+---------+----------+------------+----+----------------+-------+------------+----------+
| id | group_name    | ok   | warning | critical | service_id | id | attribute_name | value | type_value | group_id |
+----+---------------+------+---------+----------+------------+----+----------------+-------+------------+----------+
|  1 | Group_ping_01 |   10 |      30 |      100 |          1 |  1 | interval_time  | 20    |          0 |        1 |
|  1 | Group_ping_01 |   10 |      30 |      100 |          1 |  2 | number_packet  | 15    |          0 |        1 |
|  2 | Group_ping_02 |   15 |      30 |       90 |          1 |  3 | interval_time  | 25    |          0 |        2 |
|  2 | Group_ping_02 |   15 |      30 |       90 |          1 |  4 | number_packet  | 17    |          0 |        2 |
+----+---------------+------+---------+----------+------------+----+----------------+-------+------------+----------+
4 rows in set (0,00 sec)

mysql> select * from check_host;
+----+----------+--------+----------+---------+
| id | hostname | status | group_id | user_id |
+----+----------+--------+----------+---------+
|  2 | Gooloe   |     -1 |        1 |       2 |
|  3 | New DNS  |     -1 |        1 |       2 |
|  4 | Google2  |     -1 |        4 |       2 |
+----+----------+--------+----------+---------+
3 rows in set (0,00 sec)

mysql> select * from check_group;
+----+---------------+------+---------+----------+------------+
| id | group_name    | ok   | warning | critical | service_id |
+----+---------------+------+---------+----------+------------+
|  1 | Group_ping_01 |   10 |      30 |      100 |          1 |
|  2 | Group_ping_02 |   15 |      30 |       90 |          1 |
|  3 | ping_01_admin |   20 |      30 |      100 |          1 |
|  4 | Group_htpp_01 |    6 |      10 |      100 |          2 |
+----+---------------+------+---------+----------+------------+
4 rows in set (0,00 sec)

mysql> select * from check_group_attribute;
+----+----------------+-------+------------+----------+
| id | attribute_name | value | type_value | group_id |
+----+----------------+-------+------------+----------+
|  1 | interval_time  | 20    |          0 |        1 |
|  2 | number_packet  | 15    |          0 |        1 |
|  3 | interval_time  | 25    |          0 |        2 |
|  4 | number_packet  | 17    |          0 |        2 |
+----+----------------+-------+------------+----------+
4 rows in set (0,00 sec)

mysql> SELECT * FROM check_group INNER JOIN check_group_attribute ON check_group.id = check_group_attribute.group_id;
+----+---------------+------+---------+----------+------------+----+----------------+-------+------------+----------+
| id | group_name    | ok   | warning | critical | service_id | id | attribute_name | value | type_value | group_id |
+----+---------------+------+---------+----------+------------+----+----------------+-------+------------+----------+
|  1 | Group_ping_01 |   10 |      30 |      100 |          1 |  1 | interval_time  | 20    |          0 |        1 |
|  1 | Group_ping_01 |   10 |      30 |      100 |          1 |  2 | number_packet  | 15    |          0 |        1 |
|  2 | Group_ping_02 |   15 |      30 |       90 |          1 |  3 | interval_time  | 25    |          0 |        2 |
|  2 | Group_ping_02 |   15 |      30 |       90 |          1 |  4 | number_packet  | 17    |          0 |        2 |
+----+---------------+------+---------+----------+------------+----+----------------+-------+------------+----------+
4 rows in set (0,00 sec)

mysql> SELECT * FROM ((check_group INNER JOIN check_group_attribute ON check_group.id = check_group_attribute.group_id) INNER JOIN check_host ON check_host.group_id = check_group.id ) ;
+----+---------------+------+---------+----------+------------+----+----------------+-------+------------+----------+----+----------+--------+----------+---------+
| id | group_name    | ok   | warning | critical | service_id | id | attribute_name | value | type_value | group_id | id | hostname | status | group_id | user_id |
+----+---------------+------+---------+----------+------------+----+----------------+-------+------------+----------+----+----------+--------+----------+---------+
|  1 | Group_ping_01 |   10 |      30 |      100 |          1 |  1 | interval_time  | 20    |          0 |        1 |  2 | Gooloe   |     -1 |        1 |       2 |
|  1 | Group_ping_01 |   10 |      30 |      100 |          1 |  2 | number_packet  | 15    |          0 |        1 |  2 | Gooloe   |     -1 |        1 |       2 |
|  1 | Group_ping_01 |   10 |      30 |      100 |          1 |  1 | interval_time  | 20    |          0 |        1 |  3 | New DNS  |     -1 |        1 |       2 |
|  1 | Group_ping_01 |   10 |      30 |      100 |          1 |  2 | number_packet  | 15    |          0 |        1 |  3 | New DNS  |     -1 |        1 |       2 |
+----+---------------+------+---------+----------+------------+----+----------------+-------+------------+----------+----+----------+--------+----------+---------+
4 rows in set (0,00 sec)
```
