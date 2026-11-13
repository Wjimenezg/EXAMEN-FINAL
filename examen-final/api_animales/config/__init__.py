# =============================================================================
# __init__.py del paquete config: se ejecuta antes que settings.py cuando
# Django importa "config", por eso es buen lugar para preparar el driver de MySQL.
# =============================================================================

# PyMySQL permite usar MySQL sin compilar mysqlclient
# (PyMySQL está escrito 100% en Python, así que se instala fácil en Windows)
import pymysql

# Django espera el módulo "MySQLdb" (de mysqlclient). Esta línea hace que
# PyMySQL se registre con ese nombre, así Django lo usa sin notar la diferencia.
pymysql.install_as_MySQLdb()
