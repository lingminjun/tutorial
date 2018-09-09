

import pymysql, os, configparser
from pymysql.cursors import DictCursor
from DBUtils.PooledDB import PooledDB


"""
配置mysql数据库连接池
直接返回连接
"""
class MysqlConf(object):
    mincached=1
    maxcached=20
    host='127.0.0.1'
    port=3306
    user='root'
    passwd=''
    db='database'
    use_unicode=False
    charset="utf8mb4"   # charset="utf8"


class MysqlConn(object):
    __conn = None
    __cursor = None
    __commit = 0

    def __init__(self, conn):
        self.__conn = conn
        # self.__conn.autocommit(1)
        self.__cursor = self.__conn.cursor()

    def getCount(self, table, condition=None, param=None):
        """
        @summary: 结果集总数
        @param table:查询对应的表
        @param condition: string where子句子 注入风险，故参数请使用param
        @param param: 可选参数，条件列表值（元组/列表）
        @return: result 结果集总数
        """
        sql = 'select count(1) from ' + table
        if condition is not None:
            sql = sql + ' where ' + condition
        
        sql = sql + ' ;'

        if param is None:
            count = self.__cursor.execute(sql)
        else:
            count = self.__cursor.execute(sql, param)
        return count

    def getAll(self, table, condition=None, param=None):
        """
        @summary: 结果集总数
        @param table:查询对应的表
        @param condition: string where子句子 注入风险，故参数请使用param
        @param param: 可选参数，条件列表值（元组/列表）
        @return: result 结果集总数
        """
        sql = 'select * from ' + table
        if condition is not None:
            sql = sql + ' where ' + condition
        sql = sql + ' ;'
        return self.prepare(sql=sql, param=param)

    def getOne(self, table, condition=None, param=None):
        """
        @summary: 执行查询，并取出第一条
        @param table:查询对应的表
        @param condition: string where子句子 注入风险，故参数请使用param
        @param param: 可选参数，条件列表值（元组/列表）
        @return: result list/boolean 查询到的结果集
        """
        sql = 'select * from ' + table
        if condition is not None:
            sql = sql + ' where ' + condition
        sql = sql + ' limit 1 ;'
        return self.prepare(sql=sql, num=1, param=param)

    def getMany(self, table, num, condition=None, param=None):
        """
        @summary: 执行查询，并取出num条结果
        @param table:查询对应的表
        @param num:取得的结果条数
        @param condition: string where子句子 注入风险，故参数请使用param
        @param param: 可选参数，条件列表值（元组/列表）
        @return: result list/boolean 查询到的结果集
        """
        sql = 'select * from ' + table
        if condition is not None:
            sql = sql + ' where ' + condition
        
        sql = sql + ' ;'

        return self.prepare(sql=sql, num=num, param=param)

    def prepare(self, sql, num=None, param=None):
        """
        @summary: 执行查询，并取出所有结果集
        @param sql:查询ＳＱＬ，如果有查询条件，请只指定条件列表，并将条件值使用参数[param]传递进来
        @param num:取得的结果条数
        @param param: 可选参数，条件列表值（元组/列表）
        @return: result list(字典对象)/boolean 查询到的结果集
        """
        print('prepare sql[' + sql + ']')
        if param is None:
            count = self.__cursor.execute(sql)
        else:
            count = self.__cursor.execute(sql, param)
        if count > 0:
            if num is None:
                result = self.__cursor.fetchall()
            elif num == 1:
                result = self.__cursor.fetchone()
            else:
                result = self.__cursor.fetchmany(num)
        else:
            result = False
        return result

    def inserts(self, sql, values):
        """
        @summary: 向数据表插入多条记录
        @param sql:要插入的ＳＱＬ格式
        @param values: 要插入的记录数据tuple(tuple)/list[list]
        @return: count 受影响的行数
        """
        count = self.__cursor.executemany(sql, values)
        return count

    def execute(self, sql, param=None):
        """
        @summary: 执行sql语句
        @param sql:需要执行的ＳＱＬ格式
        @param values: 要插入的记录数据tuple(tuple)/list[list]
        @return: count 受影响的行数
        """
        print('execute sql[' + sql + ']')
        if param is None:
            count = self.__cursor.execute(sql)
        else:
            count = self.__cursor.execute(sql, param)
        return count

    def update(self, table, fields, condition=None, param=None):
        """
        @summary: 更新数据表记录
        @param table: 表名字
        @param fields: 要更新的 键值对 {}/字典
        @param condition: string where子句子 注入风险，故参数请使用param
        @param param: 要更新的条件参数值 tuple/list
        @return: count 受影响的行数
        """
        if fields is None:
            return 0

        # UPDATE %s SET name = "%s" WHERE id = %s
        sql = 'update ' + table + ' set '
        first = True
        lst = []
        for key in fields:
            value = fields[key]
            if first :
                first = False
            else:
                sql = sql + ', '
            sql = sql + key + ' = %s'
            lst.append(value)

        if condition is not None:
            sql = sql + ' where ' + condition

        sql = sql + ' ;'

        if param is not None:
            for i in range(len(param)): 
                pm = param[i]
                lst.append(pm)

        # print(lst)
        return self.execute(sql, lst)

    def insert(self, table, fields):
        """
        @summary: 更新数据表记录
        @param table: 表名字
        @param fields: 要更新的 键值对 {}/字典
        @param param: 要更新的条件参数值 tuple/list
        @return: count 受影响的行数
        """
        if fields is None:
            return 0
        # UPDATE %s SET name = "%s" WHERE id = %s
        sql = 'insert into ' + table + '('
        valuestr = ' values('
        first = True
        lst = []
        for key in fields:
            value = fields[key]
            if first :
                first = False
            else:
                sql = sql + ', '
                valuestr = valuestr + ', '
            sql = sql + key
            valuestr = valuestr + '%s'
            lst.append(value)

        sql = sql + ') '
        valuestr = valuestr + ')'
        sql = sql + valuestr

        sql = sql + ' ;'

        # print(lst)
        return self.execute(sql, lst)

    def upinsert(self, table, fields):
        """
        @summary: 插入或者更新记录（必须有唯一主键）
        @param table: 表名字
        @param fields: 要更新的 键值对 {}/字典
        @return: count 受影响的行数
        """
        if fields is None:
            return 0
        #  insert into t1(a,b) values( '3','r5') on duplicate key update b='r5'; 
        sql = 'insert into ' + table + '('
        valuestr = ' values('
        updatestr = ' on duplicate key update '
        first = True
        lst = []
        for key in fields:
            value = fields[key]
            if first :
                first = False
            else:
                sql = sql + ', '
                valuestr = valuestr + ', '
                updatestr = updatestr + ', '
            sql = sql + key
            valuestr = valuestr + '%s'
            updatestr = updatestr + key + ' = %s'
            lst.append(value)

        # update语句参数重复加入
        for key in fields:
            value = fields[key]
            lst.append(value)

        sql = sql + ') '
        valuestr = valuestr + ')'
        sql = sql + valuestr + updatestr + ' ;'

        # print(lst)
        return self.execute(sql, lst)

    def delete(self, table, condition, param=None):
        """
        @summary: 删除数据表记录
        @param sql: 表名字
        @param condition: string where子句子 注入风险，故参数请使用param
        @param param: 要更新的条件参数值 tuple/list
        @return: count 受影响的行数
        """
        sql = 'delete from ' + table + ' where ' + condition + ' ;'
        return self.execute(sql, param)

    def begin(self):
        """
        @summary: 开启事务
        """
        if self.__commit == 0:
            self.__conn.autocommit(0)
        self.__commit = self.__commit + 1

    def end(self, option='commit'):
        """
        @summary: 结束事务
        """
        if self.__commit <= 0:
            return
        self.__commit = self.__commit - 1

        if self.__commit == 0:
            if option == 'commit':
                self.__conn.commit()
            else:
                self.__conn.rollback()

    def __del__(self):
        """
        @summary: 释放连接池资源
        """
        if self.__commit > 0:
            self.__conn.commit()

        self.__cursor.close()
        self.__conn.close()
        print('释放链接')


class MysqlPool(object):
    """
    MYSQL数据库对象，负责产生数据库连接 , 此类中的连接采用连接池实现获取连接对象：conn = Mysql.getConn()
            释放连接对象;conn.close()或del conn
    """
    # 连接池对象
    __pool = None
    # _conn = None
    # _cursor = None

    def __init__(self,host,user,pswd,min=1,max=20,port=3306,db='database',unicode=False,charset="utf8"):
        self.__pool = PooledDB(creator=pymysql,mincached=min,maxcached=max,host=host,port=port,user=user,passwd=pswd,db=db,use_unicode=unicode,charset=charset,cursorclass=DictCursor)
        pass


    def __del__(self):
        self.__pool.close()
        print('释放链接池')


    def conn(self):
        """
        @summary: 静态方法，从连接池中取出连接
        @return MysqlConn
        """
        return MysqlConn(self.__pool.connection())


    
