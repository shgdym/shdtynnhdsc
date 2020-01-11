class Const(object):
    class ConstError(TypeError):
        pass

    class ConstCaseError(ConstError):
        pass

    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise self.ConstError("Can't change const.%s" % name)
        if not name.isupper():
            raise self.ConstCaseError('const name "%s" is not all supercase' % name)

        self.__dict__[name] = value

const = Const()

# mysql
const.DB_HOST  = '127.0.0.1'
const.DB_USER = 'root'
const.DB_PASS = 'YOURPASSWORD'
const.DB_NAME = 'YOURDBNAME'
const.DB_PORT = 3306