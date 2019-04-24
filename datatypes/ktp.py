'''

This module generates Indonesian identity card

'''

from common import helpers
import random,datetime

class Datatype:

    def __init__(self, cli_object):
        self.cli = "ktp"
        self.description = "Indonesian Identity Card"
        self.filetype = "text"
        self.datasize = int(cli_object.data_size)

    def generate_no_kk(self):
        return random.randint(100000,900000)

    def generate_no_urut(self):
        rand_comp = random.randint(1,9999)
        return "%04d" % rand_comp   

    def generate_random_date(self):
        now = datetime.datetime.now()
        earliest = datetime.date(1945,1,1)
        latest  = datetime.date((now.year-17),1,1)
        delta = latest - earliest

        int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
        random_second = random.randrange(int_delta)
        dtm = earliest + datetime.timedelta(seconds = random_second)
        
        date = int(dtm.strftime('%d'))

        if date % 2:
            return '{}{}'.format(date+40,dtm.strftime('%m%y'))
        else:
            return dtm.strftime('%d%m%y')

    def generate_data(self):

        print "[*] Generating data..."
        nik = ''
        
        for single_ni in range(0, 100000 * self.datasize):
            nik += "{}{}{}".format(self.generate_no_kk(),self.generate_random_date(),self.generate_no_urut()) + ', '
        
        return nik
