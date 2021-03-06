# -*- coding: utf-8 -*-
from __future__ import with_statement
import MySQLdb


class MySQL:
    def __init__(self, ip, user, password, db_name):
        try:
            self.db = MySQLdb.connect(ip, user, password, db_name)
        except Exception, e:
            print e
            raise IOError('connection failed')
        self.cursor = self.db.cursor()

    def select(self, sql):
        self.cursor.execute(sql)
        print '受影响的行数一共有%d行' % self.cursor.rowcount
        return self.cursor.fetchall()

    def close(self):
        self.db.close()
        print '-' * 50

    def insert(self, sql):
        try:
            self.cursor.execute(sql)
            self.db.commit()
            print '受影响的行数一共有%d行' % self.cursor.rowcount
            print '插入成功！！'
        except Exception, e:
            self.db.rollback()
            print '插入失败！！'
            print e

    def update(self, sql):
        try:
            self.cursor.execute(sql)
            self.db.commit()
            print '受影响的行数一共有%d行' % self.cursor.rowcount
            print '更新成功！！'
        except Exception, e:
            self.db.rollback()
            print '更新失败！！'
            print e

    def delete(self, sql):
        try:
            self.cursor.execute(sql)
            self.db.commit()
            print '受影响的行数一共有%d行' % self.cursor.rowcount
            print '删除成功！！'
        except Exception, e:
            self.db.rollback()
            print '删除失败！！'
            print e


if __name__ == '__main__':
    """select"""
    a = MySQL('localhost', 'root', 'admin', 'Mysql')
    sql = "SELECT * FROM test WHERE sex = 'male'"
    try:
        result = a.select(sql)
        c = []
        b = {}
        index = 0
        for re in result:
            No = re[0]
            name = re[1]
            sex = re[2]
            age = re[3]
            c.append(name)
            b[index] = re
            index += 1
            print No, name, sex, age
    except Exception, e:
        print e
        raise IOError
    finally:
        a.close()
    print c
    print b

    """insert"""
    b = MySQL('localhost', 'root', 'admin', 'Mysql')
    sql2 = "INSERT INTO `mysql`.`test` (`no`, `name`, `sex`, `age`) VALUES ('4', 'godda', 'male', '38')"
    b.insert(sql2)
    b.close()

    """update"""
    c = MySQL('localhost', 'root', 'admin', 'Mysql')
    sql3 = "UPDATE `mysql`.`test` SET `sex`='m' WHERE (`sex`='male')"
    c.update(sql3)
    c.close()

    """delete"""
    d = MySQL('localhost', 'root', 'admin', 'Mysql')
    sql4 = "DELETE FROM `mysql`.`test` WHERE no = '4'"
    d.delete(sql4)
    d.close()
