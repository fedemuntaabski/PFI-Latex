# Perfilado de completitud de CLUE-LDS (data\clue.json)

50,522,931 eventos, 2017-07-07T08:57:57Z a 2022-09-29T08:26:05Z. Generado por `scripts/evidencia/perfilado_clue.py`.

| campo | falta (%) | null / vacío / unknown (%) | sin dato (%) | cardinalidad |
|---|---|---|---|---|
| `id` | 0.0 | 0.0 | 0.0 |  |
| `time` | 0.0 | 0.0 | 0.0 |  |
| `uid` | 0.0 | 0.0 | 0.0 | 5389 |
| `uidType` | 0.0 | 0.0 | 0.0 | 2 |
| `type` | 0.0 | 0.0 | 0.0 | 49 |
| `params` | 0.0 | 0.4918 | 0.4918 |  |
| `location` | 99.7578 | 0.0 | 99.7578 |  |
| `role` | 87.8033 | 0.0 | 87.8033 | 7 |
| `isLocalIP` | 99.4528 | 0.0 | 99.4528 | 3 |
| `location.countryCode` | 0.0 | 99.7579 | 99.7579 | 52 |
| `location.city` | 0.0 | 99.7847 | 99.7847 | 584 |
| `location.latitude` | 0.0 | 99.7578 | 99.7578 |  |
| `location.longitude` | 0.0 | 99.7578 | 99.7578 |  |

## Eventos por tipo

| tipo | eventos | % |
|---|---|---|
| 'file_accessed' | 18,447,579 | 36.5133 |
| 'login_attempt' | 13,227,628 | 26.1814 |
| 'login_successful' | 12,920,800 | 25.5741 |
| 'file_written' | 1,796,064 | 3.5549 |
| 'admin_settings_changed' | 1,091,611 | 2.1606 |
| 'file_updated' | 920,986 | 1.8229 |
| 'file_created' | 876,081 | 1.734 |
| 'version_deleted' | 629,589 | 1.2461 |
| 'user_data_viewed' | 198,431 | 0.3928 |
| 'login_failed' | 130,552 | 0.2584 |
| 'deleted_from_trashbin' | 110,222 | 0.2182 |
| 'file_deleted' | 86,895 | 0.172 |
| 'public_share_accessed' | 28,502 | 0.0564 |
| 'file_renamed' | 28,018 | 0.0555 |
| 'public_share_password_changed' | 9,516 | 0.0188 |
| 'logout_occured' | 4,069 | 0.0081 |
| 'command_executed' | 4,024 | 0.008 |
| 'shared_user' | 2,666 | 0.0053 |
| 'shared_link' | 2,505 | 0.005 |
| 'unshared_link' | 1,793 | 0.0035 |
| 'public_share_update_permission' | 863 | 0.0017 |
| 'restored_from_trashbin' | 831 | 0.0016 |
| 'permission_changed' | 674 | 0.0013 |
| 'public_share_expiration_date_changed' | 627 | 0.0012 |
| 'unshared_user' | 519 | 0.001 |
| 'user_added_to_group' | 519 | 0.001 |
| 'user_removed_from_group' | 190 | 0.0004 |
| 'user_created' | 145 | 0.0003 |
| 'user_deleted' | 144 | 0.0003 |
| 'email_changed' | 136 | 0.0003 |
| 'shared_group' | 103 | 0.0002 |
| 'password_changed' | 74 | 0.0001 |
| 'quota_changed' | 73 | 0.0001 |
| 'file_copied' | 69 | 0.0001 |
| 'user_became_groupadmin' | 62 | 0.0001 |
| 'user_assign' | 57 | 0.0001 |
| 'shared_email' | 52 | 0.0001 |
| 'app_enabled' | 50 | 0.0001 |
| 'group_created' | 47 | 0.0001 |
| 'unshared_email' | 36 | 0.0001 |
| 'app_disabled' | 34 | 0.0001 |
| 'unshared_group' | 27 | 0.0001 |
| 'fullname_changed' | 20 | 0.0 |
| 'version_restored' | 19 | 0.0 |
| 'groupadmin_removed_from_group' | 13 | 0.0 |
| 'group_deleted' | 10 | 0.0 |
| 'comment_added' | 4 | 0.0 |
| 'user_disabled' | 1 | 0.0 |
| 'comment_deleted' | 1 | 0.0 |

## Valores más frecuentes

- `uidType`: 'name' (99.7112 %), 'ipaddress' (0.2888 %)
- `role`: '<falta>' (87.8033 %), 'technical' (6.1686 %), 'management' (3.4656 %), 'administration' (1.7004 %), 'external' (0.6682 %), 'consulting' (0.1674 %), 'sales' (0.0265 %)
- `isLocalIP`: '<falta>' (99.4528 %), True (0.3049 %), False (0.2422 %)
- `location.countryCode`: <null> (99.7579 %), AT (0.2021 %), DE (0.0182 %), IR (0.0062 %), NL (0.005 %), US (0.0043 %), HU (0.0012 %), IT (0.0008 %)

Claves de `params`: user (52.0167 %), path (45.1738 %), app (2.1608 %), value (2.1606 %), key (2.1606 %), trigger (1.2461 %), run (0.6403 %), ip (0.2584 %), uidOwner (0.0944 %), itemSource (0.0944 %), itemType (0.0944 %), token (0.0803 %)

ids no crecientes respecto del anterior: 0.
