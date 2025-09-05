import sys
from src.logger import logging
def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()#getting exception info
    file_name=exc_tb.tb_frame.f_code.co_filename#getting file name where exception occurred
    error_message="Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name,exc_tb.tb_lineno,str(error)#formatting error message
    )
    return error_message
class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)#calling parent class constructor
        self.error_message=error_message_detail(error_message,error_detail)#error message with details
    def __str__(self):
        return self.error_message
