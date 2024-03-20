# MySQL DB replication essential vocabulary

Some key vocabulary for MySQL database replication:

- Source database
- Replica database
- IO thread
- SQL thread
- Binary log
- Relay log
- Binary log file position-based replication
- transaction based replication (GTID)

## binary log file informations

- bin log file: mysql-bin.000001
- db name:      tyrell_corp
- line number:  154

## MySQL replication settings

### For MySQL Version 8+

```SQL
mysql> CHANGE REPLICATION SOURCE TO
            SOURCE_HOST='18.234.169.238',
            SOURCE_USER='replica_user',
            SOURCE_PASSWORD='full_belly_42',
            SOURCE_LOG_FILE='mysql-bin.000001',
            SOURCE_LOG_POS=154;
mysql> START REPLICA;
```

### For MySQL Version 5.7

```SQL
mysql> CHANGE MASTER TO
            MASTER_HOST='18.234.169.238',
            MASTER_USER='replica_user',
            MASTER_PASSWORD='full_belly_42',
            MASTER_LOG_FILE='mysql-bin.000001',
            MASTER_LOG_POS=154;

mysql> START SLAVE;
```
